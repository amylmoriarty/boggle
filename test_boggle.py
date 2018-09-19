import unittest
import boggle


class TestBoggle (unittest.TestCase):
    """
    Our Test Suite for Boggle Solver
 
    """
    def test_can_create_an_empty_grid (self):
        """
        Test to see if we can create an empty grid
        """
        grid = boggle.make_grid (0, 0)
        self.assertEqual(len (grid), 0 )
        
    