from manim import *
import random
import colour

config.max_files_cached = -1


class TranspositionTable(Scene):
    # title
    title = MarkupText(f'<span foreground="{BLUE}">象棋引擎密界兵器系列 之 <i>置换表</i></span>',
                       font="Microsoft YaHei", font_size=30).to_corner(UL)

    def setup(self):
        # load pikacat avatar
        pikacat_avatar = ImageMobject("images/pikacat.jpg").scale(0.2)
        # pikacat name
        pikacat_name = Text("PikaCat皮卡喵", font="Microsoft YaHei", color=WHITE) \
            .next_to(pikacat_avatar, DOWN)
        # show pikacat info and show title
        self.play(Write(self.title), FadeIn(pikacat_avatar), Write(pikacat_name))
        self.wait(1)
        # hide pikacat info
        self.play(FadeOut(pikacat_avatar), FadeOut(pikacat_name))
        self.remove(pikacat_avatar, pikacat_name)

    def tear_down(self):
        # load pikacat avatar
        pikacat_avatar = ImageMobject("images/pikacat.jpg").scale(0.2)
        # pikacat name
        pikacat_name = Text("PikaCat皮卡喵", font="Microsoft YaHei", color=WHITE) \
            .next_to(pikacat_avatar, DOWN)
        # show pikacat info and transform title into info
        self.play(FadeIn(pikacat_avatar), Transform(self.title, pikacat_name))
        self.wait(3)
        # hide pikacat info
        self.play(FadeOut(pikacat_avatar), FadeOut(self.title))
        self.remove(pikacat_avatar, self.title)

    def hash_table(self):
        display_text = MarkupText("欢迎来到 象棋引擎密界兵器系列 之 <i>置换表</i>",
                                  font="Microsoft YaHei", font_size=30)
        self.play(Write(display_text))
        self.wait(1)

        engine_setting = ImageMobject("images/engine_setting.jpg").scale(2)
        engine_setting.shift(DOWN)
        self.play(display_text.animate.shift(UP * 2), FadeIn(engine_setting))
        text = MarkupText("相信用过象棋引擎的小朋友都知道这个选项吧，它可以设置引擎置换表的大小",
                          font="Microsoft YaHei", font_size=30).move_to(display_text)
        self.play(Transform(display_text, text))

        border_box = Rectangle(height=1, width=2, fill_opacity=0, stroke_width=8,
                               color=colour.Color(RED)).shift(DR * 1.7)
        self.play(DrawBorderThenFill(border_box))
        self.wait(2)

        text = MarkupText("那么，置换表是什么呢？", font="Microsoft YaHei", font_size=30) \
            .move_to(display_text)
        questioning = ImageMobject("images/questioning.png").scale(7).shift(DOWN)
        self.play(Transform(display_text, text),
                  FadeOut(engine_setting),
                  FadeOut(border_box),
                  FadeIn(questioning))
        self.remove(engine_setting)
        self.wait(2)

        tt_text = f'<span foreground="{RED}">置换表</span>'
        hash_text = f'<span foreground="{PURE_GREEN}">哈希表</span>'
        text = MarkupText(f'{tt_text}是一种数据结构，用于存储搜索过程中的中间结果，它的作用主要有：'
                          '<gradient from="RED" to="YELLOW">'
                          '\n1、在搜索过程中遇到重复的局面时可以直接返回结果，从而减少不必要的搜索\n</gradient>'
                          '<gradient from="YELLOW" to="GREEN">'
                          "2、用于多线程Lazy-SMP，这种多线程算法基于在各个线程之间共享置换表进行\n</gradient>"
                          '<gradient from="GREEN" to="BLUE">'
                          "3、置换表使用的局面哈希值可以用来做棋规犯规检查，从而避免搜索到非法局面</gradient>",
                          font="Microsoft YaHei", font_size=26).move_to(display_text).shift(DOWN)
        self.play(FadeOut(questioning), Transform(display_text, text))
        self.remove(questioning)
        self.wait(6)
        text = MarkupText(f"{tt_text}本质上说是一种{hash_text}，要了解{tt_text}首先需要了解什么是{hash_text}",
                          font="Microsoft YaHei", font_size=26).next_to(display_text, DOWN, buff=2)
        self.play(DrawBorderThenFill(text))
        self.wait(4)

        self.play(FadeOut(text))
        text = MarkupText(f"那么哈希表是什么呢？", font="Microsoft YaHei", font_size=30) \
            .move_to(display_text).shift(UP)
        self.play(Transform(display_text, text))
        self.wait(1)
        text = MarkupText(f'哈希表是一种数据结构，它的特点是：'
                          '<gradient from="RED" to="YELLOW">'
                          '\n1、通过哈希函数将键值映射到哈希表中的一个位置\n</gradient>'
                          '<gradient from="YELLOW" to="GREEN">'
                          '2、哈希表中的每个位置可以存储一个或多个键值对，通过哈希冲突解决方法解决冲突问题\n'
                          '</gradient><gradient from="GREEN" to="BLUE">'
                          '3、通过哈希函数可以快速查找到键值对应的位置</gradient>',
                          font="Microsoft YaHei", font_size=26)
        self.play(ShowIncreasingSubsets(text))
        self.wait(6)

        temp_text = MarkupText(f'这里我们提到了3个概念：'
                               '<gradient from="RED" to="YELLOW">'
                               '\n1、哈希函数\n</gradient>'
                               '<gradient from="YELLOW" to="GREEN">'
                               '2、哈希冲突解决方法\n</gradient>'
                               '<gradient from="GREEN" to="BLUE">'
                               '3、哈希表的查找</gradient>', font="Microsoft YaHei", font_size=30) \
            .move_to(text)
        self.play(Transform(text, temp_text))
        self.wait(4)

        annoying_image = ImageMobject("images/annoying.jpg").scale(0.4).shift(DOWN)
        self.play(Transform(display_text,
                            Text("你说那么多我也听不懂鸭qwq，还是看看动画罢", font="Microsoft YaHei",
                                 font_size=30).move_to(display_text)),
                  FadeIn(annoying_image), Uncreate(text))
        self.wait(3)
        self.play(FadeOut(annoying_image), Uncreate(display_text))
        self.remove(annoying_image)

        temp_text = Text("哈  希  函  数", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(temp_text))
        self.wait(1)
        self.play(FadeOut(temp_text))
        # draw hash table with length of 8
        hash_table = VGroup(*[Rectangle(height=1, width=1, fill_opacity=0, stroke_width=8)
                              for _ in range(8)]).arrange(RIGHT)
        hash_index = VGroup(*[Text(str(i), font="Microsoft YaHei", font_size=30)
                              for i in range(8)]).arrange(RIGHT, buff=1.06)
        hash_table = VGroup(hash_table, hash_index).arrange(DOWN)
        border = SurroundingRectangle(hash_table, buff=0.2, color=BLUE, corner_radius=0.1)
        hash_text = Text("哈 希 表", font="Microsoft YaHei", font_size=30).next_to(border, DOWN)
        self.play(Create(hash_table), DrawBorderThenFill(hash_text), Create(border))
        hash_table = VGroup(hash_table, hash_text, border)
        self.play(hash_table.animate.shift(DOWN * 2.2))
        # draw hash function of key as key % 8, also draw 5 input data
        hash_info = MarkupText('哈希函数：hash(key) = key % 8\n'
                               '输入数据：[12, 45, 32, 11, 2]', font="Microsoft YaHei", font_size=30) \
            .next_to(hash_table, UP, buff=0.5)
        self.play(GrowFromCenter(hash_info))
        self.play(hash_info.animate.next_to(self.title, DOWN))
        self.wait(1)
        # put all the data into hash table
        data_texts = []

        def draw_data(_data):
            # draw data
            _data_text = Text(str(_data), font="Microsoft YaHei").next_to(hash_table, UP, buff=1.7)
            self.play(SpinInFromNothing(_data_text))
            self.wait(1)
            # draw the hash key calculation process
            _hash_key = Text(f"hash({_data}) = {_data} % 8 = {_data % 8}",
                             font="Microsoft YaHei").move_to(_data_text)
            self.play(ReplacementTransform(_data_text, _hash_key))
            self.wait(1)
            # calculate the hash key position
            index = _data % 8
            _data_text = Text(str(_data), font="Microsoft YaHei", font_size=30)
            _data_text.move_to(hash_table[0][0][index])
            # draw an arrow from hash key to the position
            _arrow = Arrow(_hash_key.get_center(), _data_text.get_center(), buff=0.1, color=BLUE)
            self.play(Create(_arrow))
            data_texts.append(_data_text)
            return _data_text, _hash_key, _arrow

        for data in [12, 45, 32, 11, 2]:
            data_text, hash_key, arrow = draw_data(data)
            # put the data into hash table
            self.play(ReplacementTransform(hash_key, data_text))
            # remove the arrow
            self.play(FadeOut(arrow))
            self.remove(arrow)
        self.wait(2)
        self.play(FadeOut(hash_info), FadeOut(hash_table),
                  *[FadeOut(data_text) for data_text in data_texts])

        temp_text = Text("哈  希  冲  突", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(temp_text))
        self.wait(1)
        new_hash_info = MarkupText('哈希函数：hash(key) = key % 8\n输入数据：4',
                                   font="Microsoft YaHei", font_size=30).move_to(hash_info)
        self.play(FadeOut(temp_text), FadeIn(hash_info), FadeIn(hash_table),
                  *[FadeIn(data_text) for data_text in data_texts])
        self.play(Transform(hash_info, new_hash_info))
        # draw a new data
        data_text, hash_key, arrow = draw_data(4)
        # show collision happens
        temp_text = Text("哈希冲突！", font="Microsoft YaHei").move_to(hash_key)
        self.play(Transform(hash_key, temp_text))
        self.wait(1)
        # directly replace the data
        temp_text = MarkupText("为了和置换表的行为切合，我们这里采用直接替换表项的冲突解决方法\n"
                               "实际哈希表中，我们多采用链表法或开放寻址法等方法",
                               font="Microsoft YaHei", font_size=30).move_to(hash_key)
        self.play(Transform(hash_key, temp_text))
        self.wait(5)
        self.play(ReplacementTransform(hash_key, data_text), FadeOut(data_texts[0]))
        self.remove(data_texts[0])
        data_texts.pop(0)
        self.play(FadeOut(arrow))
        self.wait(2)
        self.play(FadeOut(hash_info), FadeOut(hash_table),
                  *[FadeOut(data_text) for data_text in data_texts])

        temp_text = Text("哈  希  查  找", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(temp_text))
        self.wait(1)
        self.play(FadeOut(temp_text), FadeIn(hash_info), FadeIn(hash_table),
                  *[FadeIn(data_text) for data_text in data_texts])
        new_hash_info = MarkupText('哈希函数：hash(key) = key % 8\n'
                                   '查找序列：[45, 32, 7, 12]', font="Microsoft YaHei",
                                   font_size=30).move_to(hash_info)
        self.play(Transform(hash_info, new_hash_info))

        def find_data(_data):
            _data_text, _hash_key, _arrow = draw_data(_data)
            if _data == 12:
                _new_data_text = Text('4', font="Microsoft YaHei", font_size=30)
                _new_data_text.move_to(_data_text.get_center())
                self.remove(_data_text)
                _data_text = _new_data_text
            self.play(FadeOut(_arrow))
            self.remove(_arrow)
            _arrow = Arrow(_data_text.get_center(), _hash_key.get_center(), buff=0.1, color=BLUE)
            return _data_text, _hash_key, _arrow

        for data in [45, 32]:
            data_text, hash_key, arrow = find_data(data)
            temp_text = Text(f"{data} 等于 {data}，查找成功！", font="Microsoft YaHei").move_to(hash_key)
            group = VGroup(data_text, hash_key)
            self.play(Create(arrow), ReplacementTransform(group, temp_text))
            self.wait(1)
            self.play(FadeOut(arrow), FadeOut(temp_text))
            self.remove(arrow, temp_text)

        data_text, hash_key, arrow = find_data(7)
        self.remove(data_text)
        temp_text = Text(f"哈希表7处位置为空，查找失败！", font="Microsoft YaHei").move_to(hash_key)
        self.play(Create(arrow), ReplacementTransform(hash_key, temp_text))
        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(temp_text))
        self.remove(arrow, temp_text)

        data_text, hash_key, arrow = find_data(12)
        temp_text = Text(f"哈希表4处位置不为空，但是不等于12，查找失败！", font="Microsoft YaHei",
                         font_size=30).move_to(hash_key)
        self.play(Create(arrow), ReplacementTransform(VGroup(data_text, hash_key), temp_text))
        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(temp_text))
        self.remove(arrow, temp_text)
        self.wait(2)

        self.play(FadeOut(hash_info), FadeOut(hash_table),
                  *[FadeOut(data_text) for data_text in data_texts[:5]])
        self.remove(*set(self.mobjects) - {self.title})

    def transposition_table(self):
        temp_text = Text("置  换  表", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(temp_text))
        self.wait(1)
        text = MarkupText('说完了哈希表的基本原理，我们是时候回过头来看看置换表了\n'
                          '置换表的原理和哈希表非常相似，我们可以把置换表看作是哈希表的一个特例\n'
                          '还记得之前那3点吗，我们现在看看置换表的情况吧',
                          font="Microsoft YaHei", font_size=30)
        self.play(FadeOut(temp_text), GrowFromCenter(text))
        self.wait(8)
        self.play(FadeOut(text))

        temp_text = Text("置 换 表 的 哈 希 函 数", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(temp_text))
        self.wait(1)
        self.play(FadeOut(temp_text))
        text = MarkupText('相比于之前的哈希表，置换表的哈希函数是：'
                          f'<span foreground="{BLUE}">'
                          '<big>hash(局面) = Zobrist(局面) % 置换表项数\n</big></span>'
                          '大家其实可以看到，这和哈希表的哈希函数大同小异，只是多了一些额外的操作\n\n'
                          '置换表大小（大家平时设置的那个值）= 置换表项数 * 置换表项大小\n'
                          '置换表大小一般是2的幂次方，比如16M，256M，512M等等\n\n'
                          '大家会注意到，象棋的局面是无法直接传入hash函数计算的，因为象棋的局面并不是一个整数\n'
                          '因此，我们必须通过某种方式把局面转换为一个整数，并且保证每个局面都对应唯一的一个整数\n\n'
                          f'而进行这个转换的算法，就是 <span foreground="{BLUE}">'
                          '<big>Zobrist哈希法</big></span>',
                          font="Microsoft YaHei", font_size=23)
        self.play(Write(text), run_time=4)
        self.wait(8)

        temp_text = MarkupText("那什么是Zobrist哈希法呢xwx？\n"
                               "什么是Zobrist查询表呢xwx？\n"
                               "如何计算一个局面对应的Zobrist值呢xwx？\n"
                               "喵喵喵qwq？", font="Microsoft YaHei")
        self.play(Transform(text, temp_text))
        self.wait(5)

        temp_text = MarkupText("生成Zobrist查询表", font="Microsoft YaHei")
        self.play(Transform(text, temp_text))
        self.play(text.animate.shift(UP * 2.2))
        temp_text = MarkupText("Zobrist查询表是一个二维数组，第一维是棋子位置，第二维是棋子类型\n"
                               "查询表中一共有是90 * 14个元素（90个格子，14种棋子）\n"
                               "每个元素都是一个随机生成的64位整数\n"
                               "对于棋盘上的每个位置，每种棋子都有其对应的一个随机数\n"
                               "除此以外，还需要额外生成一个'当前局面轮到黑方走子'的随机数",
                               font="Microsoft YaHei", font_size=30)
        self.play(DrawBorderThenFill(temp_text))
        self.wait(4)
        self.play(FadeOut(text), Uncreate(temp_text))

        # draw a xiangqi palace on the left side of the screen
        chess_board = VGroup(*[Rectangle(width=1, height=1) for _ in range(4)])
        chess_board.arrange_in_grid(n_rows=2, n_cols=2, buff=0)
        chess_board.add(Line(UL, DR), Line(UR, DL),
                        Text("部分象棋棋盘", font="Microsoft YaHei", font_size=26)
                        .move_to(DOWN * 1.5))
        self.play(Create(chess_board))
        self.play(chess_board.animate.shift(LEFT * 5))

        # draw a random number generator on the right side of the screen
        random_number_generator = ImageMobject("images/random_number_generator.png")
        generator_text = Text("随只因数生成器", font="Microsoft YaHei", font_size=26) \
            .next_to(random_number_generator, DOWN)
        generator_text.add_updater(lambda m: m.next_to(random_number_generator, DOWN))
        self.play(FadeIn(random_number_generator), Create(generator_text))
        self.play(random_number_generator.animate.scale(0.5).shift(RIGHT * 5))

        special_knight_hash = 0

        for index, pos in [(0, UL), (3, UL), (3, DR)]:
            zobrist_text = MarkupText("车：\n"
                                      "马：\n"
                                      "炮：\n"
                                      "...",
                                      font="Microsoft YaHei", font_size=30).move_to(LEFT * 2)
            arrow = Arrow(chess_board[index].get_corner(pos), zobrist_text.get_corner(LEFT),
                          color=BLUE, buff=0.1)
            self.play(Create(zobrist_text), Create(arrow))
            self.wait(1)
            random_numbers = []
            for i in range(3):
                # generate random number on the top of the generator
                random_hash = random.randint(0, 2 ** 64 - 1)
                if index == 0 and i == 1:
                    special_knight_hash = random_hash
                random_number = Text(f'0x{random_hash:016x}',
                                     font="Microsoft YaHei", font_size=30) \
                    .move_to(random_number_generator.get_top() + UP)
                random_numbers.append(random_number)
                self.play(GrowFromCenter(random_number))
                # move the random number to the zobrist text
                if i == 0:
                    self.play(random_number.animate.move_to(zobrist_text[i * 2 + 1]
                                                            .get_corner(RIGHT) + RIGHT * 2.5
                                                            + UP * 0.05))
                else:
                    self.play(random_number.animate.move_to(zobrist_text[i * 2 + 1]
                                                            .get_corner(RIGHT) + RIGHT * 2.5 +
                                                            UP * 0.05))
                    self.play(random_number.animate.align_to(random_numbers[i - 1], LEFT))
            self.wait(2)
            self.play(FadeOut(zobrist_text), FadeOut(arrow), *[FadeOut(num) for num in random_numbers])

        # generate the random number for side to move
        stm_hash = random.randint(0, 2 ** 64 - 1)
        stm_text = Text(f'轮到黑方走棋：0x{stm_hash:016x}', font="Microsoft YaHei", font_size=26) \
            .move_to(random_number_generator.get_top() + UP)
        self.play(GrowFromCenter(stm_text))
        self.play(stm_text.animate.move_to(0))
        self.wait(2)
        self.play(FadeOut(chess_board), FadeOut(random_number_generator), FadeOut(generator_text),
                  FadeOut(stm_text))

        text = Text("计算局面对应的Zobrist值", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(text))
        self.play(text.animate.shift(UP * 2.2))
        temp_text = MarkupText("对于棋盘上的每一个棋子，都在刚才生成的Zobrist查询表中找到对应的随机数\n"
                               "然后将这些随机数进行异或运算，得到的结果就是局面对应的Zobrist值\n"
                               "值得注意的是，如果当前局面轮到黑方走子，那么需要多异或一个'轮到黑方走子'\n"
                               "的随机数，因为当前局面是轮到红方还是轮到黑方走棋显然是两个不同的局面\n"
                               "即使两个局面中同样的棋子在相同的位置",
                               font="Microsoft YaHei", font_size=30)
        self.play(DrawBorderThenFill(temp_text))
        self.wait(4)
        self.play(FadeOut(text), Uncreate(temp_text))

        self.play(Create(chess_board))
        side_to_move_text = Text("轮到红方行棋", font="Microsoft YaHei")
        self.play(GrowFromCenter(side_to_move_text))
        self.wait(1)
        self.play(FadeOut(side_to_move_text))
        # draw a "马" and a "炮" on the chess board
        knight = Text("马", font="Microsoft YaHei", font_size=30).move_to(chess_board[0].get_corner(UL))
        border = Circle(color=WHITE, fill_color=RED, fill_opacity=.5, radius=.3) \
            .move_to(knight.get_center())
        knight = VGroup(knight, border)
        cannon = Text("炮", font="Microsoft YaHei", font_size=30).move_to(chess_board[1].get_corner(UR))
        border = Circle(color=WHITE, fill_color=RED, fill_opacity=.5, radius=.3) \
            .move_to(cannon.get_center())
        cannon = VGroup(cannon, border)
        self.play(Create(knight), Create(cannon))

        key = 0
        pos_hash = Text(f"0x{key:016x}", font="Microsoft YaHei", font_size=30)
        text = Text(f"局面key = ", font="Microsoft YaHei", font_size=30)
        text = VGroup(text, pos_hash).arrange(RIGHT).shift(DOWN * 3)
        self.play(Write(text))

        def update_key(_index, _pos, copy):
            nonlocal temp_text, key, arrow, text
            temp_text = Text("查询刚才生成的Zobrist查询表", font="Microsoft YaHei", font_size=30)
            self.play(Write(temp_text))
            self.wait(1)
            arrow = Arrow(chess_board[_index].get_corner(_pos), temp_text.get_corner(LEFT), color=BLUE)
            if _index == 0:
                hash_val = special_knight_hash
            else:
                hash_val = random.randint(0, 2 ** 64 - 1)
            value = Text(f"0x{hash_val:016x}", font="Microsoft YaHei", font_size=30)
            self.play(Create(arrow))
            self.play(ReplacementTransform(VGroup(temp_text, copy), value))
            self.wait(1)
            self.play(FadeOut(arrow), text[1].animate.next_to(value, DOWN))
            # 展示pos_hash和value的异或运算
            xor_text = Text("异或运算！xor！", font="Microsoft YaHei", font_size=30).shift(UP * 2)
            self.play(Write(xor_text))
            self.wait(1)
            key ^= hash_val
            result = Text(f"0x{key:016x}", font="Microsoft YaHei", font_size=30)
            self.play(ReplacementTransform(VGroup(text[1], value), result))
            self.wait(1)
            self.play(FadeOut(xor_text), result.animate.next_to(text[0], RIGHT))
            text[1] = result

        # calculate the zobrist value
        for index, pos in [(0, UL), (1, UR)]:
            update_key(index, pos, knight.copy() if index == 0 else cannon.copy())

        self.play(FadeOut(chess_board), FadeOut(knight), FadeOut(cannon), FadeOut(text))
        text2 = Text("走子时局面Zobrist值的更新", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(text2))
        self.play(text2.animate.shift(UP * 2.2))
        temp_text = MarkupText("基于异或的可逆性，可以通过异或运算来更新局面的Zobrist值\n"
                               "走子时，只需要异或子力远离的位置的Zobrist，再异或子力去到的位置的Zobrist即可\n"
                               "如果有子力被吃掉，那么还需要再异或被吃掉子力的Zobrist\n"
                               "同样的，因为走子之后局面的行动方交换，所以需要异或'当前是否轮到黑方行棋'\n"
                               "这样就可以在O(1)的时间内更新局面的Zobrist值了",
                               font="Microsoft YaHei", font_size=26)
        self.play(DrawBorderThenFill(temp_text))
        self.wait(8)
        self.play(FadeOut(text2), Uncreate(temp_text))

        self.play(Create(chess_board), Create(knight), Create(cannon), Create(text))
        # move the knight to the bottom of the board
        arrow = Arrow(knight.get_center(), chess_board[2].get_corner(DR), color=BLUE)
        self.play(Create(arrow))
        self.wait(1)
        self.play(FadeOut(arrow), knight.animate.move_to(chess_board[2].get_corner(DR)))
        update_key(0, UL, Text(""))
        update_key(2, DR, knight.copy())
        self.wait(1)
        # update the side to move
        temp_text = Text("此时轮到黑方行棋了，是不是应该做些什么呢？", font="Microsoft YaHei", font_size=24)
        self.play(GrowFromCenter(temp_text))
        self.wait(2)
        stm_text = Text(f"轮到黑方走棋：0x{stm_hash:016x}", font="Microsoft YaHei", font_size=30)
        self.play(ReplacementTransform(temp_text, stm_text))
        self.wait(1)
        self.play(text[1].animate.next_to(stm_text, DOWN))
        key ^= stm_hash
        result_hash = Text(f"0x{key:016x}", font="Microsoft YaHei", font_size=30)
        self.play(ReplacementTransform(VGroup(text[1], stm_text), result_hash))
        self.wait(1)
        self.play(result_hash.animate.next_to(text[0], RIGHT))
        text[1] = result_hash
        self.wait(2)
        self.play(FadeOut(chess_board), FadeOut(knight), FadeOut(cannon), FadeOut(text))

        text = Text("置换表的存储结构", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(text))
        self.play(text.animate.shift(UP * 2.3))
        temp_text = MarkupText("置换表的每一个置换表项存储有：\n"
                               "局面的key值，局面评估值，以及做出这个评估时所处的搜索深度",
                               font="Microsoft YaHei", font_size=30).shift(UP * 1.2)
        code = Code(code="struct TranspositionTableEntry {\n\n"
                         "    uint64_t key; // 局面计算出来的Zobrist值\n\n"
                         "    int score; // 对于这个局面的评分\n\n"
                         "    int depth; // 这个评分是几层时做出来的\n\n"
                         "};", font="Microsoft YaHei", font_size=30, language="cpp", style="colorful") \
            .next_to(temp_text, DOWN)
        self.play(DrawBorderThenFill(temp_text), DrawBorderThenFill(code))
        self.wait(8)
        self.play(FadeOut(text), Uncreate(temp_text), Uncreate(code))

        text = Text("置换表的置换策略", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(text))
        self.play(text.animate.shift(UP * 2.3))
        temp_text = MarkupText("置换表的置换策略主要是基于深度优先的始终替换策略：\n"
                               "1. 如果局面对应的置换表项为空，那么直接将局面信息存入置换表\n"
                               "2. 如果局面对应的置换表项不为空，那么需要判断当前局面与置换表中的局面\n"
                               "    的搜索深度，如果当前局面的搜索深度大于等于置换表中的搜索深度，那么\n"
                               "    将当前局面的信息存入置换表，否则不做任何操作\n",
                               font="Microsoft YaHei", font_size=30).next_to(text, DOWN)
        self.play(DrawBorderThenFill(temp_text))
        self.wait(8)
        new_text = Text("大家思考一下，这样做是合理的吗？有无不合理之处呢？",
                        font="Microsoft YaHei", font_size=30)
        self.play(Transform(temp_text, new_text))
        self.wait(4)
        new_text = MarkupText("其实看似合理的做法之中往往暗藏危机，大家可以稍作思考，如果不进行干预会发生什么\n"
                              "随着搜索的进行，置换表中很快就会充斥满高层搜索的老旧局面\n"
                              "而新搜索局面的因为层数过低无法进入置换表，出现了计算机中常见的饿死现象\n\n"
                              "解决方案有两种：\n"
                              f'<span foreground="{BLUE}">'
                              "1. 每次搜索前清空置换表</span>\n"
                              f'<span foreground="{BLUE}">'
                              "2. 每次搜索前将置换表中的所有局面的搜索深度减2，如果深度小于等于0，则清空该表项"
                              "</span>",
                              font="Microsoft YaHei", font_size=26).next_to(text, DOWN)
        self.play(Transform(temp_text, new_text))
        self.wait(10)
        self.play(FadeOut(text), Uncreate(temp_text))

        text = Text("置换表的查找", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(text))
        self.play(text.animate.shift(UP * 2.3))
        temp_text = MarkupText("置换表的查找主要是基于局面的key值，通过key值可以快速定位到局面对应的置换表项\n"
                               "1. 如果局面对应的置换表项为空，那么直接返回置换表不命中，继续局面搜索\n"
                               "2. 如果局面对应的置换表项不为空，那么需要判断当前局面与置换表中的局面的key是\n"
                               "    否相同，如果不同，那么依然为置换表不命中，继续局面搜索\n"
                               "3. 如果局面key相同，这时需要判断当前局面的搜索深度是否大于置换表中的搜索深度\n"
                               "    如果大于，那么依然为置换表不命中，继续局面搜索\n"
                               "4. 如果局面key相同，且当前局面的搜索深度小于等于置换表中的搜索深度，那么置换\n"
                               "    表命中，直接返回置换表中的分数，表明该局面已经在同层或高层搜索过，无需再\n"
                               "    次搜索",
                               font="Microsoft YaHei", font_size=26).next_to(text, DOWN)
        self.play(DrawBorderThenFill(temp_text))
        self.wait(14)

        annoying_image = ImageMobject("images/annoying.jpg").scale(0.4).shift(DOWN)
        self.play(Transform(text, Text("动画呢？我的动画呢QAQ？", font="Microsoft YaHei",
                                       font_size=30).move_to(text)),
                  FadeIn(annoying_image), FadeOut(temp_text))
        self.wait(3)
        self.play(FadeOut(annoying_image), Uncreate(text))
        self.remove(annoying_image)

        text = Text("置换表的填充、替换", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(text))
        self.wait(1)
        self.play(FadeOut(text))
        # draw the transposition table in the center of the screen and shift to the right
        tt = VGroup(*[VGroup(Rectangle(width=3, height=1, fill_opacity=0, stroke_width=8),
                             Text(str(i), font="Microsoft YaHei", font_size=30))
                    .arrange(RIGHT) for i in range(4)]).arrange(DOWN)
        for i in range(1, 4):
            tt[i].align_to(tt[i - 1], LEFT)
        tt_value = [Text("[  ]", font="Microsoft YaHei", font_size=30)
                    .move_to(tt[i][0].get_center() + RIGHT * 5) for i in range(4)]
        tt_border = SurroundingRectangle(tt, buff=0.2, color=BLUE, corner_radius=0.1)
        tt_text = Text("置换表[局面key|深度|分数]", font="Microsoft YaHei", font_size=26) \
            .next_to(tt_border, DOWN)
        self.play(DrawBorderThenFill(tt), DrawBorderThenFill(tt_text), DrawBorderThenFill(tt_border))
        tt = VGroup(tt, tt_text, tt_border)
        self.play(tt.animate.shift(RIGHT * 5))
        self.play(*[DrawBorderThenFill(tt_value[i]) for i in range(4)])

        # draw a chess engine searching on the left
        engine_text = Text("Pikafish", font="Microsoft YaHei")
        engine = SurroundingRectangle(engine_text, buff=0.2, color=BLUE, corner_radius=0.3)
        engine_key = Text("当前局面key  ：", font="Microsoft YaHei", font_size=30) \
            .next_to(engine, DOWN).align_to(engine, LEFT)
        engine_key_value = Text("0", font="Microsoft YaHei", font_size=30) \
            .next_to(engine_key, RIGHT, buff=1)
        engine_depth = Text("当前搜索深度：", font="Microsoft YaHei", font_size=30) \
            .next_to(engine_key, DOWN).align_to(engine_key, LEFT)
        engine_depth_value = Text("0", font="Microsoft YaHei", font_size=30) \
            .next_to(engine_depth, RIGHT, buff=1).align_to(engine_key_value, LEFT)
        engine_score = Text("当前局面分数：", font="Microsoft YaHei", font_size=30) \
            .next_to(engine_depth, DOWN).align_to(engine_depth, LEFT)
        engine_score_value = Text("0", font="Microsoft YaHei", font_size=30) \
            .next_to(engine_score, RIGHT, buff=1).align_to(engine_depth_value, LEFT)
        engine = VGroup(engine, engine_text, engine_key, engine_key_value,
                        engine_depth, engine_depth_value,
                        engine_score, engine_score_value)
        self.play(DrawBorderThenFill(engine), run_time=2)
        self.play(engine.animate.shift(LEFT * 5))

        # yield out a position from the engine
        def yield_pos(_key, depth, score, replace=True, empty=True):
            nonlocal engine_depth_value, engine_key_value, engine_score_value
            _temp = [Text(f"0x{_key:x}", font="Microsoft YaHei", font_size=30).move_to(engine_key_value),
                     Text(str(depth), font="Microsoft YaHei", font_size=30).move_to(engine_depth_value),
                     Text(str(score), font="Microsoft YaHei", font_size=30).move_to(engine_score_value)]
            for _i in range(1, 3):
                _temp[_i].align_to(_temp[_i - 1], LEFT)
            self.play(Transform(engine_key_value, _temp[0]),
                      Transform(engine_depth_value, _temp[1]),
                      Transform(engine_score_value, _temp[2]))
            self.wait(1)
            # put the value to the transposition table
            _temp = MarkupText(f'hash(当前局面)\n'
                               f'= Zobrist(当前局面)  %  置换表项数\n'
                               f'= 0x{_key:x}  %  0x4 = {_key % 4}',
                               font="Microsoft YaHei", font_size=30).shift(UP * 2 + LEFT)
            self.play(Write(_temp))
            self.wait(1)
            _arrow = Arrow(engine.get_right(), tt_value[_key % 4].get_center() + LEFT * 1.7,
                           color=BLUE, buff=0.1)
            self.play(Create(_arrow))
            self.wait(1)
            if replace:
                if empty:
                    _text = MarkupText(f'基于深度优先的始终替换策略：\n'
                                       f'当前置换表[{_key % 4}]处为空\n'
                                       '更新置换表', font="Microsoft YaHei", font_size=30) \
                        .move_to(_temp)
                    self.play(Transform(_temp, _text))
                else:
                    _text = MarkupText(f'基于深度优先的始终替换策略：\n'
                                       f'当前搜索深度 &gt;= 置换表[{_key % 4}]处的深度\n'
                                       '更新置换表', font="Microsoft YaHei", font_size=30) \
                        .move_to(_temp)
                    self.play(Transform(_temp, _text))
                self.wait(3)
                _text = Text(f"置换表[{_key % 4}] = [0x{_key:x} | {depth} | {score}]",
                             font="Microsoft YaHei", font_size=30).shift(UP * 2 + LEFT)
                self.play(Transform(_temp, _text))
                self.wait(1)
                _text = Text(f'[0x{_key:x} | {depth} | {score}]', font="Microsoft YaHei",
                             font_size=30).move_to(tt_value[_key % 4])
                self.play(Transform(tt_value[_key % 4], _text))
            else:
                _text = MarkupText(f'基于深度优先的始终替换策略：\n'
                                   f'当前搜索深度 &lt; 置换表[{_key % 4}]处的深度\n'
                                   '不更新置换表', font="Microsoft YaHei", font_size=30) \
                    .move_to(_temp)
                self.play(Transform(_temp, _text))
                self.wait(2)
            self.play(FadeOut(_arrow), FadeOut(_temp))
            self.wait(1)

        yield_pos(0x12, 5, 300)
        yield_pos(0x10, 4, 200)
        yield_pos(0x12, 2, -10, replace=False)
        yield_pos(0x11, 3, 100)
        yield_pos(0x16, 7, 400, empty=False)
        self.wait(2)
        self.play(FadeOut(engine), FadeOut(tt), *[FadeOut(tt_value[i]) for i in range(4)])

        text = Text("置换表的衰减、查询", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(text))
        self.wait(1)
        self.play(FadeOut(text))
        self.play(Create(engine), Create(tt), *[Create(tt_value[i]) for i in range(4)])
        self.wait(1)

        text = Text('新一轮搜索，衰减！', font="Microsoft YaHei", font_size=32)
        self.wait(1)
        self.play(Write(text))
        temp = [Text('[0x10 | 2 | 200]', font="Microsoft YaHei", font_size=30).move_to(tt_value[0]),
                Text('[0x11 | 1 | 100]', font="Microsoft YaHei", font_size=30).move_to(tt_value[1]),
                Text('[0x16 | 5 | 400]', font="Microsoft YaHei", font_size=30).move_to(tt_value[2])]
        self.play(*[Transform(tt_value[i], temp[i]) for i in range(3)])
        self.play(Unwrite(text))

        def query_pos(_key, depth, score=0, use=True, key_diff=False, empty=False):
            nonlocal engine_depth_value, engine_key_value, engine_score_value
            _temp = [Text(f"0x{_key:x}", font="Microsoft YaHei", font_size=30).move_to(engine_key_value),
                     Text(str(depth), font="Microsoft YaHei", font_size=30).move_to(engine_depth_value),
                     Text('？', font="Microsoft YaHei", font_size=30).move_to(engine_score_value)]
            for _i in range(1, 3):
                _temp[_i].align_to(_temp[_i - 1], LEFT)
            self.play(*[Transform(_i, j) for _i, j in
                        zip([engine_key_value, engine_depth_value, engine_score_value], _temp)])
            self.wait(1)
            # query the value from the transposition table
            _temp = MarkupText(f'hash(当前局面)\n'
                               f'= Zobrist(当前局面)  %  置换表项数\n'
                               f'= 0x{_key:x}  %  0x4 = {_key % 4}',
                               font="Microsoft YaHei", font_size=30).shift(UP * 2 + LEFT)
            self.play(Write(_temp))
            self.wait(1)
            _arrow = Arrow(tt_value[_key % 4].get_center() + LEFT * 1.7, engine.get_right(),
                           color=BLUE, buff=0.1)
            self.play(Create(_arrow))
            self.wait(1)
            if not use:
                if empty:
                    _text = MarkupText(f'当前置换表[{_key % 4}]处为空\n'
                                       '置换表不命中', font="Microsoft YaHei", font_size=30) \
                        .move_to(_temp)
                elif key_diff:
                    _text = MarkupText(f'当前置换表[{_key % 4}]处的局面与当前局面不同\n'
                                       '置换表不命中', font="Microsoft YaHei", font_size=30) \
                        .move_to(_temp)
                else:
                    _text = MarkupText(f'局面key相同\n但当前搜索深度 &gt; 置换表[{_key % 4}]处的深度\n'
                                       '置换表不命中', font="Microsoft YaHei", font_size=30) \
                        .move_to(_temp)
                self.play(Transform(_temp, _text))
                self.wait(2)
            else:
                _text = MarkupText(f'局面key相同\n且当前搜索深度 &lt;= 置换表[{_key % 4}]处的深度\n'
                                   '置换表命中', font="Microsoft YaHei", font_size=30) \
                    .move_to(_temp)
                self.play(Transform(_temp, _text))
                self.wait(2)
                # update the engine value
                _text = Text(str(score), font="Microsoft YaHei", font_size=30) \
                    .move_to(engine_score_value).align_to(engine_score_value, LEFT)
                self.play(Transform(engine_score_value, _text))
            self.play(FadeOut(_arrow), FadeOut(_temp))
            self.wait(1)

        query_pos(0x14, 4, use=False, key_diff=True)
        query_pos(0x13, 4, use=False, empty=True)
        query_pos(0x11, 3, use=False)
        query_pos(0x16, 4, 400, use=True)
        self.play(FadeOut(engine), FadeOut(tt), *[FadeOut(tt_value[i]) for i in range(4)])
        self.wait(2)

    def tt_usage(self):
        text = Text("置换表的作用（单线程）", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(text))
        self.play(text.animate.shift(UP * 2.3))
        temp_text = MarkupText('置换表在单个线程中发挥着以下的作用：\n'
                               '1. 重复局面的搜索结果可以直接从置换表中取出，不需要重新搜索\n'
                               '2. 迭代加深搜索（逐层增加深度）时，前面深度搜索的走法可以为\n'
                               '    加速下一次迭代加深搜索的减枝流程提供信息。\n\n'
                               '注意：前面为了演示方便，我们并没有把pv走法存储到置换表中，但\n'
                               '      是，在实际的搜索中，我们会把pv走法存储到置换表中，只要当前\n'
                               '      局面key与置换表中的局面key对应，即使深度不满足要求，也可以\n'
                               '      返回置换表项中的pv走法，先尝试走走之前搜索过的最好的pv走法，\n'
                               '      从而加速整个alpha-beta搜索减枝流程。\n\n',
                               font="Microsoft YaHei", font_size=26).shift(DOWN)
        self.play(Write(temp_text))
        self.wait(14)
        temp_text_2 = MarkupText('除此以外，置换表对于胜利分数(±31754 - ±32000)和TB分数的处理与\n'
                                 '普通分数的处理流程也是不尽相同的，关于这些分数是如何存储在置换表\n'
                                 '中的，以及对于这些分数在探测置换表时所需要的层数要求，就留给大家\n'
                                 '自己研究辣\n\n'
                                 '本视频中的绝大部分内容都是简化后的情形，便于理解，实际上，置换表\n'
                                 '里面的门道是非常多的，远不止视频中呈现出来的这些，想利用好这一件\n'
                                 '兵器，绝非易事qwq\n',
                                 font="Microsoft YaHei", font_size=30).move_to(temp_text)
        self.play(Transform(temp_text, temp_text_2))
        self.wait(14)
        self.play(FadeOut(text), FadeOut(temp_text))
        self.wait(1)

        text = Text('走 法 " 置 换 "', font="Microsoft YaHei")
        temp_text = MarkupText('在实际搜索过程中，会遇到很多重复的局面，置换表的诞生就是用于解决这一问题的。\n'
                               '所谓置换，也就是通过不同的走法顺序，或者走子方式，到达同一个局面，我们称之为\n'
                               '“置换”。这也是置换表名称的由来，出现这些情况时，我们就可以复用以前存储在置换\n'
                               '表中的结果了，不必再次浪费时间搜索。', font="Microsoft YaHei", font_size=26)
        self.play(DrawBorderThenFill(text))
        self.play(text.animate.shift(UP * 2.3))
        self.play(Write(temp_text))
        self.wait(12)
        self.play(FadeOut(text), FadeOut(temp_text))

        def show_transposition(before, after, seq1, seq2):
            before_move = ImageMobject(before).shift(LEFT * 5)
            self.play(FadeIn(before_move))

            def get_seq(seq, direction):
                move_seq = MarkupText(seq, font="Microsoft YaHei", font_size=30).shift(direction * 2)
                _border = SurroundingRectangle(move_seq, buff=0.1, corner_radius=0.1)
                _arrow = Arrow(before_move.get_right(), move_seq.get_left(), color=BLUE)
                return VGroup(move_seq, _border), _arrow

            move_seq1, arrow1 = get_seq(seq1, UP)
            move_seq2, arrow2 = get_seq(seq2, DOWN)

            self.play(Write(move_seq1), Write(move_seq2), Create(arrow1), Create(arrow2))
            self.wait(2)
            after_move = ImageMobject(after).shift(RIGHT * 5)
            arrow3 = Arrow(move_seq1.get_right(), after_move.get_left(), color=BLUE)
            arrow4 = Arrow(move_seq2.get_right(), after_move.get_left(), color=BLUE)
            self.play(FadeIn(after_move), Create(arrow3), Create(arrow4))
            self.wait(6)
            pos_old = [move_seq1.get_center(), move_seq2.get_center()]
            double_side_arrow = [Arrow(move_seq1.get_bottom(), move_seq2.get_top(), color=GREEN)
                                 .shift(LEFT * 0.3),
                                 Arrow(move_seq2.get_top(), move_seq1.get_bottom(), color=GREEN)
                                 .shift(RIGHT * 0.3)]
            self.play(*[Create(_i) for _i in double_side_arrow])
            self.wait(1)
            self.play(move_seq1.animate.move_to(pos_old[1]),
                      move_seq2.animate.move_to(pos_old[0]))
            self.wait(2)
            self.play(move_seq1.animate.move_to(pos_old[0]),
                      move_seq2.animate.move_to(pos_old[1]))
            self.wait(2)
            self.play(*[FadeOut(_i) for _i in [move_seq1, move_seq2, arrow1, arrow2, arrow3, arrow4,
                                               before_move, after_move, *double_side_arrow]])

        show_transposition('images/before1.jpg', 'images/after1.jpg',
                           '1. 马六进八 炮4平3\n2. 马五进三 炮5平6',
                           '1. 马五进三 炮5平6\n2. 马六进八 炮4平3')
        show_transposition('images/before2.jpg', 'images/after2.jpg',
                           '1. 马五进六 将4平5\n2. 马六进五 将5平4',
                           '1. 马五进四 将4平5\n2. 马四进五 将5平4')

        text = Text('迭代加深中置换表的作用', font="Microsoft YaHei")
        self.play(DrawBorderThenFill(text))
        self.wait(1)
        self.play(FadeOut(text))

        position = ImageMobject('images/position.jpg').scale(.9).shift(LEFT * 4.5 + DOWN * 0.5)
        tt = Rectangle(width=3, height=1, fill_opacity=0, stroke_width=8)
        tt_text = Text('0 | 空', font="Microsoft YaHei", font_size=30).move_to(tt)
        tt_label = MarkupText('置换表[深度|PV]', font="Microsoft YaHei", font_size=30).next_to(tt, DOWN)
        tt = VGroup(tt, tt_text, tt_label)
        border = SurroundingRectangle(tt, buff=0.2, corner_radius=0.1, color=BLUE)
        tt = VGroup(tt, border)
        tt.shift(RIGHT * 5 + UP * 2.5)
        self.play(FadeIn(position), DrawBorderThenFill(tt))
        self.wait(2)

        search_results = ['深度:1 己分:7 时间:0.0 NPS:157K (0)\n'
                          '炮八平五',
                          '深度:2 己分:21 时间:0.0 NPS:318K (0)\n'
                          '炮二平五',
                          '深度:3 己分:27 时间:0.0 NPS:517K (0)\n'
                          '炮八平五',
                          '深度:4 己分:218 时间:0.0 NPS:554K (0)\n'
                          '炮八平五',
                          '深度:5 己分:31 时间:0.0 NPS:1234K (0)\n'
                          '炮八平五 炮２平５ 马八进七 马２进３',
                          '深度:6 己分:27 时间:0.0 NPS:1721K (0)\n'
                          '炮二平五 炮２平５ 马二进三 马２进３ 马八进七',
                          '深度:7 己分:29 时间:0.0 NPS:2034K (0)\n'
                          '炮二平五 炮２平５ 马八进七 马２进３ 马二进三',
                          '深度:8 己分:26 时间:0.0 NPS:2634K (0)\n'
                          '炮八平五 马８进７ 马八进七 炮２平５ 车九平八\n马２进３ 马二进三',
                          '深度:9 己分:18 时间:0.0 NPS:3064K (0)\n'
                          '炮八平五 马２进３ 兵三进一 卒３进１ 马八进七\n马８进７ 马二进三 车１平２']

        def search(depth):
            nonlocal position
            runtime = 1 if depth < 3 else 0.1
            tip = MarkupText(f'当前深度为：{depth}，查询置换表', font="Microsoft YaHei", font_size=26) \
                .to_corner(UL)
            self.play(Write(tip), run_time=runtime)
            _arrow = Arrow(tt.get_left(), position.get_right(), color=BLUE)
            self.play(Create(_arrow), run_time=runtime)
            self.wait(runtime)
            if depth == 1:
                __text = MarkupText('置换表中没有该局面，继续搜索', font="Microsoft YaHei", font_size=26) \
                    .to_corner(UL)
                self.play(Transform(tip, __text), run_time=runtime)
                self.wait(runtime * 2)
            else:
                __text = MarkupText('置换表中有该局面，但是深度不满足条件\n'
                                    '返回记录的pv走法，搜索时先尝试该走法',
                                    font="Microsoft YaHei", font_size=26).to_corner(UL)
                self.play(Transform(tip, __text), run_time=runtime)
                self.wait(runtime * 2)
            tt_pv = tt_text[2:].copy()
            self.play(tt_pv.animate.move_to(position.get_bottom() + DOWN * 0.5), run_time=runtime)
            self.wait(runtime)
            self.play(Uncreate(_arrow), FadeOut(tip), run_time=runtime)
            __text = MarkupText(search_results[depth - 1], font="Microsoft YaHei", font_size=26) \
                .to_corner(DR)
            self.play(Transform(tt_pv, __text), run_time=runtime)
            self.wait(runtime * 2)

            __text = MarkupText('搜索完成，把pv走法保存到置换表', font="Microsoft YaHei", font_size=26) \
                .to_corner(UL)
            self.play(Create(__text), run_time=runtime)
            self.wait(runtime)
            _arrow = Arrow(tt_pv.get_top(), tt.get_bottom(), color=BLUE, buff=0.1)
            self.play(Create(_arrow), run_time=runtime)
            self.wait(runtime)
            new_tt_pv = Text(str(depth) + ' | ' + search_results[depth - 1].split('\n')[1][:4],
                             font="Microsoft YaHei", font_size=30).move_to(tt_text)
            self.play(Transform(tt_text, new_tt_pv), run_time=runtime)
            self.wait(runtime)
            self.play(Uncreate(_arrow), Uncreate(__text), Uncreate(tt_pv), run_time=runtime)
            self.wait(runtime)

        self.play(FadeOut(self.title))
        for i in range(1, 10):
            search(i)
        self.play(FadeOut(tt), FadeOut(position))
        self.play(FadeIn(self.title))

        text = Text("置换表的作用（多线程）", font="Microsoft YaHei")
        self.play(DrawBorderThenFill(text))
        self.play(text.animate.shift(UP * 2.3))
        temp_text = MarkupText('置换表在多线程中发挥着以下的作用：\n'
                               '多个线程同时从同一局面出发，共享使用置换表，每个线程都会在置换表中查找局面\n'
                               '如果找到了，就不用再搜索了。如果没有找到，就把搜索结果保存到置换表中，供其\n'
                               '他线程使用。\n'
                               '理想状态下相当于多个线程同时遍历搜索树，并且各司其职，一个工程多个人完成\n'
                               '每个人都有自己的任务，互不干扰，这样就可以大大提高搜索的速度，减少搜索的时间\n'
                               '这就是Lazy-SMP的基本思想，基于置换表的多线程方案',
                               font="Microsoft YaHei", font_size=26).shift(DOWN)
        self.play(Write(temp_text))
        self.wait(14)
        temp_text_2 = MarkupText('实际上，多线程并非理想中的如此美好，由于各个线程之间只有置换表\n'
                                 '这一个交换信息的地方，很有可能一个线程正在搜索某些位置，还没搜\n'
                                 '完，没把信息放入置换表，另一个线程就过来查表了，结果没查到，又\n'
                                 '跑去搜索了同样的位置，这样就导致了多个线程的重复多余劳动',
                                 font="Microsoft YaHei", font_size=30).move_to(temp_text)
        self.play(Transform(temp_text, temp_text_2))
        self.wait(14)
        temp_text_2 = MarkupText('直观上，看似很多的重复劳动，效率低下，但从实测结果而言，Lazy-SMP\n'
                                 '效果非常好。于是产生了一种理论：Global TT, Private Heuristic\n'
                                 '也就是说，置换表是全局共享的，而各个线程的剪枝信息是各个线程独占的\n'
                                 '这样每个线程受到置换表的启发不同，也会导致各自的剪枝不同，最终导致\n'
                                 '搜索树高矮肥胖上的差异，换句话说，也就是拓宽了搜索树的搜索宽度\n'
                                 '拓宽了引擎的Horizon（眼界）',
                                 font="Microsoft YaHei", font_size=30).move_to(temp_text)
        self.play(Transform(temp_text, temp_text_2))
        self.wait(14)
        self.play(FadeOut(text), FadeOut(temp_text))
        self.wait(1)

        threads = VGroup()
        for i in range(4):
            _text = Text(f"线 程 {i}", font="Microsoft YaHei", font_size=30)
            border = SurroundingRectangle(_text, buff=0.2, corner_radius=0.2, color=BLUE)
            threads.add(VGroup(_text, border))
        threads.arrange(RIGHT, buff=2).shift(UP * 2)
        tt = Text("置  换  表", font="Microsoft YaHei", font_size=30) \
            .shift(DOWN * 2.3)
        border = SurroundingRectangle(tt, buff=0.2, corner_radius=0.2, color=BLUE)
        display_text = Text("多线程并发 随机读写置换表", font="Microsoft YaHei", font_size=30) \
            .next_to(border, DOWN, buff=0.5)
        tt = VGroup(tt, border, display_text)
        self.play(Write(threads), Write(tt))

        for i in range(10):
            # random select some threads
            _threads = random.sample(list(threads), random.randint(1, 4))
            arrows = []
            for thread in _threads:
                # random select read or write
                if random.random() < 0.5:
                    arrow = Arrow(tt.get_top(), thread.get_bottom(), color=BLUE)
                else:
                    arrow = Arrow(thread.get_bottom(), tt.get_top(), color=BLUE)
                arrows.append(arrow)
            runtime = i < 3 and 1 or 0.2
            self.play(*[Create(arrow, run_time=runtime) for arrow in arrows])
            self.wait(runtime)
            self.play(*[FadeOut(arrow, run_time=runtime) for arrow in arrows])

        self.play(FadeOut(threads), FadeOut(tt))
        self.wait(1)

        text = MarkupText('你说什么？Zobrist在象棋规则上的应用没讲？下次一定！\n',
                          font="Microsoft YaHei", font_size=30).shift(UP * 2)
        next_time = ImageMobject("images/next_time.png").scale(7).shift(DOWN)
        self.play(FadeIn(next_time), Write(text))
        self.wait(3)
        self.play(FadeOut(next_time), Uncreate(text))
        self.remove(next_time)

    def construct(self):
        self.hash_table()
        self.transposition_table()
        self.tt_usage()
