def my_min(arr):
    if len(arr) == 0:
        return None

    m = arr[0]

    for i in arr:
        if i < m:
            m = i

    return m


def my_avg(arr):
    if len(arr) == 0:
        return None

    s = 0

    for i in arr:
        s += i

    return s / len(arr)


if __name__ == '__main__':
    assert my_min([]) is None
    assert my_min([6, -1, -10, 5, 3, 7, 9]) == -10

    assert my_avg([]) is None
    assert my_avg([5, 0, 3, 1, 1]) == 2
