"""
This be how we drive development with tests. Kind of.
"""

from a_module import a_py_file


def test_my_foo():
    my_bar = a_py_file.i_pity_duh_foo()

    assert my_bar is "bar"
