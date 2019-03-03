"""
附加题二
10*10格子
n条船，且不能重复，不能超出边界
三种类型：1*1(3) 2*2(3) 4*3(1)
10次击中就获得胜利；也可以再尝试玩一局
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
    print(r,c)
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


# 一种类型多条船 且不重复
def ships(board_in, m, n, t):
    """
    t条船 可能重复
    :param board_in: list 地图
    :param m: 行数
    :param n: 列数
    :param t: 船数
    :return: list 子列表为一条船
    """
    sss = []
    while len(sss) < t:
        single_ship = large_ship(board_in, m, n)
        if single_ship:
        #   判断船是否有重复
        #   非首次添加，判断是否重复
            if sss:
                for y in single_ship:
                    for x in sss:
                        # 如果出现重复，则重新生成船；
                        # 未出现重复，保存
                        if y in x:
                            print("{} in {}".format(y, x))
                            break
                sss.append(single_ship)
            # 首次直接添加
            else:
                sss.append(single_ship)

        # 当large_ship()中超过界限的时候会返回[]，为保证sss中没有空列表
        # if single_ship:
        #     sss.append(single_ship)
    return sss


# print(ship(board))
print(ships(board, 2, 2, 5))
# print(len(ships(board, 2, 2, 5)))


# # 船不能重复
# def nonrepetive_ships(board_in, n):
#     """
#     n条船 不重复
#     :param board_in: list 地图
#     :param n: 船数
#     :return: list 子列表为一条船
#     """
#     ships = []
#
#     # for i in range(n):
#     while len(ships) < n:
#         s = ship(board_in)
#         print(s)
#         # 当ships为空，下面的语句判断结果一定为False
#         # 已经存储过，再次循环，而循环次数
#         if s in ships:
#             print("repeat")
#             continue
#         # 未存储过，添加至ships中
#         else:
#             print("nonrepeat")
#             ships.append(s)
#
#         # # ships不为空，判断新生成的船之前是否存储过
#         # if ships:
#         # # ship为空，即为首次生成船，直接生成即可
#         # else:
#         #     ships.append(s)
#     return ships
#
#
# print(nonrepetive_ships(board, 10))
#
#
# def game(ships, n):
#     """
#     n次机会 击中战舰
#     :param n: 机会
#     :return:
#     """
#     count = 1
#     while count <= n:
#         print("Round {}".format(count))
#         guess_row = int(input("Please enter the row of the ship:"))
#         guess_col = int(input("Please enter the column of the ship:"))
#         guess = []
#         guess.append(guess_row)
#         guess.append(guess_col)
#         print(guess)
#         # 猜中
#         if guess in ships:
#             print("Congratulations! You got it!")
#             break
#         # 未猜中，继续猜
#         else:
#             # 情况一：数字范围
#             if guess_row not in range(10) or \
#                             guess_col not in range(5):
#                 print("Notice: Please enter the number of row ranging from 0 to 9 and col ranging from 0 to 4")
#             # 情况二：重复猜测
#             elif board[guess_row][guess_col] == "X":
#                 print("Notice: You have guessed the location! Please try another!")
#             # 情况三：未猜中
#             else:
#                 print("You are wrong!")
#                 board[guess_row][guess_col] = "X"
#                 print_board(board)
#             count += 1
#             # continue
#     if count > n:
#         print("Sorry, you have no chances! Game over! ")
#
# n = 5
# ships = nonrepetive_ships(board, 10)
# print(ships)
# game(ships, n)