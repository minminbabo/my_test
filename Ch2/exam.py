

#사용자로부터 2개의 정수를 입력받아, 정수의 합, 정수의 차, 정수의 곱, 정수의 평균, 큰 수 작은 수를 계산하는 프로그램
from typing import Tuple
import math

def my_avearge(*args:Tuple[int,...]) -> float:
    total = 0
    for value in args:
        total += value
    aver = total / len(args)
    return aver

def my_max(*args:Tuple[int,...]) -> int:
    init_value = args[0]
    for value in args:
        if init_value < value:
            init_value = value
    return init_value

def my_min(*args:Tuple[int,...]) -> int:
    init_value = args[0]
    for value in args:
        if init_value > value:
            init_value = value
    return init_value

def my_plus(*args:Tuple[int,...]) -> int:
    summury = 0
    for value in args:
        summury += value
    return summury

def my_minus(*args:Tuple[int,...]) -> int:
    minus = args[0]
    for value in args[1:]:
        minus -= value
    return minus

def my_multiple(*args:Tuple[int,...]) -> int:
    multiple = 1
    for value in args:
        multiple *= value
    return multiple

def my_divide(*args:Tuple[int, ...]) -> float:
    if len(args) < 2 :
        print("2개 이상의 정수를 입력하세요")
        return

    divide = args[0] / args[1]
    if len(args) > 3:
        for value in args[2:]:
            divide = divide / value
    return round(divide, 2)

# def my_round(value: float, range:int) -> float:
#     round = f"{value:.{range}f}"
#     round = float(round)
#     return round

# 원기둥의 부피를 계산하는 프로그램을 작성하시오, 원기둥의 부피 : V = pi * radius **2 * height

def cylinder_volume(radius:float, height: float) -> float:
    volume = radius ** 2 * height * math.pi
    return round(volume , 3)

# 입력된 str의 각 자리의 합을 더하는 펑션

def plus_str_initial_by_initial(str:str) -> int:
    total = 0
    for i in range(len(str)):
        total += int(str[i]) 
    return total

# BMI 지수를 구하는 방법 : Weight / height ** 2

def my_BMI(weight: float, heiht: float) -> float:
    bmi = weight / (heiht/100) ** 2
    return bmi

# 두 점 사이의 거리를 구하는 함수

def my_distance(args_1:tuple[int],args_2:tuple[int]) -> float:
    x_diff = args_1[0] - args_2[0]
    y_diff = args_1[1] - args_2[1]
    
    distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
    return distance

# 사용자로부터 나이와 이름을 입력받고, 입력받은 정보를 포맷팅하여 출력하는 프로그램
def hello(name:str, age:int) -> None:
    print(f'안녕하세요, 저는 {name}이고, {age}살 입니다.')

def my_deco(func):
    def wrapper():
        print("데코 테스트")
        func()
        print("데코 테스트 끝")
        return
    return wrapper

#사용자로부터 문자열과 반복 횟수를 입력받아서 해당 문자열을 입력받은 횟수만큼 반복하여 출력하는 프로그램

def repeating(strings:str, repeat_num:int) -> None:
    for i in range(repeat_num):
        print(strings)

@my_deco
def main():
    strings = input("반복할 말 입력 : ")
    repeat_num = int(input("횟수 : "))
    repeating(strings,repeat_num)

main()