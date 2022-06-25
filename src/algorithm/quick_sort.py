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
