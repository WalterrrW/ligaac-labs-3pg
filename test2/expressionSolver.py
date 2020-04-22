def compute(exp, firstRankExp):
    try:
        if len(exp) == 1:
            return exp[0]
        for count, elem in enumerate(exp):
            if firstRankExp and isinstance(elem, str):
                if elem != "*" and elem != "/" and elem != "%":
                    continue
                if elem == "*":
                    exp.__setitem__(count - 1, int(exp.__getitem__(count - 1)) * int(exp.__getitem__(count + 1)))
                elif elem == "/":
                    exp.__setitem__(count - 1, int(exp.__getitem__(count - 1)) / int(exp.__getitem__(count + 1)))
                elif elem == "%":
                    exp.__setitem__(count - 1, int(exp.__getitem__(count - 1)) % int(exp.__getitem__(count + 1)))
                exp.pop(count + 1), exp.pop(count)
                return compute(exp, firstRankExp)
            elif not firstRankExp and isinstance(elem, str):
                if elem == "+":
                    exp.__setitem__(count - 1, int(exp.__getitem__(count - 1)) + int(exp.__getitem__(count + 1)))
                elif elem == "-":
                    exp.__setitem__(count - 1, int(exp.__getitem__(count - 1)) - int(exp.__getitem__(count + 1)))
                exp.pop(count + 1), exp.pop(count)
                return compute(exp, firstRankExp)
        return compute(exp, False)
    except:
        print("Not Valid Expression!!!")


def check(exp):
    try:
        newExp = []
        for elem in exp:
            if elem != "*" and elem != "/" and elem != "%" and elem != "+" and elem != "-":
                newExp.append(int(elem))
            else:
                newExp.append(elem)
        return newExp
    except:
        print("Not an integer!")


if __name__ == "__main__":
    print("Enter your own expression, divide values with ' ' (space), and you will get the solution!")
    print("ex of expression: 32 + 8 / 2 * 10 - 23, in this case 49 will be shown")
    s = input("An expresion pls: ")
    exp = [x for x in s.split()]
    exp = check(exp)
   # print(exp)
    solution = compute(exp, True)
    print(solution)
