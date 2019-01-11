# Ref: https://gist.github.com/brantfaircloth/764363
# modified from http://bit.ly/dEyw03


def create_dynamic_method(output, expected):
    """just don't include `test` in the function name here, nose will try to
    run it"""

    def dynamic_test_method(self):
        """this function name doesn't matter much, it can start with `test`,
        but we're going to rename it dynamically below"""
        self.assertEqual(output, expected)  # this is our actual assertion

    return dynamic_test_method


def gen_test(test_cls, cls, *input_expected_args):
    public_method_names = [method for method in dir(cls) if callable(getattr(cls, method)) if
                           not method.startswith('_')]  # 'private' methods start from _
    for method in sorted(public_method_names):
        print("Tests:", method)
        i = 1
        for input_expected in input_expected_args:
            dynamic_method = create_dynamic_method(getattr(cls, method)(*input_expected[0]), input_expected[1])
            dynamic_method.__name__ = 'test_{0}_TestCase_{1}'.format(method, i)
            # dynamic_method.__doc__ = 'my super great name {0}'.format(i)
            setattr(test_cls, dynamic_method.__name__, dynamic_method)
            i += 1
        # remove the last test name from the current namespace,
        # so nose doesn't run it
        # TODO it seem no need here
        del dynamic_method
