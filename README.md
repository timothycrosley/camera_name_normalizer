Camera Name Normalization
=====

Before normalization:

    Canon 5D mark II
    Canon 5d MKII
    Canon 5dMKII
    Canon 5D Mk III

After normalization:

    Canon 5D Mark II
    Canon 5D Mk III

Assumptions:

 - Python > 2.6 but < 3.0 is being used
 - The longer versions of Camera names are the more complete / correct ones
 - The list could potentially be much longer, so memory use should be conservative
    - Another pass could always be ran AFTER the list is reduced in size.


Using the normalizer
===================

**from within Python**:

    from .camera_name_normalizer import CameraNameNormalizer
    (normalized_data, change_map) = CameraNameNormalizer.normalize("camera_list.txt")
    new_unique_values = normalized_data.values()


Testing the normalizer
===================

In TDD fashion a test will be included with this excersize. To run the test, use py.test in the project directory.



Thought Process
===================

The thought process behind this implemntation is as follows:

If we can given a camera name, simplify (normalize it) into it's simplist possible form - that is consistent independant
of it's casing, spacing, and set of words used - we can then creating a mapping of the simplified form to the longest
best defined form within a given list. This allows the logic to be done in a quick single pass of the file, and allows
the resulting label to "Learn" with the data supplied (as a better defined label becomes available it is automatically
applied). Additionally, while two data structures are used in this example, strictly speaking only one small data
structure would be required using this approach (the mapping of the simplified form -> the best defined label available so far).

The extra data data set only exists because of the written requirement that there be a mapping of the original form to
its expanded form for all values. In practical applications the normalization method would allow you to always see what
the expanded form of any string would be on an on-demand basis. In fact, in the given code you can see what any value
in the list was mapped to by running normalized_data[original_value].

_________________________________________-

Thanks!

~Timothy Crosley
