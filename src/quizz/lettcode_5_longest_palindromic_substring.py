def LPS(_string, m, n) -> int:
    if n > m:
        if _string[m] == _string[n]:
            sub_result = LPS(_string, m + 1, n - 1)
            if sub_result == n - m - 1:
                return sub_result + 2
            else:
                return sub_result
        else:
            return max(
                LPS(_string, m + 1, n),
                LPS(_string, m, n - 1)
            )
    elif n == m:
        return 1
    else:
        return 0


def LPS2(_string, m, n, memo) -> int:
    if memo[m][n] > -1:
        return memo[m][n]

    ret_val = -1
    if n > m:
        temp_val = 0
        if _string[m] == _string[n]:
            sub_result = LPS2(_string, m + 1, n - 1, memo)
            if sub_result == n - m - 1:
                temp_val = sub_result + 2
            else:
                temp_val = sub_result

        ret_val = max(temp_val,
                      max(
                          LPS2(_string, m + 1, n, memo),
                          LPS2(_string, m, n - 1, memo)
                      )
                      )
    elif n == m:
        ret_val = 1
    else:
        ret_val = 0

    memo[m][n] = ret_val

    return ret_val


def LPS3(_string, m, n, memo) -> str:
    if memo[m][n] is not None:
        return memo[m][n]

    ret_val = None
    if n > m:
        temp_result = ""
        if _string[m] == _string[n]:
            sub_result = LPS3(_string, m + 1, n - 1, memo)
            if sub_result == _string[m + 1:n]:
                temp_result = f"{_string[m]}{sub_result}{_string[n]}"
            else:
                temp_result = sub_result

        sub_result_left = LPS3(_string, m + 1, n, memo)
        sub_result_right = LPS3(_string, m, n - 1, memo)

        if len(temp_result) >= len(sub_result_left) and len(temp_result) >= len(sub_result_right):
            ret_val = temp_result
        elif len(sub_result_left) >= len(temp_result) and len(sub_result_left) >= len(sub_result_right):
            ret_val = sub_result_left
        elif len(sub_result_right) >= len(temp_result) and len(sub_result_right) >= len(sub_result_left):
            ret_val = sub_result_right

    elif n == m:
        ret_val = _string[m]
    else:
        ret_val = ""

    memo[m][n] = ret_val

    return ret_val


from unittest import TestCase as tc


class Test(tc):
    def test1(self):
        given = "1"
        cut = LPS(given, 0, len(given) - 1)
        self.assertEqual(1, cut)

    def test2(self):
        given = "12"
        cut = LPS(given, 0, len(given) - 1)
        self.assertEqual(1, cut)

    def test3(self):
        given = "121"
        cut = LPS(given, 0, len(given) - 1)
        self.assertEqual(3, cut)

    def test4(self):
        given = "1221"
        cut = LPS(given, 0, len(given) - 1)
        self.assertEqual(4, cut)

    def test5(self):
        given = "12121"
        cut = LPS(given, 0, len(given) - 1)
        self.assertEqual(5, cut)

    def test6(self):
        given = "012121"
        cut = LPS(given, 0, len(given) - 1)
        self.assertEqual(5, cut)


class Test2(tc):
    def test1(self):
        given = "1"
        memo = [[-1 for j in range(len(given))] for i in range(len(given))]
        cut = LPS2(given, 0, len(given) - 1, memo)
        self.assertEqual(1, cut)

    def test2(self):
        given = "12"
        memo = [[-1 for j in range(len(given))] for i in range(len(given))]
        cut = LPS2(given, 0, len(given) - 1, memo)
        self.assertEqual(1, cut)

    def test3(self):
        given = "121"
        memo = [[-1 for j in range(len(given))] for i in range(len(given))]
        cut = LPS2(given, 0, len(given) - 1, memo)
        self.assertEqual(3, cut)

    def test4(self):
        given = "1221"
        memo = [[-1 for j in range(len(given))] for i in range(len(given))]
        cut = LPS2(given, 0, len(given) - 1, memo)
        self.assertEqual(4, cut)

    def test5(self):
        given = "12121"
        memo = [[-1 for j in range(len(given))] for i in range(len(given))]
        cut = LPS2(given, 0, len(given) - 1, memo)
        self.assertEqual(5, cut)

    def test6(self):
        given = "012121"
        memo = [[-1 for j in range(len(given))] for i in range(len(given))]
        cut = LPS2(given, 0, len(given) - 1, memo)
        self.assertEqual(5, cut)


class Test3(tc):
    def test1(self):
        given = "1"
        memo = [[None for j in range(len(given))] for i in range(len(given))]
        cut = LPS3(given, 0, len(given) - 1, memo)
        self.assertEqual("1", cut)

    def test2(self):
        given = "12"
        memo = [[None for j in range(len(given))] for i in range(len(given))]
        cut = LPS3(given, 0, len(given) - 1, memo)
        self.assertEqual("2", cut)

    def test3(self):
        given = "121"
        memo = [[None for j in range(len(given))] for i in range(len(given))]
        cut = LPS3(given, 0, len(given) - 1, memo)
        self.assertEqual("121", cut)

    def test4(self):
        given = "1221"
        memo = [[None for j in range(len(given))] for i in range(len(given))]
        cut = LPS3(given, 0, len(given) - 1, memo)
        self.assertEqual("1221", cut)

    def test5(self):
        given = "12121"
        memo = [[None for j in range(len(given))] for i in range(len(given))]
        cut = LPS3(given, 0, len(given) - 1, memo)
        self.assertEqual("12121", cut)

    def test6(self):
        given = "012121"
        memo = [[None for j in range(len(given))] for i in range(len(given))]
        cut = LPS3(given, 0, len(given) - 1, memo)
        self.assertEqual("12121", cut)

    def test7(self):
        given = "aacabdkacaa"
        memo = [[None for j in range(len(given))] for i in range(len(given))]
        cut = LPS3(given, 0, len(given) - 1, memo)
        self.assertEqual("aca", cut)
