import unittest
from states import State


class TestState(unittest.TestCase):

    def test_state_name(self):
        stateObj = State(3)
        self.assertEqual(str(stateObj), "Shipping soon")

    def test_bad_state_id(self):
        with self.assertRaises(ValueError):
            State(-1)

        with self.assertRaises(ValueError):
            State(5)


if __name__ == '__main__':
    unittest.main()
