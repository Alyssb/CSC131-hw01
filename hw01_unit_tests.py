import unittest
import filecmp
from csc131 import hw01


class Hw01UnitTests(unittest.TestCase):
    """
    Unit tests for the `csc131.hw01` module.
    """

    def setUp(self):
        """
        Set up the test fixture; this is executed before each unit test executes.
        :return: None
        """
        self.my_dictionary = {}

    def tearDown(self):
        """
        Clean up the test fixture; this executed after each unit test has executed.
        :return: None
        """
        self.my_dictionary = None

    def test_read(self):
        """
        Unit test that validates the `get_concordance_for_file` function.
        :return: None
        """
        self.my_dictionary = hw01.get_concordance_for_file("./csc131/input.txt")
        self.assertIsNotNone(self.my_dictionary)
        expected_dict = {'box': 1, 'animal': 4, 'camel': 2, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                         'missouri': 2, 'state': 2, 'fight': 2, 'song': 1, 'uphold': 1, 'tradition': 1, 'our': 2,
                         'school': 1, 'we': 3, 'hold': 1, 'so': 1, 'dear': 1, 'will': 1, 'be': 1, 'loyal': 1,
                         'throughout': 1, 'college': 1, 'years': 1, 'for': 2, 'victory': 1, 'while': 1, 'stand': 1,
                         'up': 1, 'and': 1, 'cheer': 1, 'lets': 1, 'hear': 1, 'it': 1, 'the': 1, 'bears': 3}
        self.assertDictEqual(self.my_dictionary, expected_dict)

    def test_write(self):
        """
        Unit test that validates the `save_results_in_file` function.
        :return: None
        """
        self.my_dictionary = {"one": 1, "two": 2, "three": 3, "four": 4}
        self.assertTrue(hw01.save_results_in_file(self.my_dictionary, "./csc131/output.txt"))
        actual_output_file_name = "./csc131/output.txt"
        expected_output_file_name = "./csc131/expected_output.txt"
        self.assertTrue(filecmp.cmp(actual_output_file_name, expected_output_file_name))


#
# Script entry-point enforcement.
#
if __name__ == '__main__':
    unittest.main()
