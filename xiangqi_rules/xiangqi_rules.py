from manim import *

config.max_files_cached = -1


class XiangqiRules(Scene):
    # title
    title = MarkupText(f'<span foreground="{BLUE}">象棋引擎密界兵器系列 之 <i>亚洲棋规详解</i></span>',
                       font="Microsoft YaHei", font_size=30).to_corner(UL)

    def setup(self):
        # load pikacat avatar
        pikacat_avatar = ImageMobject("images/pikacat.jpg").scale(0.2)
        # pikacat name
        pikacat_name = Text("PikaCat皮卡喵", font="Microsoft YaHei", color=WHITE).next_to(pikacat_avatar, DOWN)
        # show pikacat info and show title
        self.play(Write(self.title), FadeIn(pikacat_avatar), Write(pikacat_name))
        self.wait(1)
        # hide pikacat info
        self.play(FadeOut(pikacat_avatar), FadeOut(pikacat_name), FadeOut(self.title))

    def tear_down(self):
        # load pikacat avatar
        pikacat_avatar = ImageMobject("images/pikacat.jpg").scale(0.2)
        # pikacat name
        pikacat_name = Text("PikaCat皮卡喵", font="Microsoft YaHei", color=WHITE).next_to(pikacat_avatar, DOWN)
        # show pikacat info and transform title into info
        self.play(Write(self.title), FadeIn(pikacat_avatar), Write(pikacat_name))
        self.wait(3)
        # hide pikacat info
        self.play(FadeOut(pikacat_avatar), FadeOut(pikacat_name), FadeOut(self.title))

    def construct(self):
        text = MarkupText(f'大家好(o゜▽゜)o，这次我们来讲讲中国象棋的<span foreground="{PURE_GREEN}">亚洲规则</span>\n\n'
                          '一方面可以让大家了解亚洲棋规\n\n'
                          '另一方面可以让大家了解皮卡鱼使用的规则究竟长什么样', font='Microsoft YaHei', font_size=30)
        self.play(Write(text))
        self.wait(3)

        self.play(Transform(text, MarkupText('亚洲棋规中对判决影响最重要的便是：\n\n'
                                             '1. 将  军\n2. 捉  子\n3. 逃  避\n4. 三 次 循 环 重 复\n'
                                             '5. 长  将\n6. 长  捉\n7. 六 十 回 合 不 吃 子 和 棋',
                                             font='Microsoft YaHei', font_size=34,
                                             gradient=(RED, YELLOW, BLUE, GREEN, PURPLE, ORANGE, PINK))))
        self.wait(5)
        self.play(FadeOut(text))

        ############################################################

        # 将军
        text = MarkupText('将军(Check)', font='Microsoft YaHei', font_size=50)
        desc = MarkupText('凡走子直接攻击对方 <b>将</b> 、 <b>帅</b> 者谓之将军', font='Microsoft YaHei',
                          font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(3)
        self.play(FadeOut(group))

        ############################################################

        # 直接将军
        text = MarkupText('直接将军(Direct Check)', font='Microsoft YaHei', font_size=50)
        self.play(GrowFromCenter(text))
        self.wait(1)
        self.play(FadeOut(text))

        # 在屏幕中央绘制一个象棋棋盘
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

        # 走法定义
        text_left = Text("车五平六", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("将军", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制将帅
        border = Circle(color=GRAY, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_upper[2].get_corner(UR))
        king_text = MarkupText(f'<span foreground="{GRAY}"><b>将</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        black_king = VGroup(border, king_text)
        border = Circle(color=RED, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_downer[28].get_corner(DR))
        king_text = MarkupText(f'<span foreground="{RED}"><b>帅</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        red_king = VGroup(border, king_text)

        # 绘制红车
        border = Circle(color=RED, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_downer[3].get_corner(DR))
        rook_text = MarkupText(f'<span foreground="{RED}"><b>车</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        red_rook = VGroup(border, rook_text)

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(red_rook), Write(text_left),
                  Write(text_right))

        # 平车将军
        arrow = Arrow(start=red_rook.get_center(), end=red_rook.get_center() + LEFT * 0.7, buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_rook.animate.shift(LEFT * 0.7), FadeOut(arrow), text_left.animate.set_color(BLUE))

        # 红车攻击将
        arrow = Arrow(start=red_rook.get_center(), end=black_king.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        self.play(arrow.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(red_rook), FadeOut(red_king), FadeOut(black_king), FadeOut(xiangqi_board),
                  FadeOut(text_left), FadeOut(text_right))

        ############################################################

        # 闪将
        text = MarkupText('闪将(Discovered Check)', font='Microsoft YaHei', font_size=50)
        self.play(GrowFromCenter(text))
        self.wait(1)
        self.play(FadeOut(text))

        # 走法定义
        text_left = Text("兵六平七", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("将军", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[26].get_corner(DR))

        # 绘制红兵
        border = Circle(color=RED, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_upper[26].get_corner(DR))
        pawn_text = MarkupText(f'<span foreground="{RED}"><b>兵</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        red_pawn = VGroup(border, pawn_text)

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(red_rook), Write(red_pawn),
                  Write(text_left), Write(text_right))

        # 红车攻击不到将
        arrow = Arrow(start=red_rook.get_center(), end=red_pawn.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        self.play(FadeOut(arrow))

        # 平兵将军
        arrow = Arrow(start=red_pawn.get_center(), end=red_pawn.get_center() + LEFT * 0.7,
                      buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_pawn.animate.shift(LEFT * 0.7), FadeOut(arrow), text_left.animate.set_color(BLUE))

        # 红车攻击将
        arrow = Arrow(start=red_rook.get_center(), end=black_king.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        self.play(arrow.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(red_rook), FadeOut(red_pawn), FadeOut(red_king), FadeOut(black_king),
                  FadeOut(xiangqi_board), FadeOut(text_left), FadeOut(text_right))

        ############################################################

        # 捉
        text = MarkupText('捉(Chase)', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(
            '凡走子攻击对方 <b>将</b> 、 <b>帅</b> 以外之任何一子，企图于下一着吃去之者，谓之捉\n\n'
            '但以下特殊情况除外：\n'
            '1. 将（帅）和兵（卒）产生的攻击\n'
            '2. 攻击未过河兵（卒）\n'
            '3. 吃掉被攻击子后可以被对方反吃（马或炮攻击车除外）\n'
            '4. 攻击同类子且被攻击子可反吃攻击子\n',
            font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(8)
        self.play(FadeOut(group))

        ############################################################

        # 直接捉
        text = MarkupText('直接捉(Direct Chase)', font='Microsoft YaHei', font_size=50)
        self.play(GrowFromCenter(text))
        self.wait(1)
        self.play(FadeOut(text))

        # 走法定义
        text_left = Text("车二平三", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉炮", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[14].get_corner(DR))

        # 绘制黑炮
        border = Circle(color=GRAY, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_upper[21].get_corner(DR))
        cannon_text = MarkupText(f'<span foreground="{GRAY}"><b>炮</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        black_cannon = VGroup(border, cannon_text)

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(red_rook), Write(black_cannon),
                  Write(text_left), Write(text_right))

        # 平车捉炮
        arrow = Arrow(start=red_rook.get_center(), end=red_rook.get_center() + LEFT * 0.7, buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_rook.animate.shift(LEFT * 0.7), FadeOut(arrow), text_left.animate.set_color(BLUE))

        # 红车攻击炮
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        self.play(arrow.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(red_rook), FadeOut(black_cannon), FadeOut(red_king), FadeOut(black_king),
                  FadeOut(xiangqi_board), FadeOut(text_left), FadeOut(text_right))

        ############################################################

        # 特殊情况不是捉
        text = MarkupText('特殊情况1', font='Microsoft YaHei', font_size=50)
        desc = MarkupText('将（帅）和兵（卒）产生的攻击', font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(3)
        self.play(FadeOut(group))

        # 走法定义
        text_left = Text("帅四进一", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉炮", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_downer[12].get_corner(DR))

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(black_cannon), Write(text_left),
                  Write(text_right))

        # 进帅攻击黑炮
        arrow = Arrow(start=red_king.get_center(), end=red_king.get_center() + UP * 0.7, buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_king.animate.shift(UP * 0.7), FadeOut(arrow), text_left.animate.set_color(BLUE))

        # 帅攻击黑炮
        arrow = Arrow(start=red_king.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
        cross.move_to(arrow.get_center())
        big_cross = Cross(stroke_color=PURE_GREEN).scale(0.5)
        big_cross.move_to(text_right.get_center())
        self.play(Write(cross), Write(big_cross))
        self.play(FadeOut(arrow), FadeOut(cross), FadeOut(big_cross), FadeOut(text_right))
        self.wait(1)

        self.play(FadeOut(red_king), FadeOut(black_cannon), FadeOut(black_king), FadeOut(text_left))

        text_left = Text("兵一平二", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉炮", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红帅
        red_king.move_to(xiangqi_board_downer[28].get_corner(DR))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_upper[29].get_corner(DR))

        # 绘制红兵
        red_pawn.move_to(xiangqi_board_upper[31].get_corner(DR))

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(black_cannon), Write(red_pawn), Write(text_left),
                  Write(text_right))

        # 平兵捉炮
        arrow = Arrow(start=red_pawn.get_center(), end=red_pawn.get_center() + LEFT * 0.7,
                      buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_pawn.animate.shift(LEFT * 0.7), FadeOut(arrow), text_left.animate.set_color(BLUE))

        # 红兵攻击炮
        arrow = Arrow(start=red_pawn.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        cross.move_to(arrow.get_center())
        big_cross.move_to(text_right.get_center())
        self.play(Write(cross), Write(big_cross))
        self.play(FadeOut(arrow), FadeOut(cross), FadeOut(big_cross), FadeOut(text_right))
        self.wait(1)

        self.play(FadeOut(red_king), FadeOut(black_king), FadeOut(black_cannon), FadeOut(red_pawn),
                  FadeOut(xiangqi_board), FadeOut(text_left))

        ############################################################

        # 特殊情况不是捉
        text = MarkupText('特殊情况2', font='Microsoft YaHei', font_size=50)
        desc = MarkupText('攻击未过河兵（卒）', font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(3)
        self.play(FadeOut(group))

        # 走法定义
        text_left = Text("车二平三", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉卒", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[6].get_corner(DR))

        # 绘制黑卒
        border = Circle(color=GRAY, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_upper[21].get_corner(DR))
        pawn_text = MarkupText(f'<span foreground="{GRAY}"><b>卒</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        black_pawn = VGroup(border, pawn_text)

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(red_rook), Write(black_pawn),
                  Write(text_left), Write(text_right))

        # 平车攻击黑卒
        arrow = Arrow(start=red_rook.get_center(), end=red_rook.get_center() + LEFT * 0.7, buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_rook.animate.shift(LEFT * 0.7), FadeOut(arrow), text_left.animate.set_color(BLUE))

        # 车攻击黑卒
        arrow = Arrow(start=red_rook.get_center(), end=black_pawn.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        cross.move_to(arrow.get_center())
        big_cross.move_to(text_right.get_center())
        self.play(Write(cross), Write(big_cross))
        self.play(FadeOut(arrow), FadeOut(cross), FadeOut(big_cross), FadeOut(text_right))
        self.wait(1)

        self.play(FadeOut(red_king), FadeOut(black_king), FadeOut(red_rook), FadeOut(black_pawn), FadeOut(text_left),
                  FadeOut(xiangqi_board))

        ############################################################

        text = MarkupText('特殊情况3', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(f'<span foreground="{RED}">吃掉被攻击子后可以被对方反吃</span>（马或炮攻击车除外）',
                          font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(3)
        self.play(FadeOut(group))

        # 走法定义
        text_left = Text("车二平三", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉炮", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制黑象
        border = Circle(color=GRAY, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_upper[11].get_corner(DR))
        bishop_text = MarkupText(f'<span foreground="{GRAY}"><b>象</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        black_bishop = VGroup(border, bishop_text)

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[14].get_corner(DR))

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(black_cannon), Write(black_bishop),
                  Write(red_rook), Write(text_left), Write(text_right))

        # 平车捉炮
        arrow = Arrow(start=red_rook.get_center(), end=red_rook.get_center() + LEFT * 0.7,
                      buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_rook.animate.shift(LEFT * 0.7), FadeOut(arrow), text_left.animate.set_color(BLUE))

        # 红车攻击炮
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 红车吃炮
        self.play(red_rook.animate.move_to(black_cannon.get_center()), FadeOut(arrow), FadeOut(black_cannon))

        # 黑象保护炮
        arrow = Arrow(start=black_bishop.get_center(), end=black_cannon.get_center(), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))

        # 红车被黑象反吃
        self.play(black_bishop.animate.move_to(red_rook.get_center()), FadeOut(arrow), FadeOut(red_rook))

        # 恢复局面
        self.play(FadeOut(black_bishop), FadeOut(red_king), FadeOut(black_king))
        black_bishop.move_to(xiangqi_board_upper[11].get_corner(DR))
        red_rook.move_to(xiangqi_board_downer[13].get_corner(DR))
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        arrow_protect = Arrow(start=black_bishop.get_center(), end=black_cannon.get_center(), buff=0.1, color=BLUE)

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(red_rook), Write(black_bishop), Write(black_cannon),
                  GrowArrow(arrow), GrowArrow(arrow_protect))

        # 红车攻击炮不算捉
        cross.move_to(arrow.get_center())
        big_cross.move_to(text_right.get_center())
        self.play(Write(cross), Write(big_cross))
        self.play(FadeOut(arrow), FadeOut(cross), FadeOut(big_cross), FadeOut(text_right))
        self.play(arrow_protect.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(arrow_protect), FadeOut(black_bishop), FadeOut(black_cannon), FadeOut(red_rook),
                  FadeOut(red_king), FadeOut(black_king), FadeOut(text_left))

        # 走法定义
        text_left = Text("车二平三", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉炮", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制帅
        red_king.move_to(xiangqi_board_downer[27].get_corner(DR))

        # 绘制将
        black_king.move_to(xiangqi_board_upper[3].get_corner(UR))

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[14].get_corner(DR))

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(red_rook), Write(black_cannon), Write(black_bishop),
                  Write(text_left), Write(text_right))

        # 平车捉炮
        arrow = Arrow(start=red_rook.get_center(), end=red_rook.get_center() + LEFT * 0.7,
                      buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_rook.animate.shift(LEFT * 0.7), FadeOut(arrow), text_left.animate.set_color(BLUE))

        # 红车攻击炮
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 红车吃炮
        self.play(red_rook.animate.move_to(black_cannon.get_center()), FadeOut(arrow), FadeOut(black_cannon))

        # 黑象保护炮
        arrow = Arrow(start=black_bishop.get_center(), end=black_cannon.get_center(), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))

        # 红车无法被黑象反吃
        self.play(black_bishop.animate.move_to(red_rook.get_center()), FadeOut(arrow), FadeOut(red_rook))
        arrow = Arrow(start=red_king.get_center(), end=black_king.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(black_bishop), FadeOut(red_king), FadeOut(black_king))

        # 恢复局面
        black_bishop.move_to(xiangqi_board_upper[11].get_corner(DR))
        red_rook.move_to(xiangqi_board_downer[13].get_corner(DR))
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        arrow_protect = Arrow(start=black_bishop.get_center(), end=black_cannon.get_center(), buff=0.1, color=BLUE)

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(red_rook), Write(black_bishop), Write(black_cannon),
                  GrowArrow(arrow), GrowArrow(arrow_protect), Write(text_left), Write(text_right))

        # 红车攻击炮算捉
        cross.move_to(arrow_protect.get_center())
        self.play(Write(cross))
        self.play(FadeOut(arrow_protect), FadeOut(cross))
        self.play(arrow.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(black_bishop), FadeOut(black_cannon), FadeOut(red_rook), FadeOut(red_king),
                  FadeOut(black_king), FadeOut(arrow), FadeOut(text_left), FadeOut(text_right))

        # 走法定义
        text_left = Text("车五进一", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉炮", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红炮
        border = Circle(color=RED, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_downer[19].get_corner(DR))
        cannon_text = MarkupText(f'<span foreground="{RED}"><b>炮</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        red_cannon = VGroup(border, cannon_text)

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[11].get_corner(DR))

        # 绘制黑车
        border = Circle(color=GRAY, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_upper[7].get_corner(UR))
        rook_text = MarkupText(f'<span foreground="{GRAY}"><b>车</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        black_rook = VGroup(border, rook_text)

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_downer[7].get_corner(DR))

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(red_rook), Write(red_cannon), Write(black_cannon),
                  Write(black_rook), Write(black_bishop), Write(text_left), Write(text_right))

        # 进车捉炮
        arrow = Arrow(start=red_rook.get_center(), end=red_rook.get_center() + UP * 0.7,
                      buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_rook.animate.shift(UP * 0.7), FadeOut(arrow), text_left.animate.set_color(BLUE))

        # 红车攻击炮
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 红车吃炮
        self.play(red_rook.animate.move_to(black_cannon.get_center()), FadeOut(arrow), FadeOut(black_cannon))

        # 黑车保护炮
        arrow = Arrow(start=black_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))

        # 红车无法被黑车反吃
        self.play(black_rook.animate.move_to(red_rook.get_center()), FadeOut(arrow), FadeOut(red_rook))
        arrow = Arrow(start=red_cannon.get_center(), end=black_king.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(black_rook), FadeOut(red_cannon), FadeOut(black_king), FadeOut(red_king),
                  FadeOut(black_bishop))

        # 恢复局面
        black_rook.move_to(xiangqi_board_upper[7].get_corner(UR))
        red_rook.move_to(xiangqi_board_downer[3].get_corner(DR))
        red_cannon.move_to(xiangqi_board_downer[19].get_corner(DR))
        black_cannon.move_to(xiangqi_board_downer[7].get_corner(DR))
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        arrow_protect = Arrow(start=black_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=BLUE)

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(red_rook), Write(black_rook), Write(red_cannon),
                  Write(black_cannon), Write(black_bishop), GrowArrow(arrow), GrowArrow(arrow_protect))

        # 红车攻击炮算捉
        cross.move_to(arrow_protect.get_center())
        self.play(Write(cross))
        self.play(FadeOut(arrow_protect), FadeOut(cross))
        self.play(arrow.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(black_rook), FadeOut(black_cannon), FadeOut(red_rook), FadeOut(red_king), FadeOut(red_cannon),
                  FadeOut(black_bishop), FadeOut(black_king), FadeOut(arrow), FadeOut(xiangqi_board),
                  FadeOut(text_left), FadeOut(text_right))

        ########################################################

        text = MarkupText('特殊情况3', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(f'吃掉被攻击子后可以被对方反吃<span foreground="{RED}">（马或炮攻击车除外）</span>',
                          font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(3)
        self.play(FadeOut(group))

        # 走法定义
        text_left = Text("马五进三", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉车", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制帅将
        red_king.move_to(xiangqi_board_downer[28].get_corner(DR))
        black_king.move_to(xiangqi_board_upper[2].get_corner(UR))

        # 绘制黑车
        black_rook.move_to(xiangqi_board_upper[6].get_corner(UR))
        black_rook2 = black_rook.copy()
        black_rook2.move_to(xiangqi_board_upper[22].get_corner(DR))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_upper[30].get_corner(DR))

        # 绘制红马
        border = Circle(color=RED, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_downer[3].get_corner(DR))
        knight_text = MarkupText(f'<span foreground="{RED}"><b>马</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        red_knight = VGroup(border, knight_text)

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(black_rook), Write(black_rook2),
                  Write(black_cannon), Write(red_knight), Write(text_left), Write(text_right))

        # 进马捉车
        arrow = Arrow(start=red_knight.get_center(), end=xiangqi_board_downer[5].get_corner(UR), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_knight.animate.move_to(xiangqi_board_downer[5].get_corner(UR)), FadeOut(arrow),
                  text_left.animate.set_color(BLUE))

        # 红马攻击黑车
        arrow = Arrow(start=red_knight.get_center(), end=black_rook2.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑底车保护黑车
        arrow_protect = Arrow(start=black_rook.get_center(), end=black_rook2.get_center(), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow_protect))

        # 红马攻击黑车算捉
        cross.move_to(arrow_protect.get_center())
        self.play(Write(cross))
        self.play(FadeOut(arrow_protect), FadeOut(cross))
        self.play(arrow.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(red_knight), FadeOut(black_rook), FadeOut(black_rook2), FadeOut(black_cannon),
                  FadeOut(red_king), FadeOut(black_king), FadeOut(arrow), FadeOut(text_left), FadeOut(text_right))

        # 走法定义
        text_left = Text("炮五平二", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉车", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红炮
        red_cannon.move_to(xiangqi_board_downer[3].get_corner(DR))

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(red_cannon), Write(black_rook), Write(black_cannon),
                  Write(black_rook2), Write(text_left), Write(text_right))

        # 平炮打车
        arrow = Arrow(start=red_cannon.get_center(), end=xiangqi_board_downer[6].get_corner(DR), buff=0.1,
                      color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_cannon.animate.move_to(xiangqi_board_downer[6].get_corner(DR)), FadeOut(arrow),
                  text_left.animate.set_color(BLUE))

        # 红炮攻击黑车
        arrow = Arrow(start=red_cannon.get_center(), end=black_rook2.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑底车保护黑车
        arrow_protect = Arrow(start=black_rook.get_center(), end=black_rook2.get_center(), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow_protect))

        # 红炮攻击黑车算捉
        cross.move_to(arrow_protect.get_center())
        self.play(Write(cross))
        self.play(FadeOut(arrow_protect), FadeOut(cross))
        self.play(arrow.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(red_cannon), FadeOut(black_rook), FadeOut(black_rook2), FadeOut(black_cannon),
                  FadeOut(red_king), FadeOut(black_king), FadeOut(arrow), FadeOut(xiangqi_board),
                  FadeOut(text_left), FadeOut(text_right))

        ########################################################

        text = MarkupText('特殊情况4', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(f'攻击同类子且被攻击子可反吃攻击子', font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(3)
        self.play(FadeOut(group))

        # 走法定义
        text_left = Text("车二平三", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉车", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[6].get_corner(DR))

        # 绘制黑车
        black_rook.move_to(xiangqi_board_upper[13].get_corner(DR))

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(red_rook), Write(black_rook),
                  Write(text_left), Write(text_right))

        # 平车捉车
        arrow = Arrow(start=red_rook.get_center(), end=xiangqi_board_downer[5].get_corner(DR), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_rook.animate.move_to(xiangqi_board_downer[5].get_corner(DR)), FadeOut(arrow),
                  text_left.animate.set_color(BLUE))

        # 黑车可以反吃红车
        arrow = Arrow(start=black_rook.get_center(), end=red_rook.get_center(), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(black_rook.animate.move_to(red_rook.get_center()), FadeOut(arrow), FadeOut(red_rook))

        # 恢复黑车与红车
        self.play(black_rook.animate.move_to(xiangqi_board_upper[13].get_corner(DR)), Write(red_rook))

        # 红车攻击黑车
        arrow = Arrow(start=red_rook.get_center(), end=black_rook.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        cross.move_to(arrow.get_center())
        big_cross.move_to(text_right.get_center())
        self.play(Write(cross), Write(big_cross))
        self.play(FadeOut(arrow), FadeOut(cross), FadeOut(big_cross), FadeOut(text_right))
        self.wait(1)
        self.play(FadeOut(text_left))

        # 走法定义
        text_left = Text("车三进四", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉车", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红炮
        red_cannon.move_to(xiangqi_board_downer[26].get_corner(DR))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_upper[2].get_corner(DR))

        # 启动绘制动画
        self.play(black_rook.animate.move_to(xiangqi_board_upper[10].get_corner(DR)), Write(red_cannon),
                  Write(black_cannon), Write(text_left), Write(text_right))

        # 进车捉车
        arrow = Arrow(start=red_rook.get_center(), end=xiangqi_board_upper[13].get_corner(DR), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_rook.animate.move_to(xiangqi_board_upper[13].get_corner(DR)), FadeOut(arrow),
                  text_left.animate.set_color(BLUE))

        # 黑车不可以反吃红车
        arrow = Arrow(start=black_rook.get_center(), end=red_rook.get_center(), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(black_rook.animate.move_to(red_rook.get_center()), FadeOut(arrow), FadeOut(red_rook))
        arrow = Arrow(start=red_cannon.get_center(), end=black_king.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        self.wait(1)
        self.play(FadeOut(arrow), black_rook.animate.move_to(xiangqi_board_upper[10].get_corner(DR)), Write(red_rook))

        # 红车攻击黑车
        arrow = Arrow(start=red_rook.get_center(), end=black_rook.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        self.play(arrow.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(red_rook), FadeOut(black_rook), FadeOut(red_cannon), FadeOut(black_cannon),
                  FadeOut(text_left), FadeOut(text_right))

        # 走法定义
        text_left = Text("马二进四", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉马", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_downer[3].get_corner(UR))

        # 绘制黑马
        border = Circle(color=GRAY, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_upper[27].get_corner(DR))
        knight_text = MarkupText(f'<span foreground="{GRAY}"><b>马</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        black_knight = VGroup(border, knight_text)

        # 绘制红马
        red_knight.move_to(xiangqi_board_downer[14].get_corner(DR))

        # 启动绘制动画
        self.play(Write(black_cannon), Write(black_knight), Write(red_knight), Write(text_left), Write(text_right))

        # 进马捉马
        arrow = Arrow(start=red_knight.get_center(), end=xiangqi_board_downer[4].get_corner(DR), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_knight.animate.move_to(xiangqi_board_downer[4].get_corner(DR)), FadeOut(arrow),
                  text_left.animate.set_color(BLUE))

        # 黑马不可以反吃红马
        arrow = Arrow(start=black_knight.get_center(), end=red_knight.get_center(), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(arrow), FadeOut(cross))

        # 红马攻击黑马
        arrow = Arrow(start=red_knight.get_center(), end=black_knight.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        self.play(arrow.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(red_knight), FadeOut(black_knight), FadeOut(black_cannon),
                  FadeOut(black_king), FadeOut(red_king), FadeOut(xiangqi_board), FadeOut(text_left),
                  FadeOut(text_right))

        # 闪捉
        text = MarkupText('闪捉(Discovered Chase)', font='Microsoft YaHei', font_size=50)
        self.play(GrowFromCenter(text))
        self.wait(1)
        self.play(FadeOut(text))

        # 走法定义
        text_left = Text("兵三平四", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉炮", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[13].get_corner(DR))

        # 绘制红兵
        red_pawn.move_to(xiangqi_board_upper[29].get_corner(DR))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_upper[13].get_corner(DR))

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(red_rook), Write(red_pawn),
                  Write(black_cannon), Write(text_left), Write(text_right))

        # 红车攻击不到黑炮
        arrow = Arrow(start=red_rook.get_center(), end=red_pawn.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        self.play(FadeOut(arrow))

        # 平兵闪捉炮
        arrow = Arrow(start=red_pawn.get_center(), end=red_pawn.get_center() + LEFT * 0.7,
                      buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(red_pawn.animate.shift(LEFT * 0.7), FadeOut(arrow), text_left.animate.set_color(BLUE))

        # 红车攻击炮
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        self.play(arrow.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(red_rook), FadeOut(red_pawn), FadeOut(black_cannon), FadeOut(red_king),
                  FadeOut(black_king), FadeOut(text_left), FadeOut(text_right))

        # 走法定义
        text_left = Text("炮四进四", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("捉炮", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_upper[29].get_corner(DR))

        # 绘制红炮
        red_cannon.move_to(red_rook.get_center() + LEFT * 0.7)

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(red_rook), Write(red_cannon), Write(black_cannon),
                  Write(black_bishop), Write(text_left), Write(text_right))

        # 红车攻击黑炮
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑象保护黑炮
        arrow_protect = Arrow(start=black_bishop.get_center(), end=black_cannon.get_center(), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow_protect))

        # 红车无法攻击黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(arrow), FadeOut(cross))

        # 进炮塞象眼
        arrow = Arrow(start=red_cannon.get_center(), end=black_bishop.get_center() + DR * 0.7, buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(FadeOut(arrow), red_cannon.animate.move_to(black_bishop.get_center() + DR * 0.7))
        cross.move_to(arrow_protect.get_center())
        self.play(Write(cross))
        self.play(FadeOut(arrow_protect), FadeOut(cross))

        # 红车攻击黑炮
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))
        self.play(arrow.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(red_rook), FadeOut(red_cannon), FadeOut(black_cannon), FadeOut(black_bishop),
                  FadeOut(red_king), FadeOut(black_king), FadeOut(xiangqi_board), FadeOut(text_left),
                  FadeOut(text_right))

        # 给出一个即将军同时又捉的例子
        text = MarkupText('将？捉？将兼捉？', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(
            '了解了将和捉的概念之后，考考大家，下面这个局面究竟是将还是捉呢？',
            font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(3)
        self.play(FadeOut(group))

        # 走法定义
        text_left = Text("车四进四", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("将军捉炮", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红车
        red_rook.move_to(xiangqi_board_upper[28].get_corner(DR))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_upper[7].get_corner(UR))

        # 开启绘制动画
        self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(red_rook), Write(black_cannon),
                  Write(text_left), Write(text_right))

        # 进车将军
        arrow = Arrow(start=red_rook.get_center(), end=xiangqi_board_upper[4].get_corner(UR), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow))
        self.play(FadeOut(arrow), red_rook.animate.move_to(xiangqi_board_upper[4].get_corner(UR)),
                  text_left.animate.set_color(BLUE))

        # 红车将军又捉炮
        arrow1 = Arrow(start=red_rook.get_center(), end=black_king.get_center(), buff=0.1, color=RED)
        arrow2 = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(Write(arrow1), Write(arrow2))
        self.wait(2)

        self.play(FadeOut(arrow1), FadeOut(arrow2), FadeOut(red_rook), FadeOut(black_cannon), FadeOut(black_king),
                  FadeOut(red_king), FadeOut(xiangqi_board), FadeOut(text_left), FadeOut(text_right))

        text = MarkupText('将不捉，捉不将', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(
            '大家很容易步入一个误区，认为在将军的同时可以捉子，这其实是不对的\n\n'
            '其实对比将军和捉的概念就会发现，将军必须攻击到将，而捉必须不能攻击到将：\n'
            f'凡走子直接<span foreground="{RED}">攻击对方将、帅者</span>谓之将军\n'
            f'凡走子<span foreground="{RED}">攻击对方将、帅以外之任何一子</span>，企图于下一着吃去之者，谓之捉\n\n'
            '将军和捉是互斥的，因此一个子在将军的同时又在捉子，重定义为将军，这步不捉任何子',
            font='Microsoft YaHei', font_size=24)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(8)
        self.play(FadeOut(group))

        self.play(Write(xiangqi_board), Write(red_rook), Write(black_cannon), Write(black_king), Write(red_king),
                  Write(arrow1), Write(arrow2), Write(text_left), Write(text_right))

        # 消除捉的箭头
        cross.move_to(arrow2.get_center())
        self.play(Write(cross))
        text = Text("将军", font="Microsoft YaHei", font_size=50, color=GREEN).move_to(RIGHT * 5)
        self.play(FadeOut(arrow2), FadeOut(cross))
        self.play(arrow1.animate.set_color(GREEN), Transform(text_right, text))
        self.wait(1)

        self.play(FadeOut(arrow1), FadeOut(red_rook), FadeOut(black_cannon), FadeOut(black_king),
                  FadeOut(red_king), FadeOut(xiangqi_board), FadeOut(text_left), FadeOut(text_right))

        # 逃避走法
        text = MarkupText('逃避(Evade)', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(
            '凡走子让<b>己方任何一子</b>从<b>被一个或多个对方子捉</b>转变为<b>不被任何一个对方子捉</b>，谓之逃避',
            font='Microsoft YaHei', font_size=26)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(3)
        self.play(FadeOut(group))

        # 走法定义
        text_left = Text("炮7平8", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("躲炮", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[5].get_corner(DR))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_upper[21].get_corner(UR))

        # 开启绘制动画
        self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(red_rook), Write(black_cannon),
                  Write(text_left), Write(text_right))

        # 红车攻击黑炮
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮平二
        arrow_move = Arrow(start=black_cannon.get_center(), end=xiangqi_board_upper[22].get_corner(UR), buff=0.1,
                           color=BLUE)
        self.play(GrowArrow(arrow_move))
        self.play(FadeOut(arrow_move), black_cannon.animate.move_to(xiangqi_board_upper[22].get_corner(UR)),
                  text_left.animate.set_color(BLUE))

        # 红车攻击不到黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(arrow), FadeOut(cross), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(red_rook), FadeOut(black_cannon), FadeOut(black_king), FadeOut(red_king), FadeOut(text_left),
                  FadeOut(text_right))

        # 走法定义
        text_left = Text("象5进7", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("挡车", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制黑象
        black_bishop.move_to(xiangqi_board_upper[11].get_corner(DR))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_upper[21].get_corner(DR))

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(black_bishop), Write(black_cannon), Write(red_rook),
                  Write(text_left), Write(text_right))

        # 红车攻击黑炮
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑象进7
        arrow_move = Arrow(start=black_bishop.get_center(), end=xiangqi_board_upper[29].get_corner(DR), buff=0.1,
                           color=BLUE)
        self.play(GrowArrow(arrow_move))
        self.play(FadeOut(arrow_move), black_bishop.animate.move_to(xiangqi_board_upper[29].get_corner(DR)),
                  text_left.animate.set_color(BLUE))

        # 红车攻击不到黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(arrow), FadeOut(cross), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(red_rook), FadeOut(black_cannon), FadeOut(black_bishop), FadeOut(black_king),
                  FadeOut(red_king), FadeOut(text_left), FadeOut(text_right))

        # 走法定义
        text_left = Text("炮7进1", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("生根", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制黑象
        black_bishop.move_to(xiangqi_board_upper[11].get_corner(DR))

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(black_bishop), Write(red_rook),
                  Write(black_cannon), Write(text_left), Write(text_right))

        # 红车攻击黑炮
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮进1
        arrow_move = Arrow(start=black_cannon.get_center(), end=xiangqi_board_upper[29].get_corner(DR), buff=0.1,
                           color=BLUE)
        arrow_new = Arrow(start=red_rook.get_center(), end=xiangqi_board_upper[29].get_corner(DR), buff=0.1, color=RED)
        self.play(GrowArrow(arrow_move))
        self.play(FadeOut(arrow_move), black_cannon.animate.move_to(xiangqi_board_upper[29].get_corner(DR)),
                  text_left.animate.set_color(BLUE), Transform(arrow, arrow_new))

        # 黑象保护炮
        arrow_protect = Arrow(start=black_bishop.get_center(), end=black_cannon.get_center(), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow_protect))

        # 红车攻击不到黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(arrow), FadeOut(cross))
        self.play(arrow_protect.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(red_rook), FadeOut(black_cannon), FadeOut(black_bishop), FadeOut(black_king),
                  FadeOut(red_king), FadeOut(text_left), FadeOut(text_right), FadeOut(arrow_protect))

        # 走法定义
        text_left = Text("车1进2", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("将军保炮", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[22].get_corner(DR))

        # 绘制黑车
        black_rook.move_to(xiangqi_board_downer[8].get_corner(DL))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_downer[6].get_corner(UR))

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(black_rook), Write(black_cannon), Write(red_rook),
                  Write(text_left), Write(text_right))

        # 红车攻击黑炮
        arrow = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑车进2
        arrow_move = Arrow(start=black_rook.get_center(), end=black_rook.get_center() + DOWN * 2 * 0.7, buff=0.1,
                           color=BLUE)
        self.play(GrowArrow(arrow_move))
        self.play(FadeOut(arrow_move), black_rook.animate.shift(DOWN * 2 * 0.7), text_left.animate.set_color(BLUE))

        # 黑将军
        arrow_check = Arrow(start=black_rook.get_center(), end=red_king.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow_check))

        # 红车无法攻击黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(arrow), FadeOut(cross))
        self.play(arrow_check.animate.set_color(GREEN), text_right.animate.set_color(GREEN))
        self.wait(1)

        self.play(FadeOut(red_rook), FadeOut(black_cannon), FadeOut(black_rook), FadeOut(black_king),
                  FadeOut(red_king), FadeOut(text_left), FadeOut(text_right), FadeOut(arrow_check))

        # 走法定义
        text_left = Text("炮三平一", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("躲炮", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制黑车
        black_rook.move_to(xiangqi_board_upper[5].get_corner(UR))
        black_rook2.move_to(xiangqi_board_upper[7].get_corner(UR))

        # 绘制红炮
        red_cannon.move_to(xiangqi_board_downer[5].get_corner(DR))

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(black_rook), Write(black_rook2),
                  Write(red_cannon), Write(text_left), Write(text_right))

        # 黑车攻击红炮
        arrow = Arrow(start=black_rook.get_center(), end=red_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 红炮躲避
        arrow_move = Arrow(start=red_cannon.get_center(), end=xiangqi_board_downer[7].get_corner(DR), buff=0.1,
                           color=BLUE)
        self.play(GrowArrow(arrow_move))
        self.play(FadeOut(arrow_move), red_cannon.animate.move_to(xiangqi_board_downer[7].get_corner(DR)),
                  text_left.animate.set_color(BLUE))

        # 黑车2攻击红炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(arrow), FadeOut(cross))
        arrow = Arrow(start=black_rook2.get_center(), end=red_cannon.get_center(), buff=0.1, color=RED)
        big_cross.move_to(text_right.get_center())
        self.play(GrowArrow(arrow), Write(big_cross))
        self.play(arrow.animate.set_color(GREEN), FadeOut(big_cross), FadeOut(text_right))
        self.wait(1)
        self.play(FadeOut(red_cannon), FadeOut(black_rook), FadeOut(black_rook2), FadeOut(black_king),
                  FadeOut(red_king), FadeOut(text_left), FadeOut(arrow))

        # 走法定义
        text_left = Text("车五平三", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("生根", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制黑象
        black_bishop.move_to(xiangqi_board_upper[11].get_corner(DR))

        # 绘制黑车
        black_rook.move_to(xiangqi_board_upper[27].get_corner(DR))

        # 启动绘制动画
        self.play(Write(red_king), Write(black_king), Write(black_rook), Write(black_bishop), Write(red_knight),
                  Write(text_left), Write(text_right))

        # 红马攻击黑车
        arrow = Arrow(start=red_knight.get_center(), end=black_rook.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑车躲避
        arrow_move = Arrow(start=black_rook.get_center(), end=xiangqi_board_upper[29].get_corner(DR), buff=0.1,
                           color=BLUE)
        arrow_new = Arrow(start=red_knight.get_center(), end=xiangqi_board_upper[29].get_corner(DR), buff=0.1,
                          color=RED)
        self.play(GrowArrow(arrow_move))
        self.play(FadeOut(arrow_move), black_rook.animate.move_to(xiangqi_board_upper[29].get_corner(DR)),
                  text_left.animate.set_color(BLUE), Transform(arrow, arrow_new))

        # 黑象保护黑车
        arrow_protect = Arrow(start=black_bishop.get_center(), end=black_rook.get_center(), buff=0.1, color=BLUE)
        self.play(GrowArrow(arrow_protect))

        # 红马攻击被保护的黑车
        cross.move_to(arrow_protect.get_center())
        big_cross.move_to(text_right.get_center())
        self.play(Write(cross), Write(big_cross))
        self.play(FadeOut(arrow_protect), FadeOut(cross), FadeOut(big_cross), FadeOut(text_right))
        self.play(arrow.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(red_knight), FadeOut(black_rook), FadeOut(black_bishop), FadeOut(black_king),
                  FadeOut(red_king), FadeOut(text_left), FadeOut(arrow), FadeOut(xiangqi_board))

        # 循环重复
        text = MarkupText('三次循环重复(Three-Fold Repetition)', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(
            '凡双方连续走子让<b>同一局面</b>在走子序列中<b>重复出现三次</b>，称为三次循环重复\n\n'
            '无论局势如何，三次循环重复一旦出现，棋局结束，胜负和则根据循环局面序列进行判决\n'
            '用于判决的循环局面序列，包括从局面第一次出现到第三次出现之间的所有局面\n\n'
            '同一局面：所有棋子摆放位置以及局面当前的走子方相同',
            font='Microsoft YaHei', font_size=26)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(8)
        self.play(FadeOut(group))

        # 局面信息定义
        text_left = Text("局 面 1", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("1", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)

        # 绘制红车
        red_rook.move_to(xiangqi_board_upper[13].get_corner(DR))

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(red_rook), Write(text_left),
                  Write(text_right))

        # 红车进二
        self.play(red_rook.animate.shift(UP * 2 * 0.7),
                  Transform(text_left, Text("局 面 2", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right, Text("1->\n2", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 黑将进1
        self.play(black_king.animate.shift(DOWN * 1 * 0.7),
                  Transform(text_left, Text("局 面 3", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right, Text("1->\n2->3", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 红车退一
        self.play(red_rook.animate.shift(DOWN * 1 * 0.7),
                  Transform(text_left, Text("局 面 4", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right, Text("1->\n2->3->4", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 黑将退一
        self.play(black_king.animate.shift(UP * 1 * 0.7),
                  Transform(text_left, Text("局 面 5", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right,
                            Text("1->\n2->3->4->5", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 红车进一
        self.play(red_rook.animate.shift(UP * 1 * 0.7),
                  Transform(text_left, Text("局 面 2", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right,
                            Text("1->\n2->3->4->5->\n2", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 黑将进1
        self.play(black_king.animate.shift(DOWN * 1 * 0.7),
                  Transform(text_left, Text("局 面 3", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right,
                            Text("1->\n2->3->4->5->\n2->3", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 红车退一
        self.play(red_rook.animate.shift(DOWN * 1 * 0.7),
                  Transform(text_left, Text("局 面 4", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right,
                            Text("1->\n2->3->4->5->\n2->3->4", font="Microsoft YaHei", font_size=40).move_to(
                                RIGHT * 5)))
        self.wait(1)

        # 黑将退一
        self.play(black_king.animate.shift(UP * 1 * 0.7),
                  Transform(text_left, Text("局 面 5", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right,
                            Text("1->\n2->3->4->5->\n2->3->4->5", font="Microsoft YaHei", font_size=40).move_to(
                                RIGHT * 5)))
        self.wait(1)

        # 红车进一
        self.play(red_rook.animate.shift(UP * 1 * 0.7),
                  Transform(text_left, Text("局 面 2", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right,
                            Text("1->\n2->3->4->5->\n2->3->4->5->\n2", font="Microsoft YaHei", font_size=40).move_to(
                                RIGHT * 5)))
        self.wait(1)

        self.play(FadeOut(text_left), FadeOut(red_king), FadeOut(black_king), FadeOut(red_rook), FadeOut(xiangqi_board),
                  text_right.animate.move_to(ORIGIN))
        self.play(text_right.animate.scale(2))
        self.wait(3)

        self.play(
            Transform(text_right, MarkupText(
                "循环局面序列：\n\n"
                "<b><i>2</i></b> ->3->4->5-> <b><i>2</i></b> ->3->4->5-> <b><i>2</i></b>\n\n"
                "其中，局面2循环出现了3次，第一次到第三次之间的所有局面形成了循环局面序列"
                , font="Microsoft YaHei", font_size=26)))
        self.wait(4)
        self.play(FadeOut(text_right))

        # 局面信息定义
        text_left = Text("局 面 1", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("1", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)

        # 绘制红车
        red_rook.move_to(xiangqi_board_upper[3].get_corner(DR))

        # 启动绘制
        self.play(Write(xiangqi_board), Write(red_rook), Write(red_king), Write(black_king), Write(text_left),
                  Write(text_right))

        # 红车进一
        self.play(red_rook.animate.shift(UP * 1 * 0.7),
                  Transform(text_left, Text("局 面 2", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right, Text("1->2", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 黑将进1
        self.play(black_king.animate.shift(DOWN * 1 * 0.7),
                  Transform(text_left, Text("局 面 3", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right, Text("1->2->3", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 红车退一
        self.play(red_rook.animate.shift(DOWN * 1 * 0.7),
                  Transform(text_left, Text("局 面 4", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right, Text("1->2->3->4", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 黑将退一
        self.play(black_king.animate.shift(UP * 1 * 0.7),
                  Transform(text_left, Text("局 面 1", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right,
                            Text("1->2->3->4->\n1", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 红车平六
        self.play(red_rook.animate.shift(LEFT * 1 * 0.7),
                  Transform(text_left, Text("局 面 5", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right,
                            Text("1->2->3->4->\n1->5", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 黑将平五
        self.play(black_king.animate.shift(RIGHT * 1 * 0.7),
                  Transform(text_left, Text("局 面 6", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right,
                            Text("1->2->3->4->\n1->5->6", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 红车平五
        self.play(red_rook.animate.shift(RIGHT * 1 * 0.7),
                  Transform(text_left, Text("局 面 7", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right,
                            Text("1->2->3->4->\n1->5->6->7", font="Microsoft YaHei", font_size=40).move_to(RIGHT * 5)))
        self.wait(1)

        # 黑将平四
        self.play(black_king.animate.shift(LEFT * 1 * 0.7),
                  Transform(text_left, Text("局 面 1", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)),
                  Transform(text_right,
                            Text("1->2->3->4->\n1->5->6->7->\n1", font="Microsoft YaHei", font_size=40).move_to(
                                RIGHT * 5)))
        self.wait(1)

        self.play(FadeOut(text_left), FadeOut(red_king), FadeOut(black_king), FadeOut(red_rook), FadeOut(xiangqi_board),
                  text_right.animate.move_to(ORIGIN))
        self.play(text_right.animate.scale(2))
        self.wait(3)

        self.play(
            Transform(text_right, MarkupText(
                "循环局面序列：\n\n"
                "<b><i>1</i></b> ->2->3->4-> <b><i>1</i></b> ->5->6->7-> <b><i>1</i></b>\n\n"
                "其中，局面1循环出现了3次，第一次到第三次之间的所有局面形成了循环局面序列"
                , font="Microsoft YaHei", font_size=26)))
        self.wait(4)
        self.play(FadeOut(text_right))

        # 长将
        text = MarkupText('长将(Perpetual Check)', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(
            '在循环局面序列中，某一方<b>每一步棋均为将军</b>，则称其为该方长将',
            font='Microsoft YaHei', font_size=26)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(4)
        self.play(FadeOut(group))

        # 红长将军
        text = MarkupText('红  方  长  将', font='Microsoft YaHei', font_size=60)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))

        # 绘制红马
        red_knight.move_to(xiangqi_board_upper[19].get_corner(DR))

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_knight), Write(red_king), Write(black_king))

        # 马五进七
        self.play(red_knight.animate.shift(LEFT * 2 * 0.7 + UP * 1 * 0.7))

        # 马攻击黑将
        arrow = Arrow(red_knight.get_center(), black_king.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑将进1
        self.play(black_king.animate.shift(DOWN * 1 * 0.7))
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 马七退五
        self.play(red_knight.animate.shift(RIGHT * 2 * 0.7 + DOWN * 1 * 0.7))

        # 马攻击黑将
        arrow = Arrow(red_knight.get_center(), black_king.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑将退1
        self.play(black_king.animate.shift(UP * 1 * 0.7))
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 马五进七
        self.play(red_knight.animate.shift(LEFT * 2 * 0.7 + UP * 1 * 0.7))

        # 马攻击黑将
        arrow = Arrow(red_knight.get_center(), black_king.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑将进1
        self.play(black_king.animate.shift(DOWN * 1 * 0.7))
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 马七退五
        self.play(red_knight.animate.shift(RIGHT * 2 * 0.7 + DOWN * 1 * 0.7))

        # 马攻击黑将
        arrow = Arrow(red_knight.get_center(), black_king.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑将退1
        self.play(black_king.animate.shift(UP * 1 * 0.7))
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        self.wait(1)
        self.play(FadeOut(red_knight), FadeOut(red_king), FadeOut(black_king), FadeOut(xiangqi_board))

        # 长捉
        text = MarkupText('长捉(Perpetual Chase)', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(
            '在循环局面序列中，某一方<b>每一步棋均捉同一子</b>\n'
            '而对方<b>每一步棋均逃避同一子</b>，则称其为该方长捉',
            font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(6)
        self.play(FadeOut(group))

        # 红长捉
        text = MarkupText('红  方  长  捉', font='Microsoft YaHei', font_size=60)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[14].get_corner(DR))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_upper[13].get_corner(DR))

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_rook), Write(red_king), Write(black_king), Write(black_cannon))

        # 红车平三
        self.play(red_rook.animate.shift(LEFT * 1 * 0.7))

        # 红车攻击黑炮
        arrow = Arrow(red_rook.get_center(), black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮平二
        self.play(black_cannon.animate.shift(RIGHT * 1 * 0.7))
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车平二
        self.play(red_rook.animate.shift(RIGHT * 1 * 0.7))

        # 红车攻击黑炮
        arrow = Arrow(red_rook.get_center(), black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮平三
        self.play(black_cannon.animate.shift(LEFT * 1 * 0.7))
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车平三
        self.play(red_rook.animate.shift(LEFT * 1 * 0.7))

        # 红车攻击黑炮
        arrow = Arrow(red_rook.get_center(), black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮平二
        self.play(black_cannon.animate.shift(RIGHT * 1 * 0.7))
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车平二
        self.play(red_rook.animate.shift(RIGHT * 1 * 0.7))

        # 红车攻击黑炮
        arrow = Arrow(red_rook.get_center(), black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮平三
        self.play(black_cannon.animate.shift(LEFT * 1 * 0.7))
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        self.wait(1)
        self.play(FadeOut(red_rook), FadeOut(red_king), FadeOut(black_king), FadeOut(black_cannon),
                  FadeOut(xiangqi_board))

        # 红非长捉
        text = MarkupText('分  捉  非  长  捉', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(
            '根据长捉定义，如在整个循环局面序列中被捉的<b>不是同一子</b>，则不为长捉。',
            font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(4)
        self.play(FadeOut(group))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_upper[13].get_corner(DR))

        # 绘制黑炮2
        black_cannon2 = black_cannon.copy()
        black_cannon2.move_to(xiangqi_board_upper[14].get_corner(DR))

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[14].get_corner(DR))

        # 绘制红帅
        red_king.move_to(xiangqi_board_downer[27].get_corner(DR))

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_rook), Write(red_king), Write(black_king), Write(black_cannon),
                  Write(black_cannon2))

        # 红车攻击黑炮2
        arrow = Arrow(red_rook.get_center(), black_cannon2.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮2平9
        self.play(black_cannon2.animate.shift(RIGHT * 1 * 0.7))

        # 红车攻击不到黑炮2
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车平一
        self.play(red_rook.animate.shift(RIGHT * 1 * 0.7))

        # 红车攻击黑炮
        arrow = Arrow(red_rook.get_center(), black_cannon2.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮平8
        self.play(black_cannon2.animate.shift(LEFT * 1 * 0.7))

        # 红车攻击不到黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车平三
        self.play(red_rook.animate.shift(LEFT * 2 * 0.7))

        # 红车攻击黑炮
        arrow = Arrow(red_rook.get_center(), black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮平6
        self.play(black_cannon.animate.shift(LEFT * 1 * 0.7))

        # 红车攻击不到黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车平四
        self.play(red_rook.animate.shift(LEFT * 1 * 0.7))

        # 红车攻击黑炮
        arrow = Arrow(red_rook.get_center(), black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮平7
        self.play(black_cannon.animate.shift(RIGHT * 1 * 0.7))

        # 红车攻击不到黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车平二
        self.play(red_rook.animate.shift(RIGHT * 2 * 0.7))

        # 红车攻击黑炮2
        arrow = Arrow(red_rook.get_center(), black_cannon2.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮2平9
        self.play(black_cannon2.animate.shift(RIGHT * 1 * 0.7))

        # 红车攻击不到黑炮2
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车平一
        self.play(red_rook.animate.shift(RIGHT * 1 * 0.7))

        # 红车攻击黑炮
        arrow = Arrow(red_rook.get_center(), black_cannon2.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮平8
        self.play(black_cannon2.animate.shift(LEFT * 1 * 0.7))

        # 红车攻击不到黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车平三
        self.play(red_rook.animate.shift(LEFT * 2 * 0.7))

        # 红车攻击黑炮
        arrow = Arrow(red_rook.get_center(), black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮平6
        self.play(black_cannon.animate.shift(LEFT * 1 * 0.7))

        # 红车攻击不到黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车平四
        self.play(red_rook.animate.shift(LEFT * 1 * 0.7))

        # 红车攻击黑炮
        arrow = Arrow(red_rook.get_center(), black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑炮平7
        self.play(black_cannon.animate.shift(RIGHT * 1 * 0.7))

        # 红车攻击不到黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车平二
        self.play(red_rook.animate.shift(RIGHT * 2 * 0.7))

        self.wait(1)
        self.play(FadeOut(red_rook), FadeOut(black_cannon), FadeOut(black_cannon2), FadeOut(xiangqi_board),
                  FadeOut(red_king), FadeOut(black_king))

        text = MarkupText('不  逃  非  长  捉', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(
            '根据长捉定义，如在整个循环局面序列中<b>被捉子不逃</b>，则不为长捉。\n'
            '注意：某一步是否捉某一子与走子之前是否已经攻击到该子无关。',
            font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(4)
        self.play(FadeOut(group))

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[22].get_corner(DR))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_upper[14].get_corner(DR))

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_rook), Write(black_cannon), Write(red_king), Write(black_king))

        # 红车攻击黑炮
        arrow = Arrow(red_rook.get_center(), black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 红车进一
        self.play(red_rook.animate.shift(UP * 1 * 0.7),
                  Transform(arrow,
                            Arrow(red_rook.get_center() + UP * 0.7, black_cannon.get_center(), buff=0.1, color=RED)))

        # 黑炮进1
        self.play(black_cannon.animate.shift(DOWN * 1 * 0.7),
                  Transform(arrow, Arrow(red_rook.get_center(), black_cannon.get_center() + DOWN * 0.7, buff=0.1,
                                         color=RED)))

        # 红车退一
        self.play(red_rook.animate.shift(DOWN * 1 * 0.7),
                  Transform(arrow, Arrow(red_rook.get_center() + DOWN * 0.7, black_cannon.get_center(), buff=0.1,
                                         color=RED)))

        # 黑炮退1
        self.play(black_cannon.animate.shift(UP * 1 * 0.7),
                  Transform(arrow, Arrow(red_rook.get_center(), black_cannon.get_center() + UP * 0.7, buff=0.1,
                                         color=RED)))

        # 红车进一
        self.play(red_rook.animate.shift(UP * 1 * 0.7),
                  Transform(arrow,
                            Arrow(red_rook.get_center() + UP * 0.7, black_cannon.get_center(), buff=0.1, color=RED)))

        # 黑炮进1
        self.play(black_cannon.animate.shift(DOWN * 1 * 0.7),
                  Transform(arrow, Arrow(red_rook.get_center(), black_cannon.get_center() + DOWN * 0.7, buff=0.1,
                                         color=RED)))

        # 红车退一
        self.play(red_rook.animate.shift(DOWN * 1 * 0.7),
                  Transform(arrow, Arrow(red_rook.get_center() + DOWN * 0.7, black_cannon.get_center(), buff=0.1,
                                         color=RED)))

        # 黑炮退1
        self.play(black_cannon.animate.shift(UP * 1 * 0.7),
                  Transform(arrow, Arrow(red_rook.get_center(), black_cannon.get_center() + UP * 0.7, buff=0.1,
                                         color=RED)))

        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(red_rook), FadeOut(black_cannon), FadeOut(xiangqi_board), FadeOut(red_king),
                  FadeOut(black_king))

        text = MarkupText('特  殊  长  捉', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(
            '当被长捉的子为<b>被马牵制的车</b>时，其严重程度高于被捉子为其他子。',
            font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(4)
        self.play(FadeOut(group))

        # 绘制黑马
        black_knight.move_to(xiangqi_board_downer[21].get_corner(DR))

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[20].get_corner(DR))

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_rook), Write(black_knight), Write(red_king), Write(black_king))

        # 展示一个环绕红车围成一个圆的动画
        self.play(Circumscribe(red_rook, Circle, fade_out=True, run_time=2))

        self.wait(1)
        self.play(FadeOut(red_rook), FadeOut(black_knight), FadeOut(xiangqi_board), FadeOut(red_king),
                  FadeOut(black_king))

        # 规则裁决
        text = MarkupText('三次循环裁决规则', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(
            '违规：只要任何一方形成长将，长捉，则称该方违规，违规的严重程度为：长将 > 长捉被马牵制的车 > 长捉其他子\n\n'
            '1. 双方均不违规或双方均违规但严重程度相同，则<b>判和</b>（如长将对长将）\n'
            '2. 一方违规，另一方不违规，则<b>违规方判负</b>（如红方长将，黑方不违规，红方判负）\n'
            '3. 双方均违规但严重程度不同，则<b>严重程度高的一方判负</b>（如红方长捉被马牵制的车，黑方长捉其他子，红方判负）\n',
            font='Microsoft YaHei', font_size=19)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(14)
        self.play(FadeOut(group))

        text_left = Text("红方长将\n\n红方长捉", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("黑方长将\n\n黑方长捉", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制黑将
        black_king.move_to(xiangqi_board_upper[3].get_corner(UR))

        # 绘制黑士
        border = Circle(color=GRAY, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_upper[2].get_corner(UR))
        advisor_text = MarkupText(f'<span foreground="{GRAY}"><b>士</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        black_advisor = VGroup(border, advisor_text)
        black_advisor2 = black_advisor.copy()
        black_advisor2.move_to(xiangqi_board_upper[4].get_corner(UR))

        # 绘制红士
        border = Circle(color=RED, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_downer[26].get_corner(DR))
        advisor_text = MarkupText(f'<span foreground="{RED}"><b>士</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        red_advisor = VGroup(border, advisor_text)

        # 绘制黑马
        black_knight.move_to(xiangqi_board_upper[3].get_corner(DR))

        # 绘制黑车
        black_rook.move_to(xiangqi_board_downer[21].get_corner(DR))

        # 绘制红炮
        red_cannon.move_to(xiangqi_board_downer[9].get_corner(DR))

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_cannon), Write(black_rook), Write(black_knight), Write(black_king),
                  Write(black_advisor), Write(black_advisor2), Write(red_advisor), Write(red_king), Write(text_left),
                  Write(text_right))

        self.wait(3)

        # 黑车平到炮位
        self.play(black_rook.animate.shift(LEFT * 4 * 0.7),
                  Transform(text_right, Text("黑方长捉", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)))

        # 红炮平到黑车位
        self.play(red_cannon.animate.shift(RIGHT * 4 * 0.7), FadeOut(text_left))

        # 黑车平到炮位
        self.play(black_rook.animate.shift(RIGHT * 4 * 0.7))

        # 红炮平到黑车位
        self.play(red_cannon.animate.shift(LEFT * 4 * 0.7))

        # 黑车进1，将军
        self.play(black_rook.animate.shift(DOWN * 0.7), FadeOut(text_right))

        # 红帅进一
        self.play(red_king.animate.shift(UP * 0.7))

        # 黑车退1，将军
        self.play(black_rook.animate.shift(UP * 0.7))

        # 红帅退一
        self.play(red_king.animate.shift(DOWN * 0.7))

        self.wait(1)
        self.play(FadeOut(red_cannon), FadeOut(black_advisor), FadeOut(black_advisor2))

        text_left = Text("红方长将\n\n红方长捉", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("黑方长将\n\n黑方长捉", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[20].get_corner(DR))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_downer[16].get_corner(DL))

        # 启动绘制动画
        self.play(Write(red_rook), Write(black_cannon), Write(text_left), Write(text_right),
                  black_knight.animate.move_to(red_rook.get_center() + RIGHT * 0.7),
                  red_advisor.animate.move_to(red_rook.get_center() + LEFT * 0.7),
                  black_rook.animate.move_to(black_cannon.get_center() + RIGHT * 0.7),
                  black_king.animate.move_to(xiangqi_board_upper[2].get_corner(UR)))

        self.wait(3)

        # 黑车退1
        self.play(black_rook.animate.shift(UP * 0.7),
                  Transform(text_right, Text("黑方长捉", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)))

        # 黑炮捉红车
        arrow = Arrow(start=black_cannon.get_center(), end=red_rook.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 红士退六
        self.play(red_advisor.animate.shift(DL * 0.7),
                  Transform(text_left, Text("红方长捉", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)))

        # 黑炮无法捉红车
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车攻击黑马和黑炮
        arrow = Arrow(start=red_rook.get_center(), end=black_knight.get_center(), buff=0.1, color=RED)
        arrow2 = Arrow(start=red_rook.get_center(), end=black_cannon.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow), GrowArrow(arrow2))

        # 黑车退一
        self.play(black_rook.animate.shift(DOWN * 0.7))

        # 黑炮和黑车保护黑马
        arc = ArcBetweenPoints(start=black_cannon.get_center(), end=black_knight.get_center(), angle=-PI / 2,
                               color=BLUE)
        arc2 = ArcBetweenPoints(start=black_rook.get_center(), end=black_knight.get_center(), angle=-PI / 2, color=BLUE)
        self.play(Create(arc), Create(arc2))

        # 红车无法捉黑马和黑炮
        cross.move_to(arrow.get_center())
        cross2 = cross.copy()
        cross2.move_to(arrow2.get_center())
        self.play(Write(cross), Write(cross2))
        self.play(FadeOut(cross), FadeOut(cross2), FadeOut(arrow), FadeOut(arrow2))

        # 黑炮和黑车捉红车
        arrow_ = Arrow(start=black_cannon.get_center(), end=red_rook.get_center(), buff=0.1, color=RED)
        arrow_2 = Arrow(start=black_rook.get_center(), end=red_rook.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow_), GrowArrow(arrow_2))

        # 红士进六
        self.play(red_advisor.animate.shift(UR * 0.7))

        # 黑方无法攻击红车
        cross.move_to(arrow_.get_center())
        cross2.move_to(arrow_2.get_center())
        self.play(Write(cross), Write(cross2))
        self.play(FadeOut(cross), FadeOut(cross2), FadeOut(arc), FadeOut(arc2), FadeOut(arrow_), FadeOut(arrow_2))

        # 红车攻击黑马
        arrow = Arrow(start=red_rook.get_center(), end=black_knight.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑车退1
        self.play(black_rook.animate.shift(UP * 0.7))

        arc = ArcBetweenPoints(start=black_cannon.get_center(), end=black_knight.get_center(), angle=-PI / 2,
                               color=BLUE)
        self.play(Create(arc))

        # 红车无法捉黑马
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        arrow = Arrow(start=black_cannon.get_center(), end=red_rook.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 红士退六
        self.play(red_advisor.animate.shift(DL * 0.7))

        # 黑炮无法捉红车
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow), FadeOut(arc))

        # 红车捉黑马
        arrow = Arrow(start=red_rook.get_center(), end=black_knight.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑车退一
        self.play(black_rook.animate.shift(DOWN * 0.7))

        # 黑炮和黑车保护黑马
        arc = ArcBetweenPoints(start=black_cannon.get_center(), end=black_knight.get_center(), angle=-PI / 2,
                               color=BLUE)
        arc2 = ArcBetweenPoints(start=black_rook.get_center(), end=black_knight.get_center(), angle=-PI / 2, color=BLUE)
        self.play(Create(arc), Create(arc2))

        # 红车无法捉黑马和黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 黑炮和黑车捉红车
        arrow_ = Arrow(start=black_cannon.get_center(), end=red_rook.get_center(), buff=0.1, color=RED)
        arrow_2 = Arrow(start=black_rook.get_center(), end=red_rook.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow_), GrowArrow(arrow_2))

        # 红士进六
        self.play(red_advisor.animate.shift(UR * 0.7))

        # 黑方无法攻击红车
        cross.move_to(arrow_.get_center())
        cross2.move_to(arrow_2.get_center())
        self.play(Write(cross), Write(cross2))
        self.play(FadeOut(cross), FadeOut(cross2), FadeOut(arc), FadeOut(arc2), FadeOut(arrow_), FadeOut(arrow_2))

        # 红车攻击黑马
        arrow = Arrow(start=red_rook.get_center(), end=black_knight.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        self.play(text_left.animate.set_color(GREEN), text_right.animate.set_color(GREEN))

        self.wait(1)
        self.play(FadeOut(red_rook), FadeOut(black_cannon), FadeOut(black_knight), FadeOut(black_king), FadeOut(arrow),
                  FadeOut(red_king), FadeOut(black_rook), FadeOut(red_advisor), FadeOut(xiangqi_board))

        text = Text("黑方长捉被马牵制红车 > 红方长捉黑马，黑方判负", font='Microsoft YaHei', font_size=40)
        self.play(ReplacementTransform(VGroup(text_left, text_right), text))

        self.wait(3)
        self.play(FadeOut(text))

        text_left = Text("红方长将\n\n红方长捉", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("黑方长将\n\n黑方长捉", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(red_rook), Write(black_knight), Write(red_advisor), Write(black_rook),
                  Write(black_king), Write(red_king), Write(text_left), Write(text_right))

        self.wait(3)

        # 黑车进1
        self.play(black_rook.animate.shift(DOWN * 0.7),
                  Transform(text_right, Text("黑方长将", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)))

        # 黑车将军
        arrow = Arrow(start=black_rook.get_center(), end=red_king.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 红士退六
        self.play(red_advisor.animate.shift(DL * 0.7),
                  Transform(text_left, Text("红方长捉", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)))

        # 黑车无法将军
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红车攻击黑马
        arrow = Arrow(start=red_rook.get_center(), end=black_knight.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑车退一
        self.play(black_rook.animate.shift(UP * 0.7), FadeOut(text_right))

        # 黑车保护黑马
        arc = ArcBetweenPoints(start=black_rook.get_center(), end=black_knight.get_center(), angle=-PI / 2, color=BLUE)
        self.play(Create(arc))

        # 红车无法捉黑马
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红士进六
        self.play(red_advisor.animate.shift(UR * 0.7))

        cross.move_to(arc.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arc))

        # 红车攻击黑马
        arrow = Arrow(start=red_rook.get_center(), end=black_knight.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑车进1
        self.play(black_rook.animate.shift(DOWN * 0.7))

        arrow_ = Arrow(start=black_rook.get_center(), end=red_king.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow_))

        # 红车无法捉黑马
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红士退六
        self.play(red_advisor.animate.shift(DL * 0.7))

        cross.move_to(arrow_.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow_))

        # 红车捉黑马
        arrow = Arrow(start=red_rook.get_center(), end=black_knight.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        # 黑车退一
        self.play(black_rook.animate.shift(UP * 0.7))

        # 黑车保护黑马
        arc = ArcBetweenPoints(start=black_rook.get_center(), end=black_knight.get_center(), angle=-PI / 2, color=BLUE)
        self.play(Create(arc))

        # 红车无法捉黑炮
        cross.move_to(arrow.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arrow))

        # 红士进六
        self.play(red_advisor.animate.shift(UR * 0.7))

        cross.move_to(arc.get_center())
        self.play(Write(cross))
        self.play(FadeOut(cross), FadeOut(arc))

        # 红车攻击黑马
        arrow = Arrow(start=red_rook.get_center(), end=black_knight.get_center(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        self.play(text_left.animate.set_color(GREEN))

        self.wait(1)
        self.play(FadeOut(red_rook), FadeOut(black_knight), FadeOut(black_king), FadeOut(arrow), FadeOut(red_king),
                  FadeOut(black_rook), FadeOut(red_advisor), FadeOut(xiangqi_board))

        self.play(Transform(text_left, Text("红方长捉黑马，红方判负", font='Microsoft YaHei', font_size=50)))

        self.wait(2)
        self.play(FadeOut(text_left))

        # 六十回合不吃子和棋
        text = MarkupText('六十回合不吃子和棋', font='Microsoft YaHei', font_size=50)
        desc = MarkupText(
            '满足以下全部3个条件时，游戏以和棋结束：\n\n'
            '1. 在六十回合（120步）内双方都没有吃子\n'
            '2. 第120步时没有发生三次循环重复，如有，按照三次循环规则裁决\n'
            '3. 第120步没有将死或困毙，如有，不作和棋\n\n'
            '其中，120步中，双方将军<b>各自最多计算10回合</b>',
            font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(14)
        self.play(FadeOut(group))

        # 双方没有吃子
        text = MarkupText('120步不吃子和棋', font='Microsoft YaHei', font_size=60)
        self.play(Write(text))
        self.wait(4)
        self.play(FadeOut(text))

        text_left = Text("不吃子步数：\n\n119", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("判和", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红兵
        red_pawn.move_to(xiangqi_board_upper[3].get_corner(DR))

        self.play(Write(xiangqi_board), Write(text_left), Write(text_right), Write(red_pawn), Write(red_king),
                  Write(black_king))

        # 红车向右移动
        self.play(red_pawn.animate.shift(RIGHT * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n120", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)))
        self.play(text_right.animate.set_color(GREEN))
        self.wait(1)
        self.play(FadeOut(red_pawn), FadeOut(xiangqi_board), FadeOut(text_left), FadeOut(text_right), FadeOut(red_king),
                  FadeOut(black_king))

        # 双方没有吃子
        text = MarkupText('120步时将死或困毙，不和棋', font='Microsoft YaHei', font_size=60)
        self.play(Write(text))
        self.wait(4)
        self.play(FadeOut(text))

        text_left = Text("不吃子步数：\n\n119", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("判和", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红车
        red_rook.move_to(xiangqi_board_upper[3].get_corner(DR))

        self.play(Write(xiangqi_board), Write(text_left), Write(text_right), Write(red_rook), Write(red_king),
                  Write(black_king))

        # 红帅进一
        self.play(red_king.animate.shift(UP * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n120", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)))
        self.play(
            Transform(text_right, Text("困毙", font="Microsoft YaHei", font_size=50, color=GREEN).move_to(RIGHT * 5)))
        self.wait(1)
        self.play(FadeOut(red_rook), FadeOut(xiangqi_board), FadeOut(text_left), FadeOut(text_right), FadeOut(red_king),
                  FadeOut(black_king))

        # 双方没有吃子
        text = MarkupText('在120步时发生三次循环重复', font='Microsoft YaHei', font_size=50)
        self.play(Write(text))
        self.wait(4)
        self.play(FadeOut(text))

        text_left = Text("不吃子步数：\n\n112", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)
        text_right = Text("判和", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 绘制红帅
        red_king.move_to(xiangqi_board_downer[27].get_corner(DR))

        self.play(Write(xiangqi_board), Write(text_left), Write(text_right), Write(red_rook), Write(red_king),
                  Write(black_king))

        # 红车进一
        self.play(red_rook.animate.shift(UP * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n113", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)))

        # 黑帅进1
        self.play(black_king.animate.shift(DOWN * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n114", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)))

        # 红车退一
        self.play(red_rook.animate.shift(DOWN * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n115", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)))

        # 黑帅退1
        self.play(black_king.animate.shift(UP * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n116", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)))

        # 红车进一
        self.play(red_rook.animate.shift(UP * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n117", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)))

        # 黑帅进1
        self.play(black_king.animate.shift(DOWN * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n118", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)))

        # 红车退一
        self.play(red_rook.animate.shift(DOWN * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n119", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)))

        # 黑帅退1
        self.play(black_king.animate.shift(UP * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n120", font="Microsoft YaHei", font_size=50).move_to(LEFT * 5)))

        self.play(
            Transform(text_right,
                      Text("长将判负", font="Microsoft YaHei", font_size=50, color=GREEN).move_to(RIGHT * 5)))
        self.wait(1)
        self.play(FadeOut(red_rook), FadeOut(xiangqi_board), FadeOut(text_left), FadeOut(text_right), FadeOut(red_king),
                  FadeOut(black_king))

        # 超过将军的步数无效
        text = MarkupText('超过10次将军不算入计数器', font='Microsoft YaHei', font_size=50)
        desc = MarkupText('超出的将军步，60回合计数器减1', font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(4)
        self.play(FadeOut(group))

        text_left = Text("不吃子步数：\n\n118\n\n红方已将军步数：\n\n10", font="Microsoft YaHei", font_size=40).move_to(
            LEFT * 5)
        text_right = Text("判和", font="Microsoft YaHei", font_size=50).move_to(RIGHT * 5)

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(text_left), Write(text_right), Write(red_rook), Write(red_king),
                  Write(black_king))

        # 红车进一
        self.play(red_rook.animate.shift(UP * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n117\n\n红方已将军步数：\n\n11", font="Microsoft YaHei",
                                 font_size=40).move_to(LEFT * 5)))

        # 黑帅进1
        self.play(black_king.animate.shift(DOWN * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n118\n\n红方已将军步数：\n\n11", font="Microsoft YaHei",
                                 font_size=40).move_to(LEFT * 5)))

        # 红车退一
        self.play(red_rook.animate.shift(DOWN * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n117\n\n红方已将军步数：\n\n12", font="Microsoft YaHei",
                                 font_size=40).move_to(LEFT * 5)))

        # 黑帅退1
        self.play(black_king.animate.shift(UP * 1 * 0.7),
                  Transform(text_left,
                            Text("不吃子步数：\n\n118\n\n红方已将军步数：\n\n12", font="Microsoft YaHei",
                                 font_size=40).move_to(LEFT * 5)))

        self.play(FadeOut(text_right))
        self.wait(1)
        self.play(FadeOut(red_rook), FadeOut(xiangqi_board), FadeOut(text_left), FadeOut(red_king), FadeOut(black_king))

        # 吃子时又将军
        text = MarkupText('吃子归零', font='Microsoft YaHei', font_size=50)
        desc = MarkupText('只要吃子，吃子那一步全部计数器归零，无论是否将军', font='Microsoft YaHei', font_size=30)
        group = VGroup(text, desc).arrange(DOWN, buff=1)
        self.play(Write(group))
        self.wait(4)
        self.play(FadeOut(group))

        xiangqi_board.shift(RIGHT * 2)

        text_left = Text("不吃子步数：\n\n118\n\n红方已将军步数：\n\n10\n\n黑方已将军步数：\n\n10", font="Microsoft YaHei",
                         font_size=40).move_to(LEFT * 5)

        # 绘制红帅
        red_king.shift(RIGHT * 2)

        # 绘制黑将
        black_king.shift(RIGHT * 2)

        # 绘制红车
        red_rook.move_to(xiangqi_board_downer[6].get_corner(UR))

        # 绘制黑炮
        black_cannon.move_to(xiangqi_board_upper[6].get_corner(UR))

        # 启动绘制动画
        self.play(Write(xiangqi_board), Write(text_left), Write(red_rook), Write(black_cannon), Write(red_king),
                  Write(black_king))

        self.wait(1)

        # 进车吃炮
        self.play(red_rook.animate.move_to(black_cannon.get_center()), FadeOut(black_cannon),
                  Transform(text_left,
                            Text("不吃子步数：\n\n0\n\n红方已将军步数：\n\n0\n\n黑方已将军步数：\n\n0",
                                 font="Microsoft YaHei",
                                 font_size=40).move_to(LEFT * 5)))
        self.wait(1)
        self.play(FadeOut(xiangqi_board), FadeOut(text_left), FadeOut(red_rook), FadeOut(red_king), FadeOut(black_king))
