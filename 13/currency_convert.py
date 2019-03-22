from csv_parser import CSVParser
from currency_string_converter import CurrencyStringConverter
import getopt
import sys


class CurrencyConvert(object):
    def __init__(self):
        self.csv_parser = CSVParser()
        self.csc = CurrencyStringConverter()

    def usage(self, prog):
        print("""
                    usage: {} <--field N> [--multiplier N] [-i input] [-o output]
                    """.format(prog)
              )

    def convert(self):
        """
        """
        # ************************* 解析命令行 ************************************
        order = {
            "field": "",
            "multiplier": "",
            "input": "",
            "output": ""
        }

        opts, args = getopt.getopt(sys.argv[3:], 'i:o:',
                                   [
                                       'field=',
                                       'multiplier=',
                                       'help'
                                   ]
                                   )

        # opts为分析出的格式信息，是一个两元组的列表。每个元素为：(选项串,附加参数)。如果没有附加参数则为空串''。
        for option, value in opts:
            if option in ["--help"]:
                self.usage(sys.argv[2])
                # 执行return后，不再执行余下所有其他语句
                return
            elif option in ["-i"]:
                order["input"] = value
            elif option in ["-o"]:
                order["output"] = value
            elif option in ["--field"]:
                order["field"] = value
            elif option in ["--multiplier"]:
                order["multiplier"] = value

        # args为不属于格式信息的剩余的命令行参数。包括那些没有"-"或"--"的参数
        # 当命令行中使用"<"和">"作为输入和输出文件的标志时
        for i in range(len(args)):
            if args[i] == "<":
                order["input"] = args[i + 1]
            elif args[i] == ">":
                order["output"] = args[i + 1]

        # print(order)
        # ************************* 解析命令行 ************************************
        # ************************* 业务流程  *************************************
        if ".csv" in order["input"]:
            # 从文件中读取
            contents_list = self.csv_parser.file_read(order["input"])
            # prices = self.csv_parser.prices_read(contents_list)
        else:
            # 从命令行直接输入
            # print(order["input"])
            #**************************处理数据本身带有逗号的情形，欧元***********************
            contents_split = order["input"].split(",")
            print(contents_split)
            contents = []
            i = 0
            while i in range(len(contents_split)):
                if "'" in contents_split[i] and "'" in contents_split[i + 1]:
                    # 如果相邻两个字符串含有"''"，则将两个数据合并
                    contents_split[i] = contents_split[i] + "," + contents_split[i + 1]
                    contents.append(contents_split[i])
                    i = i + 2
                else:
                    contents.append(contents_split[i])
                    i = i + 1
            print(contents)
            contents_list = [contents]
            print("contents_list = {}".format(contents_list))
            # prices = ["Price Per Month"]
            # prices.append(self.csv_parser.prices_read(contents_list)[0])
            # print(prices)
        # ************************************************************************************
        prices = self.csv_parser.prices_read(contents_list)
        print("prices = {}".format(prices))

        # 美元换欧元
        new_prices = self.csc.dollar_to_euro(prices, float(order["multiplier"]))
        print(new_prices)

        # # 欧元换美元
        # new_prices = self.csc.euro_to_dollar(prices, float(order["multiplier"]))
        # print(new_prices)

        new_contents = self.csv_parser.contents_update(new_prices, contents_list)

        if len(order["output"]) != 0:
            # 指定输出文件,则写入输出文件中
            self.csv_parser.file_write(order["output"], new_contents)
        else:
            # 未指定输出文件, 输出new_contents，与文件显示样式相同
            content = ""
            for i in range(len(new_contents)):
                # row = new_contents[i]
                for j in range(len(new_contents[i])):
                    # 判断是否为最后一个元素
                    # 如果是最后一个元素，不再添加","
                    if j == len(new_contents[i]) - 1:
                        # 行中的某个元素，string = new_contents[i][j]
                        content += new_contents[i][j]
                    else:
                        # 不是最后一个元素，每次添加元素之后，要添加csv文件的分隔符","
                        content += new_contents[i][j] + ","
            print(content)


if __name__ == '__main__':
    cc = CurrencyConvert()
    cc.convert()
