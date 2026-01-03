import unittest


from main import longestCommonPrefix


class TestLongestCommonPrefix(unittest.TestCase):
    def test_example1(self):
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        self.assertEqual(longestCommonPrefix(strs), expected)

    def test_example2(self):
        strs = ["dog", "racecar", "car"]
        expected = ""
        self.assertEqual(longestCommonPrefix(strs), expected)

    def test_empty_array(self):
        strs = []
        expected = ""
        self.assertEqual(longestCommonPrefix(strs), expected)

    def test_single_string(self):
        strs = ["single"]
        expected = "single"
        self.assertEqual(longestCommonPrefix(strs), expected)

    def test_no_common_prefix(self):
        strs = ["abc", "def", "ghi"]
        expected = ""
        self.assertEqual(longestCommonPrefix(strs), expected)

    def test_all_strings_identical(self):
        strs = ["same", "same", "same"]
        expected = "same"
        self.assertEqual(longestCommonPrefix(strs), expected)

    def test_partial_common_prefix(self):
        strs = ["interview", "internet", "internal", "interval"]
        expected = "inter"
        self.assertEqual(longestCommonPrefix(strs), expected)

    def test_leetcode_case(self):
        strs = ["ab", "a"]
        expected = "a"
        self.assertEqual(longestCommonPrefix(strs), expected)


unittest.main()
