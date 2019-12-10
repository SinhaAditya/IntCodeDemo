import unittest

from IntCodeDemo.Intcode import IntCode


class MyTestCase(unittest.TestCase):

    def test_if_index_steps_forward_by_four(self):
        intcode = IntCode()
        self.assertEqual(intcode.position, 0)
        intcode.step()
        self.assertEqual(intcode.position, 4)


if __name__ == '__main__':
    unittest.main()
