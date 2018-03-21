class Charactor(object):
    def __init__(self, sex, element, job, equipment):
        self.Sex = sex
        self.Element = element
        self.Job = job
        self.Equipment = equipment

        self._skill = Skill.get_skill(self)
        self.base_ability_calculation = BaseAbilityCalculation()
        self.additional_ability_calculation = AdditionalAbilityCalculation()

    @property
    def attack(self):
        _atk_base       = self.base_ability_calculation.attack(self)
        _atk_additional = self.additional_ability_calculation.attack(self)
        return _atk_base + _atk_additional

    @property
    def defence(self):
        _def_base       = self.base_ability_calculation.defence(self)
        _def_additional = self.additional_ability_calculation.defence(self)
        return _def_base + _def_additional

    @property
    def skill(self):
        return self._skill

class BaseAbilityStrategy(object):
    def attack(cls, charactor):
        raise NotImplementedError(cls.__class__.__name__)

    def defence(cls, charactor):
        raise NotImplementedError(cls.__class__.__name__)


class BaseAbilityCalculation(BaseAbilityStrategy):
    """
    キャラクター(Character):

    性別 -> 男の場合は攻撃力 +5, 女の場合は防御力 +5

    属性(Element)
    - 風(Wind) -> 攻撃力 +5 防御力 +10
    - 水(Water) -> 攻撃力 +10 防御力 +5
    - 雷(Thunder) -> 攻撃力 +15 防御力 +0

    ジョブ(Job)
    - 戦士(Fighter) → スキル: 男の場合は「ギガスラッシュ」、女の場合は「ビッグバン」
    - 魔法使い(Magician) → スキル: 男の場合は「ベギラマ」、女の場合は「メラミ」
    - 武道家(Martial) → スキル: 男の場合は「ブースト」、女の場合は「カウンタ」

    装備(Equipment)
    - 剣(Sword) 攻撃力 +30 防御力 +30
    - 杖(Stick) 攻撃力 +30 防御力 +10
    - グローブ(Glove) 攻撃力 +20 防御力 +20
    """

    def attack(self, charactor):
        attack = 0

        if charactor.Sex == "Male":
            attack += 5

        elif charactor.Sex == "Female":
            attack += 0

        if charactor.Element == "Wind":
            attack += 5

        elif charactor.Element == "Water":
            attack += 10

        elif charactor.Element == "Thunder":
            attack += 15

        if charactor.Equipment == "Sword":
            attack += 30

        elif charactor.Equipment == "Stick":
            attack += 30

        elif charactor.Equipment == "Glove":
            attack += 20

        return attack

    def defence(self, charactor):
        defence = 0

        if charactor.Sex == "Male":
            defence += 0

        elif charactor.Sex == "Female":
            defence += 5

        if charactor.Element == "Wind":
            defence += 10

        elif charactor.Element == "Water":
            defence += 5

        elif charactor.Element == "Thunder":
            defence += 0

        if charactor.Equipment == "Sword":
            defence += 30

        elif charactor.Equipment == "Stick":
            defence += 10

        elif charactor.Equipment == "Glove":
            defence += 20

        return defence

class AdditionalAbilityCalculation(BaseAbilityStrategy):
    """
    パラメータの値によって追加で付加される能力値（攻撃力／防御力／スキル）の計算ロジック
    """

    def attack(self, charactor):
        """
        風(Wind) -> 攻撃力 +5 防御力 +10(武道家の場合はさらに攻撃力+20)

        剣(Sword) 攻撃力 +30 防御力 +30(戦士の場合はさらに攻撃力+20)
        杖(Stick) 攻撃力 +30 防御力 +10(魔法使いの場合はさらに攻撃力+20)
        """
        attack = 0
        if charactor.Element == "Wind" and charactor.Job == "Martial":
            attack += 20

        if charactor.Equipment == "Sword" and charactor.Job == "Fighter":
            attack += 20

        if charactor.Equipment == "Stick" and charactor.Job == "Magician":
            attack += 20

        return attack

    def defence(self, charactor):
        """
        水(Water) -> 攻撃力 +10 防御力 +5(戦士の場合はさらに防御力+10)
        雷(Thunder) -> 攻撃力 +15 防御力 +0(魔法使いの場合はさらに防御力+5)

        グローブ(Glove) 攻撃力 +20 防御力 +20(武道家の場合はさらに防御力+20)
        """
        defence = 0

        if charactor.Element == "Water" and charactor.Job == "Fighter":
            defence += 10

        if charactor.Element == "Thunder" and charactor.Job == "Magician":
            defence += 5

        if charactor.Equipment == "Stick" and charactor.Job == "Martial":
            defence += 20

        return defence


class Skill(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @classmethod
    def get_skill(cls, charactor):
        """
        戦士(Fighter) → スキル: 男の場合は「ギガスラッシュ」、女の場合は「ビッグバン」
        魔法使い(Magician) → スキル: 男の場合は「ベギラマ」、女の場合は「メラミ」
        武道家(Martial) → スキル: 男の場合は「ブースト」、女の場合は「カウンタ」
        """
        skill_name = ""
        if charactor.Sex == "Male":
            if charactor.Job == "Fighter":
                skill_name = "ギガスラッシュ"
            elif charactor.Job == "Magician":
                skill_name = "ベギラマ"
            elif charactor.Job == "Martial":
                skill_name = "ブースト"
            else:
                pass
        elif charactor.Sex == "Female":
            if charactor.Job == "Fighter":
                skill_name = "ビッグバン"
            elif charactor.Job == "Magician":
                skill_name = "メラミ"
            elif charactor.Job == "Martial":
                skill_name = "カウンタ"
            else:
                pass

        else:
            pass

        def __str__(self):
            return self.name

        return Skill(skill_name)


if __name__ == "__main__":
    pass