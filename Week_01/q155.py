class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_stack = []

    def push(self, x: int) -> None:
        self._stack.append(x)
        if len(self._min_stack) == 0 or x <= self._min_stack[-1]:
            self._min_stack.append(x)

    def pop(self) -> None:
        if self._stack[-1] == self._min_stack[-1]:
            self._min_stack.pop()
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]
