num1 = 10
num2 = 20
num3 = num1 + num2  # 정수 + 정수 = 정수

num1 = 30.5
num2 = 50.5
num3 = num1 + num2  # 실수 + 실수 = 실수

num1 = 10
num2 = 30.5
num3 = num1 + num2  # 정수 + 실수 = 실수


# 매출액 구하기
month1 = int(input('1월 매출 : '))
month2 = int(input('2월 매출 : '))
month3 = int(input('3월 매출 : '))
quarter1 = month1 + month2 + month3

print('1분기 총 매출은 {0}원 입니다.'.format(quarter1))

num1 = 3.14
num2 = 0.25
num3 = num1 + num2
float(num3)
int(num3)

# 이익 구하기
sales1 = int(input('1분기 매출 : '))
buy1 = int(input('1분기 매입 : '))
profit = sales1 - buy1

print('수익 : {0} 원'.format(profit))

# 방 너비 구하기
width = int(input('가로너비 : '))
height = int(input('세로너비 : '))
area = width * height

print('넓이 : {0} cm2'.format(area))


str1 = 'Hello, World!! '
str1 * 3
3 * str1 * 2
str1 * -1
# str1 * 0.1 # error


# BMI 구하기
weight = int(input('몸무게 : '))
height = int(input('신장 : '))
height = height / 100

bmi = weight / (height * height)

print('BMI : {0:.2f}'.format(bmi))
print(f'BMI : {bmi:.2f}')   # f-string : python 3.6 부터 지원

# print 출력 속도 : format > % > f-string(가장빠름)

# 동전 갯수 알아보기
coins = int(input('손 안의 동전 수를 입력하세요 '))
isEven = coins % 2

print(f'동전의 홀짝여부 (0:짝, 1:홀) {isEven}')

10 / 3
10 // 3


# 빵 나누어주기
bread = int(input('빵 갯수 : '))
diver = int(input('나줘줄 빵 갯수 : '))

stud = bread // diver
divmod = bread % diver

print(f'{bread}개의 빵은 {diver}개씨 {stud}명의 학생에게 나눠줄 수 있고,')
print(f'{divmod}개의 빵이 남음')

2 ** 3
2 ** 8

2 ** 29

# 복리계산기
# 원금, 유치기간, 연이율을 입력받아 복리계산후 총수령액 출력
# 1년차 : 원금 * 이율 = 원금
# ...
# 2년차 : 원금 * 이율 = 원금

money = 5_000_000
duration = 5
interest = 0.05

takes = money + (money * 0.05)   # 1년차
# takes = takes + (takes * 0.05)   # 2년차
takes += takes * 0.05
# takes = takes + (takes * 0.05)   # 3년차
takes += takes * 0.05
# takes = takes + (takes * 0.05)   # 4년차
takes += takes * 0.05
# takes = takes + (takes * 0.05)   # 5년차
takes += takes * 0.05

# 범퍼카 탑승 가능 여부 확인
height = int(input('어린이의 신장을 입력하세요 '))
# isRide = height >= 120 and height > 170
isRide = 120 <= height > 170
print(f'탑승 가능여부 : {isRide} (True : 탑승가능)')


'a' == 'b'
'a' > 'b'    # 아스키코드로 변환 후 비교


# 범퍼카 탑승 가능 여부 확인
height = int(input('어린이의 신장을 입력하세요 '))
# isRide = height >= 120 and height < 170
isRide = 120 <= height < 170
print(f'탑승 가능여부 : {isRide} (True : 탑승가능)')

temp = 0
temp <= 16 or temp > 28


# short circuit evaluation
num1 = 17
num2 = 20
(num1 < 15) and (num2 > 15)  # False and True

num1 = 10
num2 = 20
(num1 < 15) or (num2 < 15)  # True and False

# (num1 < 5) and xyz      # py38만 지원

# 삼항 연산자
# 참값 if 조건식 else 거짓일때값

num = 11
'짝수' if (num % 2 == 0) else '홀수'

# 적자/흑자 판단하기

income = int(input('수입을 입력하세요 '))
outcome = int(input('지출을 입력하세요 '))

result = '흑자' if (income > outcome) else '적자'
print(result)


# 윤년여부 알아보기
# 4로 나눠 떨어지고 100으로 나눠떨어지지 않음
# 400 으로 나눠 떨어짐
year = int(input('년도를 입력하세요 '))
isLeap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
result = '윤년' if (isLeap) else '평년'

print(result)

# operator 모듈을 이용하면 대량의 데이터 처리시 속도 향상이 존재함
import operator as op

op.add(10, 20)
op.sub(10, 20)
op.mul(10, 20)
op.floordiv(10, 3)  # 정수 몫 : //
op.truediv(10, 20)  # 실수 몫 : /
op.mod(10, 3)
op.pow(2, 30)

op.eq(10, 20)
op.ne(10, 20)
op.gt(10, 20)
op.lt(10, 20)
op.ge(10, 20)
op.le(10, 20)

x = op.eq(10, 20)
y = op.lt(10, 20)
op.and_(x, y)
op.or_(x, y)

# 긴급재난지원금 대상자 판별하기
income = int(input('월 소득을 입력하세요 '))
choice = int(input('다른 지원금을 받고 있습니까? (1번 받고있다. 2번 받고있지않다) '))

x = op.le(income, 4000000)
y = op.eq(choice, 2)
result = '수급 대상자' if(op.and_(x, y)) else '수급 대상자 아님'
print(result)


