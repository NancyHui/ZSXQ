inventory = {
    "change": 500,
    "small_pocket": ["knife", "rope", "gloves"],
    "big_pocket": ["tent", "bottle", "sleeping bag", "towel"]
}

# 增加一个key="snacks"
inventory["snacks"] = ["apple", "bread", "milk"]

# 排序
inventory["big_pocket"] = sorted(inventory["big_pocket"])
# inventory["big_pocket"].sort()
# 去掉"towel"
inventory["big_pocket"].remove("towel")
# 零钱加50
inventory["change"] = inventory["change"] + 50
print(inventory)
print(inventory["big_pocket"])