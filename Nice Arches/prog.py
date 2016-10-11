class Stack():
    def __init__(self):
        self.stack = []

    def topItem(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def popItem(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def pushItem(self, item):
        self.stack.insert(len(self.stack), item)

    def printStack(self):
        print(self.stack)

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

def isBubblyWord(word):
    stack = Stack()

    for char in word:
        if stack.topItem() == char:
            stack.popItem()
        else:
            stack.pushItem(char)

    return stack.isEmpty()

if __name__=='__main__':
    bubblyCount = 0
    M = int(input())

    for _ in range(M):
        word = input().strip()
        if isBubblyWord(word):
            bubblyCount += 1

    print(bubblyCount)
