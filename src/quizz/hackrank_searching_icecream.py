from collections import defaultdict


def whatFlavors(cost, money):
    print(f"cost:{cost}, money:{money}")
    d = defaultdict(lambda: [])
    for idx in range(len(cost)):
        price = cost[idx]
        d[price].append(idx)

    for favor_1_idx in range(len(cost)):
        price_1 = cost[favor_1_idx]
        if price_1 < money:
            price_2 = money - price_1
            if d.__contains__(price_2):
                favor_idx_list = d[price_2]
                for favor_2_idx in favor_idx_list:
                    if favor_2_idx != favor_1_idx:
                        return favor_1_idx + 1, favor_2_idx + 1


import unittest


class Test(unittest.TestCase):
    def test1(self):
        cost = [1, 4, 5, 3, 2]
        money = 4
        cut = whatFlavors(cost, money)
        self.assertEqual((1, 4), cut)
