import controller
import unittest


class task_test(unittest.TestCase):

    def setUp(self):
        self.maintenance = controller.Task("maintenance test", "Maintenance")
        self.research = controller.Task("research test", "Research")
        self.test = controller.Task("test(the task) test", "Test")
        self.notATask = controller.Task("This is not a valid task",
                                        "Invalid-Category")

    def test_create_maintenance(self):
        self.assertEqual(self.maintenance.title, "maintenance test")
        self.assertEqual(self.maintenance.label, "Maintenance")

    def test_create_research(self):
        self.assertEqual(self.research.title, "research test")
        self.assertEqual(self.research.label, "Research")

    def test_create_test(self):
        self.assertEqual(self.test.title, "test(the task) test")
        self.assertEqual(self.test.label, "Test")

    def test_create_invalid_task(self):
        self.assertFalse(hasattr(self.notATask, "title"))
        self.assertFalse(hasattr(self.notATask, "label"))


if __name__ == "__main__":
    unittest.main()
