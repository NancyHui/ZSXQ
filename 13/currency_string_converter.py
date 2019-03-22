class CurrencyStringConverter(object):
    """货币字符串转换类，负责转换货币种类
    美元转换为欧元
    欧元转换为美元
    """
    # interest = 0.8

    def is_number(self, s):
        """
        判断字符串是否为数字
        :param s: 字符串
        :return:
        """
        try:
            float(s)
            return True
        except ValueError:
            pass
        return False

    def dollar_to_euro(self, prices, interest):
        """
        美元转换为欧元
        实例：74.23*0.8=€59.38
        保留小数点后两位
        :param prices:价钱列表 由字符串组成，判断元素是否为数字
        :param interest:利率
        :return:列表 有字符串组成
        """
        # euros = [prices[0]]
        # for i in range(1, len(prices)):
        #     price = prices[i]
        #     # print(float(price))
        #     # print(float(price) * self.interest)
        #     # 计算结果保留两位小数
        #     euro = "€{:.2f}".format(float(price) * interest)
        #     # 字符串中元素替换
        #     euros.append(euro.replace(".", ","))
        # return euros
        euros = []
        for i in range(0, len(prices)):
            price = prices[i]
            # isdigit()只能判断整数
            # isalpha()只能判断全是字母的情形，不能判断"Price Per Month"
            # 通过if...else...循环，将prices中的"Price Per Month"排除掉
            if self.is_number(price):
                # 当前price的内容为数字，则转换
                # print(float(price))
                # print(float(price) * self.interest)
                # 计算结果保留两位小数
                euro = "€{:.2f}".format(float(price) * interest)
                # 字符串中元素替换
                # euro = euro.replace(".", ",")
                # euros.append("{}".format(euro))
                # 欧元中有","，为了区分分隔符","，此处用"''"作为整体加以区分
                euros.append("'" + euro.replace(".", ",") + "'")
            else:
                euros.append(price)
                continue
        return euros

    def euro_to_dollar(self, prices, interest):
        """
        欧元欧元转换为美元
        实例：€59,38/0.8=74.23
        先取出59,38转换为59.38
        保留小数点后两位
        :param prices:价钱列表 由字符串组成，判断元素是否为数字
        :param interest:利率
        :return:列表 有字符串组成
        """
        # dollars = [prices[0]]
        # for i in range(1, len(prices)):
        #     # 从字符串中取出数字，仍为字符串
        #     price = prices[i][1:]
        #     # 字符串中的","替换为"."  e.g.: 59,38转换为59.38
        #     price = price.replace(",", ".")
        #     # 计算结果保留两位小数
        #     dollar = "{:.2f}".format(float(price) / interest)
        #     # 字符串中元素替换
        #     dollars.append(dollar)
        # return dollars
        dollars = []
        for i in range(0, len(prices)):
            # 从列表中取出元素，为字符串
            # 从字符串中取出数字，仍为字符串，去掉欧元标志及"''"
            price = prices[i][2:(len(prices[i])-1)]
            # 字符串中的","替换为"."  e.g.: 59,38转换为59.38
            price = price.replace(",", ".")
            # 通过if...else...循环，将prices中的"Price Per Month"排除掉
            if self.is_number(price):
                # 当前price的内容为数字，则转换
                # 计算结果保留两位小数
                dollar = "{:.2f}".format(float(price) / interest)
                # 字符串中元素替换
                dollars.append(dollar)
            else:
                # price不是数字，直接放入dollars中
                dollars.append(price)
                continue
        return dollars


# csv = CurrencyStringConverter()
# ds = ['Price Per Month', '74.23', '55.12', '826.02', '7.99', '19.62']
# print(csv.dollar_to_euro(ds))
#
# es = ['Price Per Month', '€59,38', '€44,10', '€660,82', '€6,39', '€15,70']
# print(csv.euro_to_dollar(es))
