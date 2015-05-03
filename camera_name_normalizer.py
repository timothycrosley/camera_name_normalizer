"""camera_name_normalizer.py

Provides a utility to take a set of files with camera models names and normalize them into a smaller more consistent
set of names.

usage:
    (normalized_data, change_map) = CameraNameNormalizer.normalize("path/data.set")

Copyright (C) 2015  Timothy Edmund Crosley
Under the MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

"""
class CameraNameNormalizer(dict):
    REPLACEMENTS = {'mark': 'mk', '1': 'i', '2': 'ii', '3': 'iii', '4': 'iv', '5': 'v', 'cannon': '', 'canon': '',
                    'cano ': ' ', 'nkon': '', 'nikon': '', 'go pro': '', 'gopro': ''}

    def _normalize(self, key):
        """Normalizes a camera name into the smallest possible representation"""
        normalized = key.lower()
        for to_replace, replacement in self.REPLACEMENTS.iteritems():
            normalized = normalized.replace(to_replace, replacement)
        return ''.join(normalized.split())

    def __getitem__(self, key):
        """Overides get item to return fully qualified label, independant of what value is passed in"""
        return dict.__getitem__(self, self._normalize(key))

    def add(self, camera_name):
        """Adds a camera a camera name to the dictionary, pointing the normalized version to the longest defined
           representation

        #"""
        camera_name = " ".join(part[0].upper() + part[1:] for part in camera_name.split())
        normalized = self._normalize(camera_name)
        existing_value = self.setdefault(normalized, camera_name)

        # If the camera name is longer or has more uppercase characters replace existing label
        if len(camera_name) > existing_value or (len(camera_name) == existing_value and
                                                 sum(ord(character) for character in camera_name) <
                                                 sum(ord(character) for character in existing_value)):
            self[normalized] = camera_name

        return normalized

    @classmethod
    def normalize(cls, file_name):
        """Takes a file containing camera names and returns a normalized_name -> long form label dictionary,
           alongside a mapping of all the values converted, to their new value.

        """
        normalized = cls()
        mapping = {}

        with open(file_name) as camera_data:
            for camera_name in (line.strip() for line in camera_data if line):
                mapping[camera_name] = normalized.add(camera_name)

            for mapped_from, mapped_to in mapping.items():
                mapping[mapped_from] = normalized[mapped_to]

        return (normalized, mapping)
