
import keyword

myName = 'Jaemuk'
myMajor = '데이터 분석'

print(myName)
print(myMajor)

myName = 100
myName = True
myName = False
myName = 3.141592

intro = 'Hello'
print(intro)
intro = '안녕하세요.'
print(intro)

nickname = 'Mr.Yang'
print(nickname)

print(keyword.kwlist)
# print(keyword.softkwlist)   # python 3.9 에서 추가

myName = 'yang'

# $myScore = 100
# *score! = 200
_score_ = 300

bigint = 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
print(bigint)

bigfloat = 1.234567890234567890234567890234567890234567890234567890234567890234567890234567890234567890234567890
print(bigfloat)

a = 123
b = '456'

a = a + 1
# b = b + 1

print(type('안녕하세요'))
print(type(123))
print(type(True))

print(type(myName))

# 다중 선언
x = 1
y = 1
z = 1

x = y = z = 10

# 자릿수 구분
million = 1000000
million = 1_000_000
num = 1_2_3

# 논리값 확인 : bool
bool(True)
bool(1)
bool(100)
bool(-100)
bool(0)

str(123)
int('456')
float('3.14')

name = input('이름을 입력하세요\n')
print(name)

# 이름, 국어, 영어, 수학을 입력받아
# 출력하는 프로그램을 작성하세요

name = input('이름을 입력하세요 : ')
kor = input('국어점수를 입력하세요 : ')
eng = input('영어점수를 입력하세요 : ')
mat = input('수학점수를 입력하세요 : ')
print (name, kor, eng, mat)






