"""
附加题四
10*10格子
n条船，且不能重复，不能超出边界
三种类型：1*1(3) 2*2(3) 4*3(1)
10次击中就获得胜利；也可以再尝试玩一局
积分功能：1*1 5分；2*2 10分；4*3 20分
游戏结束时，提示游戏得分。
"""
from random import randint

# 10*10格子
board = []
for i in range(10):
    board.append(["O"]*10)
print(board)


def print_board(board_in):
    """
    子列表分行打印
    :param board_in: 由子列表组成的列表
    :return: 子列表
    """
    for row in board_in:
        # 针对列表中的元素，使用" "（空格）链接
        print(" ".join(row))


# board[2][2] = "x"
print_board(board)


def random_row(board_in):
    """
    随机行数
    :param board_in:列表
    :return: 随机行数
    """
    # randint(a, b) [a,b]
    row = randint(0, len(board_in)-1)
    return row


def random_col(board_in):
    """
    随机列数
    :param board_in:列表
    :return: 随机列数
    """
    col = randint(0, len(board_in[0])-1)
    return col


# 每条船生成的时候不管多大，都只取一个左上角；然后计算剩下的点位置并存储所有点的位置
# 每次生成新的船时,只要检查新船的所有点是否存储过


# 首次生成新船，存储；
# 再次生成新船时，判断之前是否生成过
# 一个格子
def ship(board_in):
    """
     1*1 一个格子：一条船或船的左上角
     :param board_in: list 地图
     :return:一个格子 tuple (row, col)
     """
    # row_col = []

    row = random_row(board_in)
    col = random_col(board_in)
    # row_col.append(row)
    # row_col.append(col)
    return row, col


# 一个船有m*n个格子，不能超出边界
def large_ship(board_in, m, n):
    """
    一条船：m*n
    :param board_in: list 地图
    :param m: 行
    :param n: 列
    :return: 船所在格子的列表 list 每一个格子用tuple表示
    """
    ss = []
    # 随机产生一条小船或大船的左上角 tuple
    r, c = ship(board_in)
    print(r, c)
    # 判断是否超出边界
    if r + m <= len(board_in) and c + n <= len(board_in):
        for i in range(r, r + m):
            for j in range(c, c + n):
                # s = []
                # s.append(i)
                # s.append(j)
                s = i, j
                ss.append(s)
        # return ss
    else:
        print("Notice: There is not enough space for such ship in the map!")
        # return ss
    return ss


# print(large_ship(board, 4, 3))


# 一条船与集合船是否重复的判断
def is_repeat(t, d):
    """
    判断船是否重复，若重复，返回True
    :param t:所有船的集合 list
    :param d:一条船 list
    :return: 重复的船 list
    有重复：len() > 0 ====True
    无重复：len() = 0 空列表 ====False
    """

    ss = []
    # e是m*n个格子 以船为单位
    for e in t:
        #  a是tuple，一个格子（一条船的一个坐标）
        for a in d:
            if a in e:
                print("{} in {}".format(a, e))
                ss = e
                # 执行了return之后，后面的语句都不知行了
                # 此处return：如果找到重复，则立即返回重复的船
                return ss
    return ss


# 一种类型多条船 且不重复
def ships(board_in, m, n, t):
    """
    同种类型 t条船 不重复
    :param board_in: list 地图
    :param m: 行数
    :param n: 列数
    :param t: 船数
    :return: list 子列表为一条船
    """
    sss = []
    while len(sss) < t:
        single_ship = large_ship(board_in, m, n)
        # 当large_ship()中超过界限的时候会返回[]，为保证sss中没有空列表
        if single_ship:
            # 判断船是否有重复
            # if、while 后面的list不为空的时候返回True
            if is_repeat(sss, single_ship):
                print("Repeat")
                continue
            else:
                sss.append(single_ship)
            # """
            # 不需要判断是否首次添加，如果sss=[]时，isrepeat()的结果为False
            # #   非首次添加，判断是否重复
            # """
            # if sss:
            #     if is_repeat(sss, single_ship) > 0:
            #         # single_ship = large_ship(board_in, m, n)
            #         # is_repeat(sss, single_ship)
            #         continue
            #     # # y是tuple，一个格子
            #     # for y in single_ship:
            #     #     # x是子列表，m*n个格子 以船为单位
            #     #     for x in sss:
            #     #         # 如果出现重复，需重新生成船；
            #     #         if y in x:
            #     #             print("{} in {}".format(y, x))
            #     #             single_ship = large_ship(board_in, m, n)
            #     #             # 找到立刻当前的退出循环，后面不再进行比较！！！
            #     #             break
            #
            #     # 未出现重复，保存
            #     else:
            #         sss.append(single_ship)
            # else:
            #     sss.append(single_ship)
    return sss


# 多种类型多条船 不重复
def mul_ships(board_in, a, b, c):
    """
    假设已知有三种类型的船，分别是1*1， 2*2， 4*3
    :param board_in:
    :param a:1*1 船数
    :param b:2*2 船数
    :param c:4*3 船数
    :return:
    """
    # 生成第一种类型船的时候，一种类型不重复的船
    sss = ships(board_in, 1, 1, a)
    print(len(sss))
    # 生成第二种类型
    while a <= len(sss) < (a + b):
        single_ship = large_ship(board_in, 2, 2)
        # 当large_ship()中超过界限的时候会返回[]，为保证sss中没有空列表
        if single_ship:
            # 判断船是否有重复
            if is_repeat(sss, single_ship):
                print("Repeat")
                continue
            else:
                sss.append(single_ship)
    # 生成第三种类型
    while (a + b) <= len(sss) < (a + b + c):
        single_ship = large_ship(board_in, 4, 3)
        # 当large_ship()中超过界限的时候会返回[]，为保证sss中没有空列表
        if single_ship:
            # 判断船是否有重复
            if is_repeat(sss, single_ship):
                print("Repeat")
                continue
            else:
                sss.append(single_ship)
    return sss


# print(ship(board))
# print(ships(board, 4, 3, 3))
# print(ships(board, 2, 2, 5))
# print(len(ships(board, 2, 2, 5)))

# print(mul_ships(board, 3, 3, 1))


def game(ships, n):
    """
    n次机会 击中战舰
    :param ships: 所有的船
    :param n: 机会
    :return:
    """
    count = 1
    while count <= n:
        print("Round {}".format(count))
        # 猜测点类型也要是 [(a, b)]，看做是1*1的一条船
        guess = []
        guess_row = int(input("Please enter the row of the ship:"))
        guess_col = int(input("Please enter the column of the ship:"))
        guess.append((guess_row, guess_col))
        print(guess)
        repeat_ship = is_repeat(ships, guess)
        # 猜中
        if repeat_ship:
            # 判断guess属于哪种类型的船
            # 根据所在的船判断
            if len(repeat_ship) == 1:
                score = 5
            elif len(repeat_ship) == 4:
                score = 10
            elif len(repeat_ship) == 12:
                score = 20
            print(score)
            print("Congratulations! You got it!")
            break
        # 未猜中，继续猜
        else:
            # 情况一：数字范围
            if guess_row not in range(10) or \
                            guess_col not in range(10):
                print("Notice: Please enter the number ranging from 0 to 9 and ")
            # 情况二：重复猜测
            elif board[guess_row][guess_col] == "X":
                print("Notice: You have guessed the location! Please try another!")
            # 情况三：未猜中
            else:
                print("You are wrong!")
                board[guess_row][guess_col] = "X"
                print_board(board)
            # 三种未猜中的情况，分数都为0
            score = 0
            # 修改循环条件
            count += 1

    print("Your score is {}".format(score))
    # if count > n:
    #     print("Sorry, you have no chances! Game over! ")



n = 5
ships = mul_ships(board, 3, 3, 1)
print(ships)
game(ships, n)
