import unittest
from theater.theater import Theater

class TestTheaterClass(unittest.TestCase):

  def test_init(self):
    theater = Theater(5)
    self.assertIsInstance(theater, Theater)
  
  def test_instance_variables(self):
    theater = Theater(2)
    self.assertEqual(theater._seats, 2)
    self.assertEqual(theater._patrons, 0)

  def test_admit(self):
    theater = Theater(4)
    theater.admit(1)
    self.assertEqual(theater._patrons, 1)

    theater.admit(5)
    self.assertEqual(theater._patrons, 1)

  def test_at_capacity(self):
    theater = Theater(8)
    self.assertFalse(theater.at_capacity())
    theater.admit(8)
    self.assertTrue(theater.at_capacity())

  def test_record_walk_outs(self):
    theater = Theater(4)
    theater.admit(1)
    theater.record_walk_outs(2)
    self.assertEqual(theater._patrons, 1)
    theater.record_walk_outs(1)
    self.assertEqual(theater._patrons, 0)