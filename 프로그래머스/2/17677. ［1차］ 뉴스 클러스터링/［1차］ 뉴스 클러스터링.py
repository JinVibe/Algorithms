# 테스트3는 중복 허용 집합
from collections import Counter
import math

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    
    str1_list = []
    str2_list = []
    
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1_list.append(str1[i: i + 2])
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_list.append(str2[i: i + 2])
            
    counter1 = Counter(str1_list)
    counter2 = Counter(str2_list)
    
    inter = counter1 & counter2
    uni = counter1 | counter2
    
    inter_len = sum(inter.values())
    uni_len = sum(uni.values())
    
    if uni_len == 0:
        return 65536
    else:
        return math.floor((inter_len / uni_len) * 65536)