from django.test import TestCase

class FirstTestCase(TestCase):

    def setUp(self):
        pass
    
    def test_equal(self):
        self.assertEqual(1, 1)

    def test_patient_register(self):
        patients = [{
            "fullName":"Anshuman",
        }]


#     def test_first(self):
#         self.assertTrue(True)

# class SecondTestCase(TestCase):
#     def test_second(self):
#         self.assertTrue(True)