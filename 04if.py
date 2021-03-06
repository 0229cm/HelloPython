# 조건문
# 주어진 상황에 따라 적절한 명령문을 수행하는 문장
# 프로그래밍에서 조건을 판단하여
# 해당 조건에 맞는 상황을 수행하는데 사용됨

# 조건문 작성시 반드시 들여쓰기(탭)에 따라 문장을 작성해야함
# 조건문은 일반적으로 비교연산자나 논리연산자를
# 이용한 표현식으로 구성
# 비교 연산자 : x > 100, y != 123
# 논리 연산자 : (x > 100) and (y != 123)

# if 조건식 :
#     수행할 문장
#
# if 조건식:
#     수행할 문장1
# else:
#     수행할 문장2

# 총점이 85 라고 할 때 80 ~ 89 이면
# '우' 라고 출력하는 조건문을 작성하세요
tot =85
if (tot >= 80) and (tot < 90):
    print('우')

# 나이가 18일때, 18보다 크고 20보다 같거나
# 작으면 '성년을 축하해!' 라고 출력하고
# 그렇지 않을 경우 '아직 성년이 되려면 멀었군!'
# 이라고 출력하는 조건문을 작성하세요
age = 19
if (age > 18) and (age <= 20):
    print('성년을 축하해!')
else:
    print('아직 성년이 되려면 멀었군!')

# if 문에서 조건식이 참일 경우
# 실행할 문장이 하나 이상인 경우
# 들여쓰기 위치를 일치시켜야함
a = 200
if a >= 100:
    print('100보다 크군요')
    print('이 문장도 보이나요?')

# 정수를 하나 입력받아
# 입력한 숫자가 짝수인지 홀수인지 검사
# 입력함수 : input(메세지)
# 형변환 : int(대상)
x = input('정수를 하나 입력하세요 : ')
x = int(x)

x = int(input('정수를 하나 입력하세요 : '))
if (x % 2 ==0):
    print('짝수입니다')
else:
    print('홀수입니다')

# 중첩 if 문
# if 문 속에 또 다른 if 문을 포함시켜 작성하는 조건문
# 조건문을 중첩할때는 들여쓰기에 유의해야함

# 평균이 73.5라 할 때 조건에 따라
# 수/우/미/양/가 학점을
# 출력하는 조건문을 작성하세요
avg = 73.5
if(avg >= 90):
    print('수')
else:
    if(avg >= 80):
        print('우')
    else:
        if(avg>=70):
            print('미')
        else:
            if(avg>=60):
                print('양')
            else:
                print('가')

# 다중 if 문
# 중첩 if 문을 작성하는 경우 조건이 많으면 다소 복잡함
# 이러한 중첩 if 문을 단순하게 작성할 수 있는 조건문이
# 다중 if 문임
# if 조건식1:
#     실행할문장1
# elif 조건식2:
#     실행할문장2
# else:
#     실행할문장3

avg = 73.5
if avg > 90:
    print('수')
elif avg >= 80:
    print('우')
elif avg >= 70:
    print('미')
elif avg >= 60:
    print('양')
else:
    print('가')

# 나이가 35이라 할 때 축하메세지 출력하기
# 1~18 : 유년을 축하해요!
# 19~30 : 성년을 축하해요!
# 31~40 : 장년을 축하해요!
# 41~50 : 중년을 축하해요!
age = 35
if (age >=1) and (age <=18):
    print('유년을 축하해요!')
elif (age >=19) and (age <=30):
    print('성년을 축하해요!')
elif (age >=31) and (age <=40):
    print('장년을 축하해요!')
else:
    print('중년을 축하해요!')

# 아이디가 abc123 이고 비밀번호가 987xyz 일 때
# 아이디나 비밀번호가 일치하지 않으면 '로그인 실패',
# 아이디와 비밀번호가 일치하면 '로그인 성공' 이라는
# 메세지를 출력하는 조건문을 작성하세요
id = 'abc123'
pw = '987xyz'
if (id != 'abc123') or (pw != '987xyz'):
    print('로그인 실패')
else:
    print('로그인 성공')

# 현재년도가 각각 1992, 2000, 2020 과
# 1900, 2000, 2100 에 대해 윤년여부를 출력하는
# 조건식을 작성하세요
# 윤년 : 4로 나눠 나머지가 0
# 윤년 : 4로 나눠 나머지가 0 이고
#       100으로 나눠 나머지가 0 이 아니면
# 윤년 : 400으로 나눠 나머지가 0
year = [1992, 2000, 2020, 1900, 2000, 2100]

year = int(input('연도를 입력하세요 : '))
if (year % 4 == 0) :
    print('윤년입니다')
elif (year % 4 == 0) and (year % 100 == 0):
    print('윤년이 아닙니다')
elif (year % 400 == 0):
    print('윤년입니다')
else:
    print('윤년이 아닙니다')

# 삼항 연산자
# 참일때 값 if 조건식 else 거짓일 때 값

x = int(input('정수를 하나 입력하세요 :'))

msg = ''
msg = '짝수' if x % 2 == 0 else '홀수'
print(msg)

print('짝수' if x % 2 == 0 else '홀수')

# 두 수를 입력받아 큰 수/작은수를 출력하는 코드를 작성하세요
num1 = int(input('정수를 하나 입력하세요 :'))
num2 = int(input('정수를 하나 입력하세요 :'))

min = num1 if num1 < num2 else num2
max = num2 if num1 < num2 else num1

print(f'큰수는 {max} 이고 작은수는 {min} 입니다')

# 세 수를 입력받아 큰 수/작은수를 출력하는 코드를 작성하세요
num1 = int(input('첫번째 숫자를 입력하세요 :'))
num2 = int(input('두번째 숫자를 입력하세요 :'))
num3 = int(input('세번째 숫자를 입력하세요 :'))

# num1, num2 비교
min = num1 if num1 < num2 else num2
max = num2 if num1 < num2 else num1

# min, max 와 num3 비교
min = num3 if min > num3 else min
max = num3 if max < num3 else max

print(f'큰수는 {max} 이고 작은수는 {min} 입니다')

