label name:
    scene bg onn
    define pov = Character("[povname]")

python:
    povname = renpy.input("あなたの名前は?")
    povname = povname.strip()

"[povname]でよろしいですか？"
menu:
    "はい":
        "[povname]でゲームを開始します"
        jump prologue
    "いいえ":
        jump name
