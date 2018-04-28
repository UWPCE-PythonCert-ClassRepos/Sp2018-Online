import unittest
import Lesson_03_Activity as Activity


class TestLocke(unittest.TestCase):

    small_locke = Activity.Locke(5)
    large_locke = Activity.Locke(10)
    boats = 8

    def test_boats_to_locke(self):
        # tests the number of boats are less than the large locke, and greater than the small locke
        self.assertLess(self.boats, self.large_locke.capacity)
        self.assertGreater(self.boats, self.small_locke.capacity)

    def test_print_statements_small(self):
        # tests the print statements are present in operating the small locke
        self.assertIn("Stopping the pumps.", self.small_locke.message)
        self.assertIn("Opening the doors.", self.small_locke.message)
        self.assertIn("Closing the doors.", self.small_locke.message)
        self.assertIn("Restarting the pumps.", self.small_locke.message)

    def test_print_statements_large(self):
        # tests the print statements are present in operating the large locke
        self.assertIn("Stopping the pumps.", self.large_locke.message)
        self.assertIn("Opening the doors.", self.large_locke.message)
        self.assertIn("Closing the doors.", self.large_locke.message)
        self.assertIn("Restarting the pumps.", self.large_locke.message)

    def test_error_small(self):
        # tests a ValueError is raised when operating a small lock with too many boats
        self.assertRaises(ValueError, self.small_locke.move_boats_through, self.boats)

    def test_no_error_large(self):
        # tests no error is raised when operating a large locke with fewer boats
        self.large_locke.move_boats_through(self.boats)
        self.assertEqual(self.large_locke.num_boats, self.boats)


if __name__ == '__main__':
    unittest.main()

