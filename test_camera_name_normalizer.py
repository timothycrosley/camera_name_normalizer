"""test_camera_name_normalizer.py

Tests to ensure that the camera_name normalization class works as expected.

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
from tempfile import NamedTemporaryFile
from .camera_name_normalizer import CameraNameNormalizer


def test_camera_normalization():
    """Test to define desired behaviour when parsing camera names from a file"""
    with NamedTemporaryFile('w') as test_file:
        test_file.write("Canon 5D mark II\n"
                        "Canon 5d MKII\n"
                        "Canon 5dMKII\n"
                        "Canon 5D Mk III\n")
        test_file.flush()
        (results, mappings) = CameraNameNormalizer.normalize(test_file.name)

        assert len(results) == 2
        assert set(results.values()) == set(('Canon 5D Mark II', 'Canon 5D Mk III'))

        assert mappings == {"Canon 5D mark II": "Canon 5D Mark II",
                            "Canon 5d MKII": "Canon 5D Mark II",
                            "Canon 5dMKII": "Canon 5D Mark II",
                            "Canon 5D Mk III": "Canon 5D Mk III"}
