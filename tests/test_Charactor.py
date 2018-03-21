from unittest import TestCase
from charactor import Charactor


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
        self.assertEqual(self.charactor.skill.name, "ギガスラッシュ")

    def test_special_condition(self):
        """
        属性とジョブ、ジョブと装備で相乗効果のある組み合わせのテスト
        """
        testset = [["Male", "Wind", "Fighter", "Sword", 60, 40],
                   ["Male", "Wind", "Magician", "Stick", 60, 20],
                   ["Male", "Wind", "Martial", "Sword", 60, 40],
                   ["Male", "Wind", "Martial", "Stick", 60, 40],
                   ["Male", "Wind", "Martial", "Glove", 50, 30],
                   ["Male", "Water", "Fighter", "Sword", 65, 45],
                   ["Male", "Water", "Fighter", "Stick", 45, 25],
                   ["Male", "Water", "Fighter", "Glove", 35, 35],
                   ["Male", "Water", "Magician", "Stick", 65, 15],
                   ["Male", "Water", "Martial", "Stick", 45, 35],
                   ["Male", "Thunder", "Fighter", "Sword", 70, 30],
                   ["Male", "Thunder", "Magician", "Sword", 50, 35],
                   ["Male", "Thunder", "Magician", "Stick", 70, 15],
                   ["Male", "Thunder", "Magician", "Glove", 40, 25],
                   ["Male", "Thunder", "Martial", "Stick", 50, 30],
                   ["Female", "Wind", "Fighter", "Sword", 55, 45],
                   ["Female", "Wind", "Magician", "Stick", 55, 25],
                   ["Female", "Wind", "Martial", "Sword", 55, 45],
                   ["Female", "Wind", "Martial", "Stick", 55, 45],
                   ["Female", "Wind", "Martial", "Glove", 45, 35],
                   ["Female", "Water", "Fighter", "Sword", 60, 50],
                   ["Female", "Water", "Fighter", "Stick", 40, 30],
                   ["Female", "Water", "Fighter", "Glove", 30, 40],
                   ["Female", "Water", "Magician", "Stick", 60, 20],
                   ["Female", "Water", "Martial", "Stick", 40, 40],
                   ["Female", "Thunder", "Fighter", "Sword", 65, 35],
                   ["Female", "Thunder", "Magician", "Sword", 45, 40],
                   ["Female", "Thunder", "Magician", "Stick", 65, 20],
                   ["Female", "Thunder", "Magician", "Glove", 35, 30],
                   ["Female", "Thunder", "Martial", "Stick", 45, 35]]

        for case in testset:
            self._assert_atk_def(*case)

    def _assert_atk_def(self, sex, element, job, equip, attack, defence):
        c = Charactor(sex, element, job, equip)
        self.assertEqual((c.attack, c.defence), (attack, defence))
