from manim import *
from manim_voiceover import VoiceoverScene

sys.path.append("..")
from EdgeService import EdgeService


class QA1(VoiceoverScene):
    def construct(self):
        self.set_speech_service(EdgeService())

        title = Text("Q&A", font="Microsoft YaHei", color=BLUE).to_corner(UL)
        self.play(DrawBorderThenFill(title))

        with self.voiceover('大家好，我是喵喵，这次来回答一些问题吧。'):
            pass

        text = Text('问题1：皮卡鱼开发的目标是什么？', font="Microsoft YaHei")
        self.play(Write(text))
        with self.voiceover('皮卡鱼的开发目标是跟上时代的发展，和鳕鱼的技术栈保持紧密的联系。'):
            pass

        self.play(Transform(text, Text('问题2：棋软还有多大的进步空间？', font="Microsoft YaHei")))
        with self.voiceover('这个不好说，前NNUE时代人们也会认为传统评估也就是天花板了，但是根据策梅洛定理，肯定是存在一个天花板的。'):
            pass
        with self.voiceover('策梅洛定理认为，在二人的有限对弈游戏中，如果双方皆拥有完全的资讯，并且运气因素并不牵涉在游戏中，'
                            '那先行或后行者当中必有一方有必胜或者必不败的策略。'):
            pass
        with self.voiceover('显然，中国象棋软件的终点就是32子库，32子库就是一个存储了所有可能象棋局面的库，也就是对中国象棋这个游戏的破解，'
                            '但可惜的是这个库太大，无论从计算资源、计算时间还是从存储角度而言都无法接受。'):
            pass
        with self.voiceover('现在所有象棋软件都是对32子库的有损压缩，谁的损失率低，谁就走的更好，象棋软件的进步也就是进一步提升压缩的精度，'
                            '但因为32子库的大小是固定的，所以象棋软件的进步空间也必然是有上限的'):
            pass
        with self.voiceover('就中国象棋而言，我认为大概率，先行和后行都没法必胜，发展到最后和棋就是终极奥义'):
            pass

        self.play(Transform(text, Text('问题3：能不能讲讲中国规则和天天规则？', font="Microsoft YaHei")))
        with self.voiceover('不懂，棋规找afkbad'):
            pass

        self.play(Transform(text, Text('问题4：我平时用什么界面？', font="Microsoft YaHei")))
        with self.voiceover('鲨鱼象棋免费版，不下棋，单纯调试软件'):
            pass

        self.play(Transform(text, Text('问题5：下个版本鱼什么时候更新？', font="Microsoft YaHei")))
        with self.voiceover('等什么时候px0谱起作用的时候就更新'):
            pass

        self.play(Transform(text, Text('问题6：如何获取女大学生自用版赛科龙？', font="Microsoft YaHei")))
        with self.voiceover('不能提供获取途径，但是可以给提示：AES加密，鳕鱼随机数生成器PRNG，'
                            '你说什么，我用什么激活码激活旋风？呐，123456789 ## 123456789123'):
            pass

        self.play(Transform(text, Text('问题7：鱼发布的时候能带更多指令集的版本吗？', font="Microsoft YaHei")))
        with self.voiceover('下一次发版会增加avxvnni指令集（256位宽的vnni支持）'):
            pass

        self.play(Transform(text, Text('问题8：有无在开发的中象界面？', font="Microsoft YaHei")))
        with self.voiceover('无'):
            pass

        self.play(Transform(text, Text('问题9：皮卡鱼或者说鳕鱼能否提供对vnni256的支持？', font="Microsoft YaHei",
                                       font_size=30)))
        with self.voiceover('其实，在鳕鱼的指令集体系里面vnni512和vnni256所需的运行条件是一样的，'
                            'vnni256也就是说处理器本身支持512位宽的vnni，但是只使用其中的一半做计算，'
                            '真正的256位宽指的是avxvnni这个指令集，但是实测会比bmi2慢一些'):
            pass

        self.play(Transform(text, Text('问题10：我是女大学生吗？', font="Microsoft YaHei")))
        with self.voiceover('喵喵这么可爱，你听我的声音，觉得我是女大学生吗？假作真时真亦假，无为有时有还无。'):
            pass
