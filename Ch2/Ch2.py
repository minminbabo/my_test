
# //은 몫만을 나타내는 연산자 ex) 7 // 4 -> 1
# %는 나머지 만을 나타내는 연산자 ex) 7 % 4 -> 3
# 지수연산자 **은 제곱임, ex) 2 ** 2 -> 2^2 = 4 -> 다른 산술 연산자보다 먼저 계산됨

#divmod(a ,b) -> tuple (a // b , a % b) 
#arr.index(value) - > index of array

# !important!
# 16진수 표현 방법 : 0x
# 8진수 표현 방법 : 0o
# 2진수 표현 방법 : 0b

from typing import Tuple
import math
import turtle

def tax(price: int) -> float:
    return price * (1.075)

def my_Turtle(x : int,y: int) -> None: #너비와 높이를 입력받아 사각형을 그리는 거북이
    t = turtle.Turtle()
    t.shape('turtle')
    t.goto(x,0)
    t.goto(x,y)
    t.goto(0,y)
    t.goto(0,0)

def mathtool(a:int,b:int) -> None: # a와 b를 입력받아 사칙연산 결과를 표시해주는 계산기
    p = a + b
    m = a - b
    d = a / b
    mu = a * b
    print(f'합은 {a+b}')
    print(f'차는 {a-b}')
    print(f'나누기는 {a/b}')
    print(f'곱은 {a*b}')
    print(f'{a} ** {b} = {a ** b}')

def interest(a:int, b:float, c:int) -> None: # 복리의 원리금을 구하는 함수
    inter_ = b / 100
    print (a * (1 + inter_) ** c)

def my_min(*args:Tuple[int,...]) -> int:
    min_value = args[0]
    for i in args:
        if min_value > i:
            min_value = i
    return min_value
            

def my_max(*args: Tuple[int,...]) -> int:
    determine = 0
    for _ in range(len(args)):
        if determine <= args[_]:
            determine = args[_]
    return determine

def ex_bool(radius : int) -> bool:
    return radius > 32

def whatday(a:str,b:int) -> None : # 무슨 요일인지 구하는 함수
    dayarr = ['월','화','수','목','금','토','일']
    today_index = dayarr.index(a)
    day_index = (today_index + b) % len(dayarr)
    print(f'{dayarr[day_index]} 입니다.')

def mod(a:int,b:int) -> None: # 나머지 연산과 몫 연산 연습
    q = a // b
    r = a % b
    return print(f'{a}를 {b}로 나누면, 몫은 {q} 나머지는 {r} 입니다.')

def compare(a:int,b:int) -> None: # 두 수를 비교하여 큰 수를 반환함
    e = a ** b
    f = b ** a
    if e > f:
        print(f'{e} 와 {f}, 더 큰 수는 a ** b')
    else :
        print(f'{e} 와 {f}, 더 큰 수는 b ** a')
        
def square(a:int) -> int:
    return a ** 3

def absolute(num: int) -> int: # 정수를 입력받아 절대값으로 반환하는 함수
    if num >= 0:
        return num
    else:
        return num * -1
    

def plus(a:int,b:int) -> None: # 정수의 합을 구하여 프린트 해주는 함수
    return print(a+b)

def minus(a:int,b:int) -> None: # 정수의 차를 구하여 프린트해주는 함수
    return print(a-b)

def triangle_square(width:int,height:int) -> None: # 삼각형의 넓이를 구하여 프린트 해주는 함수 
    return print(width*height/2)

def func()->None: # 메인 펑션
    x = [10,20,30]
    y = x.copy()
    y.reverse()
    print(x)
    print(f'{id(x)}, {id(y)})')


func()