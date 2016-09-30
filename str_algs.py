def my_reverse(str):
    return ''.join(reversed(list(str)))


if __name__ == '__main__':
    assert my_reverse("hello, world") == "dlrow ,olleh"
    assert my_reverse("арозаупаланалапуазора") == "арозаупаланалапуазора"
