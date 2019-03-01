"""
5*5格子
一条船
每条船只占一个格子
10次击中就获得胜利；
也可以再尝试玩一局
"""
from random import randint

# 5*5格子
board = []
for i in range(5):
    board.append(["O"]*5)


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
    一个随机行数
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
    col = randint(0, len(board_in)-1)
    return col


# 目标船的位置
ship_row = random_row(board)
ship_col = random_col(board)
print("ship_row = {}, ship_col = {}".format(ship_row, ship_col))

# guess_row = int(input("Please the row of the ship:"))
# guess_col = int(input("Please the column of the ship:"))


def game(n):
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
        # 猜中
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You got it!")
            break
        # 未猜中，继续猜
        else:
            # 情况一：数字范围
            if guess_row not in range(5) or \
                            guess_col not in range(5):
                print("Notice: Please enter the number ranging from 0 to 4")
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
game(n)
# 是否再玩一局 战舰的位置不变
again = input("Would you want to try again?(y/n)")
if again == "y":
    print("You have another ten chances! Let start!")
    game(n)
else:
    print("Bye!")