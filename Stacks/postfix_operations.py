from llistStackADt import Stack

def operation(postfix):
    s = Stack()
    for char in postfix:
        if char.isdigit(): 
            s.push(int(char))
        elif char in "+-*/":
            if s.__len__() < 2:
                return "Invalid postfix. (Only one value on stack, two needed.)"
            else:
                b = s.pop()
                a = s.pop()
                if char == "+": ans = a + b
                if char == "-": ans = a - b
                if char == "*": ans = a * b
                if char == "/": ans = a/b
                s.push(ans)
    if s.__len__() == 1:
        return s.peek()
    else:
        return "Invalid postfix. (Too many values left on stack.)"
    
if __name__ == "__main__":
    def prints(pi):
        if not isinstance(operation(pi), (int, float)):
            print(f"{pi} : {operation(pi)}")
        else: print(f"The result of '{pi}' is {operation(pi)}")

    p = "823+*4/"
    p1 = "82*34+"
    p2 = "82*+"
    prints(p)
    prints(p1)
    prints(p2)
