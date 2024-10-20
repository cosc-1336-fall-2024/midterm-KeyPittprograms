#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import show_value, test_config
from src.question_b.question_b import get_day_of_week
from src.question_c.question_c import get_sum_of_evens
from src.question_d.question_d import get_person_category
class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_day_of_week(self):
        self.assertEqual("Invalid number", get_day_of_week(0))
        self.assertEqual("Monday", get_day_of_week(1))
        self.assertEqual("Tuesday", get_day_of_week(2))
        self.assertEqual("Wednesday", get_day_of_week(3))
        self.assertEqual("Thursday", get_day_of_week(4))
        self.assertEqual("Invalid number", get_day_of_week(8))

    def test_get_sum_of_evens(self):
        self.assertEqual(30, get_sum_of_evens(11))
        self.assertEqual(30, get_sum_of_evens(10))
        self.assertEqual(20, get_sum_of_evens(8))

    def test_get_person_category(self):
        self.assertEqual("Infant", get_person_category(1))
        self.assertEqual("Child", get_person_category(2))
        self.assertEqual("Teenager", get_person_category(14))
        self.assertEqual("Adult", get_person_category(20))

