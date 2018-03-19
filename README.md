# exam_swe

以下の仕様で、戦士、魔法使い、武道家の

- 攻撃力
- 防御力
- スキル

の3パラメータを取得できるようにする

パラメータは _性別、属性、装備_ で変化する

すべての組み合わせに対応できるクラス構成を実装する

キャラクター(Character):

    性別 -> 男の場合は攻撃力 +5, 女の場合は防御力 +5

属性(Element):

    風(Wind) -> 攻撃力 +5 防御力 +10(武道家の場合はさらに攻撃力+20)
    水(Water) -> 攻撃力 +10 防御力 +5(戦士の場合はさらに防御力+10)
    雷(Thunder) -> 攻撃力 +15 防御力 +0(魔法使いの場合はさらに防御力+5)

ジョブ(Job):

    戦士(Fighter) → スキル: 男の場合は「ギガスラッシュ」、女の場合は「ビッグバン」
    魔法使い(Magician) → スキル: 男の場合は「ベギラマ」、女の場合は「メラミ」
    武道家(Martial) → スキル: 男の場合は「ブースト」、女の場合は「カウンタ」

装備(Equipment):

    剣(Sword) 攻撃力 +30 防御力 +30(戦士の場合はさらに攻撃力+20)
    杖(Stick) 攻撃力 +30 防御力 +10(魔法使いの場合はさらに攻撃力+20)
    グローブ(Glove) 攻撃力 +20 防御力 +20(武道家の場合はさらに防御力+20)

## 属性パターン

| Sex    | Element | Job      | Equipment | Attack | Defence | Skill   |
|--------|---------|----------|-----------|--------|---------|---------|
| Male   | Wind    | Fighter  | Sword     | 60     | 40      | ギガスラッシュ |
| Male   | Wind    | Fighter  | Stick     | 40     | 20      | ギガスラッシュ |
| Male   | Wind    | Fighter  | Glove     | 30     | 30      | ギガスラッシュ |
| Male   | Wind    | Magician | Sword     | 40     | 40      | ベギラマ    |
| Male   | Wind    | Magician | Stick     | 60     | 20      | ベギラマ    |
| Male   | Wind    | Magician | Glove     | 30     | 30      | ベギラマ    |
| Male   | Wind    | Martial  | Sword     | 60     | 40      | ブースト    |
| Male   | Wind    | Martial  | Stick     | 60     | 40      | ブースト    |
| Male   | Wind    | Martial  | Glove     | 50     | 30      | ブースト    |
| Male   | Water   | Fighter  | Sword     | 65     | 45      | ギガスラッシュ |
| Male   | Water   | Fighter  | Stick     | 45     | 25      | ギガスラッシュ |
| Male   | Water   | Fighter  | Glove     | 35     | 35      | ギガスラッシュ |
| Male   | Water   | Magician | Sword     | 45     | 35      | ベギラマ    |
| Male   | Water   | Magician | Stick     | 65     | 15      | ベギラマ    |
| Male   | Water   | Magician | Glove     | 35     | 25      | ベギラマ    |
| Male   | Water   | Martial  | Sword     | 45     | 35      | ブースト    |
| Male   | Water   | Martial  | Stick     | 45     | 35      | ブースト    |
| Male   | Water   | Martial  | Glove     | 35     | 25      | ブースト    |
| Male   | Thunder | Fighter  | Sword     | 70     | 30      | ギガスラッシュ |
| Male   | Thunder | Fighter  | Stick     | 50     | 10      | ギガスラッシュ |
| Male   | Thunder | Fighter  | Glove     | 40     | 20      | ギガスラッシュ |
| Male   | Thunder | Magician | Sword     | 50     | 35      | ベギラマ    |
| Male   | Thunder | Magician | Stick     | 70     | 15      | ベギラマ    |
| Male   | Thunder | Magician | Glove     | 40     | 25      | ベギラマ    |
| Male   | Thunder | Martial  | Sword     | 50     | 30      | ブースト    |
| Male   | Thunder | Martial  | Stick     | 50     | 30      | ブースト    |
| Male   | Thunder | Martial  | Glove     | 40     | 20      | ブースト    |
| Female | Wind    | Fighter  | Sword     | 55     | 45      | ビッグバン   |
| Female | Wind    | Fighter  | Stick     | 35     | 25      | ビッグバン   |
| Female | Wind    | Fighter  | Glove     | 25     | 35      | ビッグバン   |
| Female | Wind    | Magician | Sword     | 35     | 45      | メラミ     |
| Female | Wind    | Magician | Stick     | 55     | 25      | メラミ     |
| Female | Wind    | Magician | Glove     | 25     | 35      | メラミ     |
| Female | Wind    | Martial  | Sword     | 55     | 45      | カウンタ    |
| Female | Wind    | Martial  | Stick     | 55     | 45      | カウンタ    |
| Female | Wind    | Martial  | Glove     | 45     | 35      | カウンタ    |
| Female | Water   | Fighter  | Sword     | 60     | 50      | ビッグバン   |
| Female | Water   | Fighter  | Stick     | 40     | 30      | ビッグバン   |
| Female | Water   | Fighter  | Glove     | 30     | 40      | ビッグバン   |
| Female | Water   | Magician | Sword     | 40     | 40      | メラミ     |
| Female | Water   | Magician | Stick     | 60     | 20      | メラミ     |
| Female | Water   | Magician | Glove     | 30     | 30      | メラミ     |
| Female | Water   | Martial  | Sword     | 40     | 40      | カウンタ    |
| Female | Water   | Martial  | Stick     | 40     | 40      | カウンタ    |
| Female | Water   | Martial  | Glove     | 30     | 30      | カウンタ    |
| Female | Thunder | Fighter  | Sword     | 65     | 35      | ビッグバン   |
| Female | Thunder | Fighter  | Stick     | 45     | 15      | ビッグバン   |
| Female | Thunder | Fighter  | Glove     | 35     | 25      | ビッグバン   |
| Female | Thunder | Magician | Sword     | 45     | 40      | メラミ     |
| Female | Thunder | Magician | Stick     | 65     | 20      | メラミ     |
| Female | Thunder | Magician | Glove     | 35     | 30      | メラミ     |
| Female | Thunder | Martial  | Sword     | 45     | 35      | カウンタ    |
| Female | Thunder | Martial  | Stick     | 45     | 35      | カウンタ    |
| Female | Thunder | Martial  | Glove     | 35     | 25      | カウンタ    |
