from llistStackADt import Stack

def isValidSource(srcfile):
    s = Stack()
    for line in srcfile:
        for token in line:
            if token in "{[(":
                s.push(token)
            elif token in "}])":
                if s.isEmpty():
                    return False
                else:
                    left = s.pop()
                    if (token == "}" and left != "{") or \
                    (token == "]" and left != "[") or \
                    (token == ")" and left != "(") :
                        return False
    return s.isEmpty()

if __name__ == "__main__":
    with open("RightTest.c", "r") as rc_file, \
        open("WrongTest.c", "r") as wc_file:
        print(isValidSource(rc_file))
        print(isValidSource(wc_file))