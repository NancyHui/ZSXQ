# r, c = [1, 1]
# ss = []
#
# for z in range(1, 3):
#     for j in range(1, 3):
#         # s = []
#         # s.append(i)
#         # s.append(j)
#         s = z, j
#         ss.append(s)
# print(ss)

# from random import randint
#
# # 10*10格子
# board = []
# for i in range(10):
#     board.append(["O"]*10)
# print(board)
#
#
# def print_board(board_in):
#     """
#     子列表分行打印
#     :param board_in: 由子列表组成的列表
#     :return: 子列表
#     """
#     for row in board_in:
#         # 针对列表中的元素，使用" "（空格）链接
#         print(" ".join(row))
#
#
# # board[2][2] = "x"
# print_board(board)

# x, y = (1, 2)
# print("x = {}, y = {}".format(x, y))
#
# print(1,2)
#
# s = 1, 2
# print(s)

t = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
d = [(4, 2), (3, 4)]
for e in t:
    for a in d:
        if a in e:
            print("Y")
        # else:
        #     print(t.append(d))




