init python:
    import ourModule # 何かショートカットコードを作るならここへ

# 標準位置設定
transform C:
    xalign 0.5
    yalign 1.0

transform Cdown:
    xalign 0.5
    yalign 0.5

transform Cbig:
    xalign 0.5
    yalign -1

# 登場人物
## ナレーション
define nal = Character("天の声", color="#ffffff")
## 名前未登場キャラ
define unknown = Character("???", color="#ffffff")
## 主人公
define you = Character("あなた", color="#ffffff")
## ヒロイン
### フォレスト
define hi_f = Character("フォレスト", color="#ffffff")
### コラーニング１
define hi_c1 = Character("コラーニング１", color="#ffffff")
### コラーニング２
define hi_c2 = Character("コラーニング２", color="#ffffff")
### メディアライブラリー
define hi_m = Character("メディアライブラリー", color="#ffffff")

# 立ち絵準備
# unknow
# image im unknow = im.FactorScale("images/characters//", width=1.0)
# you
# image im you = im.FactorScale("images/characters//", width=1.0)
# フォレスト
image im forest = im.FactorScale("images/characters/gibara/gibara.png", width=0.55)
image im2 forest = im.FactorScale("images/characters/gibara/mameshiba.png", width=0.55)

# 変数
default point = 0

label start:

    scene bg onn

    nal "あなたはこの物語で誰と恋をする？"

    with dissolve

    jump name

    return

