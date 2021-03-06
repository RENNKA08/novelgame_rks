label may_week_second:
    scene bg dark

    nal "5月 第2週"

    "俺は駅前でフォレストハウスが来るのを待っていた。"
    "薄暗い道には浴衣を来た男女が歩いていた。"
    "俺はそれを見て、フォレストハウスのことを考えた。快活な声、嬉しげな表情。道行く人のどんな美点より、フォレストハウスのほうがより優れている。"
    "そんな気がした。他人を見て思い出す。近くで話している人よりあいつの方が、いま階段を降りてきた人よりあいつの方が。"
    "そんなサイクルがぐるぐると頭の中で回っていた。"
    "回らなくても良いの──いや……　俺はフォレストハウスのことを考えたくない、なんて思ってはいない。"
    "俺はあいつと、互いに承認しあうことを承認しあっている関係を築きたい、なんて哲学的な引用をするつもりもない。"
    "俺は──"
    if point >= 30:
        "そのあと、すぐにフォレストハウスは来た。俺たちは雑踏の中を進んでいった。"
        "薄闇の中で色とりどりの浴衣が、街灯の粉っぽい黄色い光に照らされていた。歩く間フォレストハウスはこんな話をしていた。"

        show im forest at Cdown

        hi_f "あんた、自分が老いて、死ぬときのことを考えたことある？"
        hi_f "頭も体も鈍くなって、何もかも忘れて死んでしまうの。悲しむべきこと、悔やむべきことをすら忘れて。"
        hi_f "最も貴重であるものを大切にすることで、貴重じゃなくなっちゃう。非論理で不条理。それが人生なのかしら。"
        "そのまま俺たちは歩き続け、広場へと出た。そこはさっきまでのうるささが嘘のように、静寂に包まれていた。"
        "人っ子一人いなかった。"
        "深い山中に二人だけで遭難したかのように世界はちっぽけなものになっていた。"
        "薄闇の中、ベンチに俺たちは腰を下ろした。すると、同時に花火が上がり始めた。"
        "花火は夜空に広がり、己の美しさを一瞬間最大限誇示し、散っていく。"
        "と同時にフォレストハウスの顔が白く光り、頭髪に浮かぶようにあのときのかんざしが輝き、顔へと浮かぶ表情が見て取れた。"
        "そのとき、俺は自分のすべきことを理解した。そして、そこに一切の逡巡はなかった。"

        jump trueEnding

    else:
        jump badEnding

    return