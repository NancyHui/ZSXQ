"""
附加题一
10*5格子
n条船
每条船只占一个格子，且不能重复
10次击中就获得胜利；也可以再尝试玩一局
"""
from random import randint

# 10*5格子
board = []
for i in range(10):
    board.append(["O"]*5)
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


# 首次生成新船，存储；
# 再次生成新船时，判断之前是否生成过
def ship(board_in):
    """
     一条船
     :param board_in: list 地图
     :return:一条船 list [row, col]
     """
    row_col = []

    row = random_row(board_in)
    col = random_col(board_in)
    row_col.append(row)
    row_col.append(col)
    return row_col


def ships(board_in, n):
    """
    n条船 可能重复
    :param board_in: list 地图
    :param n: 船数
    :return: list 子列表为一条船
    """
    ships = []
    for i in range(n):
        ships.append(ship(board_in))
    print(ships)


print(ship(board))
ships(board, 5)


# 船不能重复
def nonrepetive_ships(board_in, n):
    """
    n条船 不重复
    :param board_in: list 地图
    :param n: 船数
    :return: list 子列表为一条船
    """
    ships = []

    # for i in range(n):
    while len(ships) < n:
        s = ship(board_in)
        print(s)
        # 当ships为空，下面的语句判断结果一定为False
        # 已经存储过，再次循环，而循环次数
        if s in ships:
            print("repeat")
            continue
        # 未存储过，添加至ships中
        else:
            print("nonrepeat")
            ships.append(s)

        # # ships不为空，判断新生成的船之前是否存储过
        # if ships:
        # # ship为空，即为首次生成船，直接生成即可
        # else:
        #     ships.append(s)
    return ships


print(nonrepetive_ships(board, 10))


def game(ships, n):
    """
    n次机会 击中战舰
    :param n: 机会
    :return:
    """
    count = 1
    while count <= n:
        print("Round {}".format(count))
        guess_row = int(input("Please enter the row of the ship:"))
        guess_col = int(input("Please enter the column of the ship:"))
        guess = []
        guess.append(guess_row)
        guess.append(guess_col)
        print(guess)
        # 猜中
        if guess in ships:
            print("Congratulations! You got it!")
            break
        # 未猜中，继续猜
        else:
            # 情况一：数字范围
            if guess_row not in range(10) or \
                            guess_col not in range(5):
                print("Notice: Please enter the number of row ranging from 0 to 9 and col ranging from 0 to 4")
            # 情况二：重复猜测
            elif board[guess_row][guess_col] == "X":
                print("Notice: You have guessed the location! Please try another!")
            # 情况三：未猜中
            else:
                print("You are wrong!")
                board[guess_row][guess_col] = "X"
                print_board(board)
            count += 1
            # continue
    if count > n:
        print("Sorry, you have no chances! Game over! ")

n = 5
ships = nonrepetive_ships(board, 10)
print(ships)
game(ships, n)