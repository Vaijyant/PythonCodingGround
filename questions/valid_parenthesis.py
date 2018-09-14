def parse(program_string):
    dic = {'(' : ')', '[' : ']', '{':'}'}
    stack = []
    for c in program_string:
        if c in dic:
            stack.append(c)
        else:
            if not stack or dic[stack.pop()] != c:
                return False
    return not stack


print(parse('[]{{}{}}'))
print(parse("[]["))