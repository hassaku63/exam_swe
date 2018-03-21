class Charactor(object):
    def __init__(self, sex, element, job, equipment):
        self.sex = sex
        self._element = element
        self._job = job
        self._equipment = equipment
        self.attack = 0
        self.defence = 0

        self._skill = Skill.get_skill(self)
        self.base_ability_calculation = BaseAbilityCalculation()
        self.additional_ability_calculation = AdditionalAbilityCalculation()

        self.update_ability()

    @property
    def element(self):
        return self._element

    @element.setter
    def element(self, element):
        self._element = element
        self.update_ability()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        self._job = job
        self.update_ability()

    @property
    def equipment(self):
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        self._equipment = equipment
        self.update_ability()

    @property
    def skill(self):
        return self._skill

    def update_ability(self):
        """
        インスタンスの初期化時とプロパティの更新時に呼び出す
        """
        self.attack = \
            self.base_ability_calculation.attack(self)\
            + self.additional_ability_calculation.attack(self)

        self.defence = \
            self.base_ability_calculation.defence(self)\
            + self.additional_ability_calculation.defence(self)

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

        if charactor.sex == "Male":
            attack += 5

        elif charactor.sex == "Female":
            attack += 0

        if charactor.element == "Wind":
            attack += 5

        elif charactor.element == "Water":
            attack += 10

        elif charactor.element == "Thunder":
            attack += 15

        if charactor.equipment == "Sword":
            attack += 30

        elif charactor.equipment == "Stick":
            attack += 30

        elif charactor.equipment == "Glove":
            attack += 20

        return attack

    def defence(self, charactor):
        defence = 0

        if charactor.sex == "Male":
            defence += 0

        elif charactor.sex == "Female":
            defence += 5

        if charactor.element == "Wind":
            defence += 10

        elif charactor.element == "Water":
            defence += 5

        elif charactor.element == "Thunder":
            defence += 0

        if charactor.equipment == "Sword":
            defence += 30

        elif charactor.equipment == "Stick":
            defence += 10

        elif charactor.equipment == "Glove":
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
        if charactor.element == "Wind" and charactor.job == "Martial":
            attack += 20

        if charactor.equipment == "Sword" and charactor.job == "Fighter":
            attack += 20

        if charactor.equipment == "Stick" and charactor.job == "Magician":
            attack += 20

        return attack

    def defence(self, charactor):
        """
        水(Water) -> 攻撃力 +10 防御力 +5(戦士の場合はさらに防御力+10)
        雷(Thunder) -> 攻撃力 +15 防御力 +0(魔法使いの場合はさらに防御力+5)

        グローブ(Glove) 攻撃力 +20 防御力 +20(武道家の場合はさらに防御力+20)
        """
        defence = 0

        if charactor.element == "Water" and charactor.job == "Fighter":
            defence += 10

        if charactor.element == "Thunder" and charactor.job == "Magician":
            defence += 5

        if charactor.equipment == "Stick" and charactor.job == "Martial":
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
        if charactor.sex == "Male":
            if charactor.job == "Fighter":
                skill_name = "ギガスラッシュ"
            elif charactor.job == "Magician":
                skill_name = "ベギラマ"
            elif charactor.job == "Martial":
                skill_name = "ブースト"
            else:
                pass
        elif charactor.sex == "Female":
            if charactor.job == "Fighter":
                skill_name = "ビッグバン"
            elif charactor.job == "Magician":
                skill_name = "メラミ"
            elif charactor.job == "Martial":
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