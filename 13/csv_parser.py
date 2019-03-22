# https://www.cnblogs.com/guochangyu/p/7788414.html
class CSVParser(object):
    """
    csv文件的读取和写入
    并且还有 价格列表和写入内容的更新
    """
    def file_read(self, filepath):
        """
        reading contents from the csv file
        :param filepath:csv文件路径
        :return:内容列表 子列表为各行
        """
        with open(filepath, "r", encoding="utf-8") as file:
            # type(lines) = <class 'list'>，子元素为字符串
            lines = file.readlines()
            print(lines)
            contents_list = []
            for line in lines:
                # type(line) = <class 'str'>
                line_list = line.split(",")
                # price = line_list[1]
                # line_list[len(line_list)-1].replace("\n", "")
                contents = []
                i = 0
                while i in range(len(line_list)):
                    if "'" in line_list[i] and "'" in line_list[i + 1]:
                        # 如果相邻两个字符串含有"''"，则将两个数据合并
                        line_list[i] = line_list[i] + "," + line_list[i + 1]
                        contents.append(line_list[i])
                        i = i + 2
                    else:
                        contents.append(line_list[i])
                        i = i + 1
                contents_list.append(contents)
        return contents_list

    def prices_read(self, contents_list):
        """
        reading prices from the csv file
        :param contents_list: csv文件内容，list类型
        :return:价格列表
        """
        prices = []
        for row in contents_list:
            # type(line) = <class 'str'>
            price = row[1]
            prices.append(price)
        return prices

    # print(prices_read("data.csv"))

    def contents_update(self, new_prices, contents_list):
        """
        转换后的货币信息，替换原来的prices
        :param new_prices: list
        :param contents_list: list 子元素仍为列表
        :return:list 与contents_list结构一致
        """
        # new_contents = []
        # new_contents.append(contents_list[0])
        # 可以用如下方式简单表示：
        # new_contents = [contents_list[0]]
        new_contents = []
        for i in range(0, len(contents_list)):
            contents_list[i][1] = new_prices[i]
            new_contents.append(contents_list[i])
        return new_contents

    def file_write(self, filepath, new_contents):
        """
        writing contents in the file
        :param filepath: csv文件路径
        :param new_contents: 所有内容，list类型
        :return:
        """
        with open(filepath, "w", encoding="utf - 8") as file:
            for i in range(len(new_contents)):
                # row = new_contents[i]
                for j in range(len(new_contents[i])):
                    # 判断是否为最后一个元素
                    # 如果是最后一个元素，不再添加","
                    if j == len(new_contents[i]) - 1:
                        # 行中的某个元素，string = new_contents[i][j]
                        file.write(new_contents[i][j])
                    else:
                        # 不是最后一个元素，每次添加元素之后，要添加csv文件的分隔符","
                        file.write(new_contents[i][j] + ",")
            print("Done")


# csv = CSVParser()
# # print(csv.prices_read("data.csv"))
#
# print("contents_list = {}".format(csv.file_read("data.csv")))
# # print("prices = {}".format(csv.prices_read(csv.file_read("data.csv"))))
#
# prices = ['Price Per Month', '€59,38', '€44,10', '€660,82', '€6,39', '€15,70']
# contents_list = [['Feed Name', 'Price Per Month', 'Source Name', 'Last Update', 'Remote Name', 'Local Name\n'],
#                  ['newsmonster', '74.23', 'News Monster', '1483820232', '/mirror/nm/newsmonster.tgz', '/r/nm.tgz\n'],
#                  ['microtech', '55.12', 'MicroTech', 'Industries (TODO: Inc.? LLC?)', '1483820232', '/dl/mtech.tar.gz', '/r/mt.tgz\n'],
#                  ['fastniche', '826.02', 'Fast Niche® Markets', '1483820247', '/site/fastniche.zip', '/r/fn.tgz\n'],
#                  ['pivotsense', '7.99', 'Pivotal Sense (ltd.)', '1483820006', '/dl area/pivotsense.tgz', '/r/ps.tgz\n'],
#                  ['woldenheim', '19.62', 'Woldenheim GmbH', '1483817526', '/woldenheim/db-new.zip', '/r/wh.tgz']]
# print("new_contents = {}".format(csv.contents_update(prices, contents_list)))
#
# new_contents = [['Feed Name', 'Price Per Month', 'Source Name', 'Last Update', 'Remote Name', 'Local Name\n'],
#                 ['newsmonster', '€59,38', 'News Monster', '1483820232', '/mirror/nm/newsmonster.tgz', '/r/nm.tgz\n'],
#                 ['microtech', '€44,10', 'MicroTech', 'Industries (TODO: Inc.? LLC?)', '1483820232', '/dl/mtech.tar.gz', '/r/mt.tgz\n'],
#                 ['fastniche', '€660,82', 'Fast Niche® Markets', '1483820247', '/site/fastniche.zip', '/r/fn.tgz\n'],
#                 ['pivotsense', '€6,39', 'Pivotal Sense (ltd.)', '1483820006', '/dl area/pivotsense.tgz', '/r/ps.tgz\n'],
#                 ['woldenheim', '€15,70', 'Woldenheim GmbH', '1483817526', '/woldenheim/db-new.zip', '/r/wh.tgz']]
# filepath = "data2.csv"
# csv.file_write(filepath, new_contents)
