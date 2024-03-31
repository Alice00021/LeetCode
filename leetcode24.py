
def isPalindrome(x:int)-> bool:
    return  str(x)==str(x)[::-1]
print(isPalindrome(101))




class BracketChecker:
    def __init__(self):
        self.stack = []

    def push(self, symbol):
        self.stack.append(symbol)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def process_input(self, input_string):
        opening_brackets = "({["
        closing_brackets = ")}]"
        for symbol in input_string:
            if symbol in opening_brackets:
                self.push(symbol)
            elif symbol in closing_brackets:
                if len(self.stack) == 0:
                    return False
                top = self.pop()
                if opening_brackets.index(top) != closing_brackets.index(symbol):
                    return False

        if len(self.stack) == 0:
            return True
        else:
            return False

