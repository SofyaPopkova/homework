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


example_1 = '(((([{}]))))'
example_2 = '[([])((([[[]]])))]{()}'
example_3 = '{{[(])]}}'


def check_parentheses(example):
    unit = Stack()
    for char in example:
        if char in ['(', '{', '[']:
            unit.push(char)
        else:
            if not unit:
                return False
            current_char = unit.pop()
            if current_char == '(':
                if char != ')':
                    return False
            if current_char == '{':
                if char != '}':
                    return False
            if current_char == '[':
                if char != ']':
                    return False

    if unit:
        return False
    return True


if __name__ == '__main__':
    if check_parentheses(example_1):
        print("Сбалансированно")
    else:
        print("Не сбалансированно")

    if check_parentheses(example_2):
        print("Сбалансированно")
    else:
        print("Не сбалансированно")

    if check_parentheses(example_3):
        print("Сбалансированно")
    else:
        print("Не сбалансированно")
