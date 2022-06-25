def merge(arr_a, start_a, end_a, arr_b, start_b, end_b):
    merged_arr = []
    idx_a = start_a
    idx_b = start_b
    while idx_a < end_a and idx_b < end_b:
        if arr_a[idx_a] > arr_b[idx_b]:
            merged_arr.append(arr_b[idx_b])
            idx_b += 1
        else:
            merged_arr.append(arr_a[idx_a])
            idx_a += 1

    while idx_a < end_a:
        merged_arr.append(arr_a[idx_a])
        idx_a += 1

    while idx_b < end_b:
        merged_arr.append(arr_b[idx_b])
        idx_b += 1

    return merged_arr


def merge_sort(arr: list, m, n) -> list:
    if n > m:
        mid = int((m + n) / 2)
        sub_arr_left = merge_sort(arr, m, mid)
        sub_arr_right = merge_sort(arr, mid + 1, n)
        idx_left = idx_right = 0
        merged_arr = []
        while idx_left < len(sub_arr_left) and idx_right < len(sub_arr_right):
            if sub_arr_left[idx_left] > sub_arr_right[idx_right]:
                merged_arr.append(sub_arr_right[idx_right])
                idx_right += 1
            else:
                merged_arr.append(sub_arr_left[idx_left])
                idx_left += 1

        while idx_left < len(sub_arr_left):
            merged_arr.append(sub_arr_left[idx_left])
            idx_left += 1

        while idx_right < len(sub_arr_right):
            merged_arr.append(sub_arr_right[idx_right])
            idx_right += 1

        return merged_arr
    else:
        return [arr[m]]


from unittest import TestCase as tc


class Test(tc):
    def test1(self):
        a = [1]
        b = [2]
        self.assertListEqual([1, 2], merge(a, 0, len(a), b, 0, len(b)))

    def test2(self):
        a = [1, 3, 5]
        b = [2, 4, 6]
        self.assertListEqual([1, 2, 3, 4, 5, 6], merge(a, 0, len(a), b, 0, len(b)))

    def test3(self):
        a = [1]
        b = [2, 4, 6]
        self.assertListEqual([1, 2, 4, 6], merge(a, 0, len(a), b, 0, len(b)))

    def test4(self):
        a = [1, 3, 5]
        b = [2]
        self.assertListEqual([1, 2, 3, 5], merge(a, 0, len(a), b, 0, len(b)))

    def test5(self):
        a = [1, 3, 2, 5, 7, 6, 4]
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7], merge_sort(a, 0, len(a) - 1))

    def test6(self):
        a = [9, 2, 4, 6, 3, 2, 5, 76, 7, 3, 22, 4, 6, 6, 889, 5, 2, 21, 2, 4]
        self.assertListEqual([2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 9, 21, 22, 76, 889],
                             merge_sort(a, 0, len(a) - 1))
