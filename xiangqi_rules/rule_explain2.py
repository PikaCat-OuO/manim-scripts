from manim import *
from manim_voiceover import VoiceoverScene

sys.path.append("..")
from EdgeService import EdgeService


class RuleExplain2(VoiceoverScene):
    def construct(self):
        self.set_speech_service(EdgeService(transcription_model='base'))

        with self.voiceover(
                '大家好，好久不见，欢迎回到喵喵的棋规小课堂，今天我们依然来分析一个棋规案例。'):
            title = Text("棋规判决案例分析", font="Microsoft YaHei", color=BLUE).to_corner(UL)

            # load pikacat avatar
            pikacat_avatar = ImageMobject("images/pikacat.jpg").scale(0.2)
            # pikacat name
            pikacat_name = Text("PikaCat皮卡喵", font="Microsoft YaHei", color=WHITE).next_to(pikacat_avatar, DOWN)
            # show pikacat info and show title
            self.play(DrawBorderThenFill(title), FadeIn(pikacat_avatar), Write(pikacat_name))
        # hide pikacat info
        self.play(FadeOut(pikacat_avatar), FadeOut(pikacat_name), FadeOut(title))

        xiangqi_board_upper = VGroup(*[Rectangle(width=1, height=1) for _ in range(32)])
        xiangqi_board_upper.arrange_in_grid(rows=4, buff=0)
        xiangqi_board_upper.add(Line(xiangqi_board_upper[3].get_corner(UL), xiangqi_board_upper[12].get_corner(DR)),
                                Line(xiangqi_board_upper[4].get_corner(UR), xiangqi_board_upper[11].get_corner(DL)))

        xiangqi_board_downer = VGroup(*[Rectangle(width=1, height=1) for _ in range(32)])
        xiangqi_board_downer.arrange_in_grid(rows=4, buff=0)
        xiangqi_board_downer.add(Line(xiangqi_board_downer[19].get_corner(UL), xiangqi_board_downer[28].get_corner(DR)),
                                 Line(xiangqi_board_downer[20].get_corner(UR), xiangqi_board_downer[27].get_corner(DL)))
        xiangqi_board = VGroup(xiangqi_board_upper, Rectangle(width=8, height=1), xiangqi_board_downer) \
            .arrange(DOWN, buff=0).scale(0.7)

        def add_piece(side, piece, grid, loc):
            color = GRAY if side == '黑' else RED
            position = xiangqi_board_upper[grid] if grid < 32 else xiangqi_board_downer[grid - 32]
            position = position.get_corner(loc)
            border = Circle(color=color, fill_color=WHITE, fill_opacity=.9, radius=.3).move_to(position)
            text = MarkupText(f'<span foreground="{color}"><b>{piece}</b></span>', font="Microsoft YaHei",
                              font_size=30).move_to(border.get_center())
            return VGroup(border, text)

        # 绘制车
        red_rook1 = add_piece('红', '车', 17, DR)
        red_rook2 = add_piece('红', '车', 28, DR)
        black_rook1 = add_piece('黑', '车', 0, UR)
        black_rook2 = add_piece('黑', '车', 5, DR)

        # 绘制士
        red_advisor1 = add_piece('红', '士', 59, UR)
        red_advisor2 = add_piece('红', '士', 59, DL)
        black_advisor1 = add_piece('黑', '士', 4, UR)
        black_advisor2 = add_piece('黑', '士', 4, DL)

        # 绘制炮
        red_cannon1 = add_piece('红', '炮', 18, UR)
        red_cannon2 = add_piece('红', '炮', 18, DR)
        black_cannon1 = add_piece('黑', '炮', 19, UR)
        black_cannon2 = add_piece('黑', '炮', 35, UR)

        # 绘制兵
        red_pawn1 = add_piece('红', '兵', 32, DL)
        red_pawn2 = add_piece('红', '兵', 39, DR)
        black_pawn1 = add_piece('黑', '卒', 16, DL)
        black_pawn2 = add_piece('黑', '卒', 23, DR)
        black_pawn3 = add_piece('黑', '卒', 34, UR)

        # 绘制马
        black_knight = add_piece('黑', '马', 0, DL)

        # 绘制象
        red_bishop1 = add_piece('红', '相', 43, DR)
        red_bishop2 = add_piece('红', '相', 57, DR)
        black_bishop1 = add_piece('黑', '象', 1, UR)
        black_bishop2 = add_piece('黑', '象', 5, UR)

        # 绘制将帅
        red_king = add_piece('红', '帅', 60, DR)
        black_king = add_piece('黑', '将', 3, UR)

        with self.voiceover('这是一个象棋局面，<bookmark mark="A"/>红黑双方在此局面下按照这样的走子序列进行走子。'):
            # 启动绘制动画
            self.play(Write(xiangqi_board), Write(red_rook1), Write(red_rook2), Write(black_rook1), Write(black_rook2),
                      Write(red_advisor1), Write(red_advisor2), Write(black_advisor1), Write(black_advisor2),
                      Write(red_cannon1), Write(red_cannon2), Write(black_cannon1), Write(black_cannon2),
                      Write(red_pawn1), Write(red_pawn2), Write(black_pawn1), Write(black_pawn2), Write(black_pawn3),
                      Write(black_knight), Write(red_bishop1), Write(red_bishop2), Write(black_bishop1),
                      Write(black_bishop2), Write(red_king), Write(black_king))

            self.wait_until_bookmark('A')
            for _ in range(2):
                # 红后炮平五
                self.play(red_cannon2.animate.shift(RIGHT * 0.7))

                # 黑将左平一
                self.play(black_king.animate.shift(LEFT * 0.7))

                # 红炮五平六
                self.play(red_cannon2.animate.shift(LEFT * 0.7))

                # 黑将右平一
                self.play(black_king.animate.shift(RIGHT * 0.7))

            self.wait(1)

        with self.voiceover(
                '我们可以看到，第一个局面在走子序列中一共重复出现了3次，形成了3次循环重复，该局面成为待判局面。'):
            pass

        with self.voiceover('我们首先判断红方是否违规。'):
            pass

        with self.voiceover(
                '红方的第一步，<bookmark mark="A"/>后炮平五。由于这一步不是将军，因此不符合长将需要每一步均为将军的定义，所以红方不是长江。'):
            self.wait_until_bookmark('A')
            # 红右士退中
            self.play(red_cannon2.animate.shift(RIGHT * 0.7))

        with self.voiceover('我们后续只需要关注红方是否存在长捉即可，我们看此时红方捉黑方哪些子。'):
            pass

        with self.voiceover(
                '红方的七路车不对黑方的边卒形成捉，该卒尚未过河，<bookmark mark="A"/>也不捉黑方的底象，因为吃掉黑方底象会被黑车或黑马反吃。'):
            arrow = Arrow(red_rook1.get_center(), black_pawn1.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(black_pawn1, Circle, fade_out=True, run_time=1))
            cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
            cross.move_to(arrow.get_center())
            self.play(Write(cross))
            self.play(FadeOut(arrow), FadeOut(cross))

            self.wait_until_bookmark('A')
            arrow = Arrow(red_rook1.get_center(), black_bishop1.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(black_bishop1, Circle, fade_out=True, run_time=1))

            arrow2 = Arrow(black_rook1.get_center(), black_bishop1.get_center(), buff=0.1, color=BLUE)
            arrow3 = Arrow(black_knight.get_center(), black_bishop1.get_center(), buff=0.1, color=BLUE)
            self.play(GrowArrow(arrow2), GrowArrow(arrow3))

            cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
            cross.move_to(arrow.get_center())
            self.play(Write(cross))
            self.play(FadeOut(arrow), FadeOut(cross))
            self.play(arrow2.animate.set_color(GREEN), arrow3.animate.set_color(GREEN))
            self.wait(1)
            self.play(FadeOut(arrow2), FadeOut(arrow3))

        with self.voiceover('红方的五路炮不对黑方的中士形成捉，因为吃掉黑方中士后可以被黑方多个子反吃。'):
            arrow = Arrow(red_cannon2.get_center(), black_advisor2.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(black_advisor2, Circle, fade_out=True, run_time=1))

            arc = ArcBetweenPoints(start=black_cannon2.get_center(), end=black_advisor2.get_center(), angle=-PI / 2,
                                   color=BLUE)
            arrow2 = Arrow(black_advisor1.get_center(), black_advisor2.get_center(), buff=0.1, color=BLUE)
            arrow3 = Arrow(black_rook2.get_center(), black_advisor2.get_center(), buff=0.1, color=BLUE)
            arrow4 = Arrow(black_king.get_center(), black_advisor2.get_center(), buff=0.1, color=BLUE)
            self.play(Create(arc), GrowArrow(arrow2), GrowArrow(arrow3), GrowArrow(arrow4))

            cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
            cross.move_to(arrow.get_center())
            self.play(Write(cross))
            self.play(FadeOut(arrow), FadeOut(cross))
            self.play(arc.animate.set_color(GREEN), arrow2.animate.set_color(GREEN), arrow3.animate.set_color(GREEN),
                      arrow4.animate.set_color(GREEN))
            self.wait(1)
            self.play(FadeOut(arc), FadeOut(arrow2), FadeOut(arrow3), FadeOut(arrow4))

        with self.voiceover(
                '红方的四路车此时对黑方的底士是否形成捉呢？<bookmark mark="A"/>给红方走一步的机会，<bookmark mark="B"/>吃掉这个子。<bookmark mark="C"/>'
                '黑方中士被红方中路炮牵制，无法反吃红车。<bookmark mark="D"/>红方借帅助攻，黑将也无法反吃红车。'):
            arrow = Arrow(red_rook2.get_center(), black_advisor1.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(black_advisor1, Circle, fade_out=True, run_time=1))
            self.wait_until_bookmark('A')

            self.wait_until_bookmark('B')
            self.play(red_rook2.animate.shift(UP * 0.7 * 4), FadeOut(arrow), FadeOut(black_advisor1))
            self.wait_until_bookmark('C')

            arc = ArcBetweenPoints(start=red_cannon2.get_center(), end=black_king.get_center(), angle=-PI / 2,
                                   color=RED)
            self.play(Create(arc))
            self.play(Circumscribe(black_advisor2, Circle, fade_out=True, run_time=1))
            arrow = Arrow(black_advisor2.get_center(), red_rook2.get_center(), buff=0.1, color=BLUE)
            self.play(GrowArrow(arrow))
            cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
            cross.move_to(arrow.get_center())
            self.play(Write(cross))
            self.play(FadeOut(arrow), FadeOut(cross))
            self.play(arc.animate.set_color(GREEN))
            self.wait_until_bookmark('D')

            arrow = Arrow(red_king.get_center(), red_rook2.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            arrow2 = Arrow(black_king.get_center(), red_rook2.get_center(), buff=0.1, color=BLUE)
            self.play(GrowArrow(arrow2))
            cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
            cross.move_to(arrow2.get_center())
            self.play(Write(cross))
            self.play(FadeOut(arrow2), FadeOut(cross))
            self.play(arrow.animate.set_color(GREEN))
            self.wait(1)
            self.play(FadeOut(arrow))

            self.play(red_rook2.animate.shift(DOWN * 0.7 * 4), FadeIn(black_advisor1))

        with self.voiceover('黑方无子可反吃红车，因此红车捉黑底士成立。'):
            arrow = Arrow(red_rook2.get_center(), black_advisor1.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(black_advisor1, Circle, fade_out=True, run_time=1))
            self.play(arrow.animate.set_color(GREEN))

        with self.voiceover('黑方出将，此时，红方中炮对黑中士的牵制失效，<bookmark mark="A"/>如果此时红车再吃底士，那么黑中士可以反吃，因此红车此时不对黑底士形成捉。'
                            '黑方的底士此时不被任何红方子捉，黑方出将这步使黑底士逃捉。'):
            self.play(black_king.animate.shift(LEFT * 0.7))
            cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
            cross.move_to(arc.get_center())
            self.play(Write(cross))
            self.play(FadeOut(arc), FadeOut(cross))
            self.wait_until_bookmark('A')

            self.play(arrow.animate.set_color(RED))
            self.play(Circumscribe(black_advisor1, Circle, fade_out=True, run_time=1))

            arrow2 = Arrow(black_advisor2.get_center(), black_advisor1.get_center(), buff=0.1, color=BLUE)
            self.play(GrowArrow(arrow2))
            self.play(Circumscribe(black_advisor1, Circle, fade_out=True, run_time=1))
            cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
            cross.move_to(arrow.get_center())
            self.play(Write(cross))
            self.play(FadeOut(arrow), FadeOut(cross))
            self.play(arrow2.animate.set_color(GREEN))
        self.play(FadeOut(arrow2))

        with self.voiceover('红炮平炮将军，根据捉的定义，将不捉，捉不将，红方这一步是将军，因此走完之后不捉黑方任何子。'
                            '由于红方存在一步不捉黑方任何子，不符合长捉需要每一步均捉同一子的定义，因此红方不是长捉。'):
            self.play(red_cannon2.animate.shift(LEFT * 0.7))
            arrow = Arrow(red_cannon2.get_center(), black_king.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(black_king, Circle, fade_out=True, run_time=1))
            self.play(arrow.animate.set_color(GREEN))
        self.play(FadeOut(arrow))

        with self.voiceover('红方既不长江也不长捉，因此红方为 允许循环。我们对红方的分析就此结束。'):
            pass

        with self.voiceover('我们接着分析黑方，<bookmark mark="A"/>黑方中士在红走出第一步之前捉着红前炮'):
            self.play(black_king.animate.shift(RIGHT * 0.7))
            self.wait_until_bookmark('A')

            arrow = Arrow(black_advisor2.get_center(), red_cannon1.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(red_cannon1, Circle, fade_out=True, run_time=1))

            self.play(arrow.animate.set_color(GREEN))

        with self.voiceover("红后炮平中，对黑中士形成牵制，使其无法捉六路炮，红这步使六路炮逃捉。"):
            self.play(red_cannon2.animate.shift(RIGHT * 0.7))

            arc = ArcBetweenPoints(start=red_cannon2.get_center(), end=black_king.get_center(), angle=PI / 2,
                                   color=BLUE)
            self.play(Create(arc))
            self.play(Circumscribe(black_advisor2, Circle, fade_out=True, run_time=1))
            cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
            cross.move_to(arrow.get_center())
            self.play(Write(cross))
            self.play(FadeOut(arrow), FadeOut(cross))
            self.play(arc.animate.set_color(GREEN))

        with self.voiceover(
                '黑方出将，使黑中士逃脱牵制。使中士继续捉红六路炮。由于黑方出将的这一步不对红方形成将军，因此不符合长将需要每一步均为将军的定义，所以黑方不是长江。'):
            self.play(black_king.animate.shift(LEFT * 0.7))

            cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
            cross.move_to(arc.get_center())
            self.play(Write(cross))
            self.play(FadeOut(arc), FadeOut(cross))

            arrow = Arrow(black_advisor2.get_center(), red_cannon1.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(red_cannon1, Circle, fade_out=True, run_time=1))
            self.play(arrow.animate.set_color(GREEN))

        with self.voiceover(
                '红方中炮平六，将军黑方。黑中士吃红前炮此时成为非法走法，黑方无法在不应江的情况下吃红前炮，因此黑中士对红前炮无法形成捉，红方平炮将军这一步使红前炮逃捉。'):
            self.play(red_cannon2.animate.shift(LEFT * 0.7))

            arrow2 = Arrow(red_cannon2.get_center(), black_king.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow2))
            self.play(Circumscribe(black_king, Circle, fade_out=True, run_time=1))

            self.play(Circumscribe(red_cannon1, Circle, fade_out=True, run_time=1))
            cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
            cross.move_to(arrow.get_center())

            self.play(Write(cross))
            self.play(FadeOut(arrow), FadeOut(cross))
            self.play(arrow2.animate.set_color(GREEN))

        with self.voiceover(
                '黑方入将应江，黑中士吃红前炮此时重新成为合法走法，因此黑在入将后再次对红前炮形成捉。'):
            self.play(black_king.animate.shift(RIGHT * 0.7))

            cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
            cross.move_to(arrow2.get_center())

            self.play(Write(cross))
            self.play(FadeOut(arrow2), FadeOut(cross))

            arrow = Arrow(black_advisor2.get_center(), red_cannon1.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(red_cannon1, Circle, fade_out=True, run_time=1))
            self.play(arrow.animate.set_color(GREEN))

        with self.voiceover('我们已经分析完成了前两次循环重复，后面第三次循环和前面的两次循环过程类似，不再赘述。'):
            pass

        with self.voiceover(
                '根据程序竞赛棋规，黑方没有长江，但是黑方在整个循环序列中步步均捉红前炮，红步步均逃捉红前炮，因此黑方长捉红前炮成立。'):
            pass

        with self.voiceover('由于红方是允许循环，因此黑方 长捉判负。'):
            pass

        with self.voiceover('好啦，今天就分享到这里吧，感谢大家的观看，记得一键三连哦。下次见，拜拜~'):
            self.play(*[FadeOut(obj) for obj in self.mobjects])
            title = Text("参考文献", font="Microsoft YaHei", color=BLUE).to_corner(UL)

            # load rule reference
            rule_img = ImageMobject("images/rule.jpg").scale(.7)
            rule_link = Text("https://pikafish.org/中国象棋程序竞赛规则.pdf", font="Microsoft YaHei", font_size=28,
                             color=WHITE).next_to(rule_img, DOWN)
            # show rule info and show title
            self.play(DrawBorderThenFill(title), FadeIn(rule_img), Write(rule_link))
