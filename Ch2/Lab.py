# brief:
# 사용자로부터 도시, 기온, 날씨를 입력받아
# 오늘 {도시}의 날씨는 {날씨}이며, 기온은 {기온}입니다. 적당한 날씨입니다. 즐거운 하루 보내세요 라고 출력

from typing import Tuple

def acronym(*args:Tuple[str,...]) -> str:
    acro = ''
    for index in args:
        acro += index[0]
    return acro



def robot()->None:
    city = input("도시 정보 입력 : ")
    whether = input("날씨 정보 입력 " )
    temp = input("기온 입력 : ")
    
    news = f'오눌 {city}의 날씨는 {whether}이며, 기온은 {temp}입니다.'

    news += "적당한 날씨입니다. 즐거운 하루 보내세요"
    print(news)


def main() -> None:
    strings = input("문자열을 입력하세요 : ")
    first_str = strings[0]
    last_str = strings[-1]
    mid_num = int(len(strings) / 2)
    mid_str = strings[mid_num]

    print(f'첫 번쨰 글자 : {first_str}\n가운데 글자 : {mid_str}\n마지막 글자 : {last_str}')

main()