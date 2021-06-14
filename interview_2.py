class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def check_parentheses(example):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    unit = Stack()
    unit_list = unit.items
    for char in example:
        if char in open_list:
            unit.push(char)
        elif char in close_list:
            res = close_list.index(char)
            if len(unit_list) > 0 and open_list[res] == unit_list[len(unit_list)-1]:
                unit.pop()
            else:
                return 'Не сбалансированно'
    if len(unit_list) == 0:
        return 'Сбалансированно'


if __name__ == '__main__':
    print(check_parentheses('(((([{}]))))'))
    print(check_parentheses('{{[()]}}'))
    print(check_parentheses('{{[(])]}}'))
