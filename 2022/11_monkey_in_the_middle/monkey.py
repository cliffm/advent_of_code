from typing import List


class Monkey:
    def __init__(self, monkey_id: int, items: List[int], operation, div_test: int, true: int, false: int):
        self.id = monkey_id
        self.items = items
        self.div_test = div_test
        self.operation = operation
        self.true = true
        self.false = false

        self.inspect_count = 0

    def __repr__(self):
        return f"{self.id}"

    def perform_operation(self, item) -> int:
        self.inspect_count += 1
        return eval(self.operation.replace("old", str(item)))
