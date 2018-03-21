from unittest import TestCase
from charactor import Charactor, BaseAbilityCalculation, AdditionalAbilityCalculation

class TestBaseAbilityCalculation(TestCase):
    def setUp(self):
        self.charactor = Charactor("Male", "Wind", "Fighter", "Sword")
        self.base_ability_calculation = BaseAbilityCalculation()

    def test_attack(self):
        self.assertEqual(self.base_ability_calculation.attack(self.charactor), 40)

    def test_defence(self):
        self.assertEqual(self.base_ability_calculation.defence(self.charactor), 40)



class TestAdditionalAbilityCalculation(TestCase):
    def setUp(self):
        self.charactor = Charactor("Male", "Wind", "Fighter", "Sword")
        self.additional_ability_calculation = AdditionalAbilityCalculation()

    def test_attack(self):
        self.assertEqual(self.additional_ability_calculation.attack(self.charactor), 20)

    def test_defence(self):
        self.assertEqual(self.additional_ability_calculation.defence(self.charactor), 0)