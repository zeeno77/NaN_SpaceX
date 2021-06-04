import controller
import unittest


class issue_test(unittest.TestCase):

    def setUp(self):
        self.issue = controller.Issue("Issue test",
                                      "A nice description for this test")

    def test_create_issue(self):
        self.assertEqual(self.issue.title, "Issue test")
        self.assertEqual(self.issue.description,
                         "A nice description for this test")


if __name__ == "__main__":
    unittest.main()
