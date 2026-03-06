def f(x):
    if x % 2 == 0:
        return x + 1
    
    x = f'0{bin(x)[2:]}' # 이진수 변환
    x = f"{x[:x.rindex('0')]}10{x[x.rindex('0') + 2:]}"
    
    return int(x, 2)

# 7 = 0111
# 8 = 1000
# 9 = 1001
# 10 = 1010
# 11 = 1011 = 01011
# 12 = 1100 = 01100
# 13 = 1101 = 01101

def solution(numbers):
    return [f(number) for number in numbers]