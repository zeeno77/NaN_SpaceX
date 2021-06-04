import controller
import unittest


class bug_test(unittest.TestCase):

    def setUp(self):
        self.bug = controller.Bug("Bug test")

    def test_create_bug(self):
        self.assertEqual(self.bug.description, "Bug test")
        self.assertIsNotNone(self.bug.title)
        self.assertEqual(self.bug.label, "Bug")


if __name__ == "__main__":
    unittest.main()
