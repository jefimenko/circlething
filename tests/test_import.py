from a_module import a_py_file


def test_my_foo():
    my_bar = a_py_file.foo()

    assert my_bar is 'bar'
