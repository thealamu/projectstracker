import unittest
from states import State
from states import id_for_string


class TestState(unittest.TestCase):

    def test_state_name(self):
        stateObj = State(3)
        self.assertEqual(str(stateObj), "Shipping soon")

    def test_bad_state_id(self):
        with self.assertRaises(ValueError):
            State(-1)

        with self.assertRaises(ValueError):
            State(5)

    def test_id_for_string(self):
        self.assertEqual(id_for_string("PAUSED"), 1)
        self.assertEqual(id_for_string("Shipping soon"), 3)
        self.assertEqual(id_for_string("Doesn't exist"), 0)


if __name__ == '__main__':
    unittest.main()
