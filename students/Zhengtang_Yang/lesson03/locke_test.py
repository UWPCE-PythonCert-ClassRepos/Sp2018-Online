import unittest
from locke import Locke
from io import StringIO
from contextlib import redirect_stdout

class LockeTest(unittest.TestCase):

	def test_init(self):
		a = Locke(5)
		self.assertEqual(a._capacity_, 5)

		with self.assertRaises(ValueError):
			Locke(0)

	def test_enter(self):
		f = StringIO()
		locke = Locke(1)
		with redirect_stdout(f):
			a = locke.__enter__()
		
		self.assertIsInstance(a, Locke)
		self.assertIn("Stopping the pumps.", f.getvalue())
		self.assertIn("Opening the doors.", f.getvalue())

	def test_locke_exit(self):
		f = StringIO()
		a = Locke(1)
		with redirect_stdout(f):
			a.__exit__(None, None, None)

		self.assertIn("Closing the doors.", f.getvalue())
		self.assertIn("Restarting the pumps.", f.getvalue())

	def test_locke(self):
		f = StringIO()
		with redirect_stdout(f):
			with Locke(1):
				pass
		self.assertIn("Stopping the pumps.", f.getvalue())
		self.assertIn("Opening the doors.", f.getvalue())
		self.assertIn("Closing the doors.", f.getvalue())
		self.assertIn("Restarting the pumps.", f.getvalue())

	def test_move_boats_through(self):
		a = Locke(5)
        
		with self.assertRaises(ValueError):
			a.move_boats_through(6)

		try:
			a.move_boats_through(6)
		except ValueError as err:
			self.assertEqual(repr(err), "ValueError('Number of boat exceeds locke capacity 5',)")

if __name__ == '__main__':
	unittest.main()
