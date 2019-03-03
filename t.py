from random import randint
board = []
for i in range(2):
    board.append(["O"]*2)
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


# board[6][7] = "x"
# print_board(board)


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
     :return:一个格子 list [row, col]
     """
    row = random_row(board_in)
    col = random_col(board_in)

    return row, col

# print(ship(board))

def large_ship(board_in, m, n):
    """
    一条船：m*n
    :param board_in: list 地图
    :param m: 行
    :param n: 列
    :return: 船所在格子的列表 list
    """
    ss = []
    # 随机产生一条小船或大船的左上角 tuple
    r, c = (0, 0)
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


print(large_ship(board, 2, 2))
# print_board(board)
