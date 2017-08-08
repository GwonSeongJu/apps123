def factor(inp):
    if inp == 1:
        return 1
    return int(inp) * factor(int(inp)-1)
input_v = input("값을 입력해주세요")
print(factor(input_v))
