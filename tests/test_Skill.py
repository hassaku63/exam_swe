from unittest import TestCase
from main import Charactor, Skill

class TestSkill(TestCase):
    def setUp(self):
        self.charactor = Charactor("Male", "Wind", "Fighter", "Sword")

    def test_skill(self):
        skill = Skill.get_skill(self.charactor)
        self.assertEqual(skill.name, "ギガスラッシュ")