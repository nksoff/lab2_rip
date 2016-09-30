ivan = {
    "name": "ivan",
    "age": 34,
    "children": [
        {
            "name": "vasja",
            "age": 10,
        },
        {
            "age": 12,
            "name": "petja",
        }
    ],
}
darja = {
    "name": "darja",
    "age": 41,
    "children": [
        {
            "age": 15,
            "name": "kirill",
        },
        {
            "age": 21,
            "name": "pavel",
        }
    ],
}
emps = [ivan, darja]


def my_filter(employyes):
    filtered = []

    for emp in employyes:
        for child in emp['children']:
            if child['age'] > 18:
                filtered.append(emp)
                break

    return filtered


if __name__ == '__main__':
    filtered = my_filter(emps)
    print(list(map(lambda x: x.get('name'), filtered)))
    assert darja in filtered
    assert ivan not in filtered
