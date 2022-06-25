class Stack:
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        del self.data[-1]

    def top(self) -> int:
        self.data[-1]

    def empty(self) -> bool:
        return self.data.__len__() == 0
