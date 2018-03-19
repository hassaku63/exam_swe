from unittest import TestCase
from main import Charactor


class TestCharactor(TestCase):
    def setUp(self):
        self.charactor = Charactor("Male", "Wind", "Fighter", "Sword")

    def test_charactor(self):
        self.assertEqual(self.charactor.Sex, "Male")
        self.assertEqual(self.charactor.Element, "Wind")
        self.assertEqual(self.charactor.Job, "Fighter")
        self.assertEqual(self.charactor.Equipment, "Sword")

    def test_attack(self):
        self.assertEqual(self.charactor.attack, 60)

    def test_defence(self):
        self.assertEqual(self.charactor.defence, 40)

    def test_skill(self):
        self.assertEqual(self.charactor.skill, "ギガスラッシュ")
