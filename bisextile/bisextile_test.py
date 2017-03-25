import unittest

from bisextile import is_bisextile

class BisextileTest(unittest.TestCase):

    def test_une_anee_pas_divisible_par_4_est_pas_bisectile(self):
        self.assertEqual(False, is_bisextile(annee=3))
        self.assertEqual(False, is_bisextile(annee=2003))
        self.assertEqual(False, is_bisextile(annee=2013))


    def test_une_anee_divisible_par_4_est_bisectile(self):
        self.assertEqual(True, is_bisextile(annee=4))

    def test_une_anee_divisible_par_100_est_pas_bisectile(self):
        self.assertEqual(False, is_bisextile(annee=1900))

    def test_une_anee_divisible_par_400_est_bisectile(self):
        self.assertEqual(True, is_bisextile(annee=2000))
