# 자료형(자료형태)

# ctrl + s = save

# ctrl + z = back(이전돌아가기)

#숫자형
'''
print(5) #정수

print(-10) #음수

print(3.14) #실수(소수)

print(1000) #큰숫자

print(5+3) #덧셈 

print(2*8) #곱셈

print(3*(3+1)) #괄호속 3+1을 먼저 구한후 3이랑 곱해줌
'''

#문자형
'''
print('풍선') # 문자형은 ''나 ""를 사용한다

print("나비")

print("zzzzzzzz")

print('케'*9) #문자와 숫자를 곱하면 그 문자가 곱해져서 나옴
'''


#불리안 < 참 / 거짓을 의미
'''
print(5 > 10) # 5가 10보다 크지 않기때문에 F

print(5<10) # 5가 10보다 작기 때문에 T
print(True)
print(False)
print(not True) #뒤(여기선 True)의 반대를 의미(출력)
print(not False) #여기선 True
print(not(5>10)) #여기선 5보다 10이 작기 때문에 False가 나와야하는데 앞에 not 이 붙어 True가 출력됨
'''

#변수
# -> 변수는 문장 중간에 들어갈수도 있음
# ex)애완동물을 소개해 주세요
'''
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3 #나이가 3살 이상이면 어른 adult로 본다


print("우리집 "+ animal + "의 이름은" + name + "예요") 
hobby = "공놀이" # 여기서 hobby를 선언하게되면 이 명령문 밑줄부터는 "산책"이 아닌 "공놀이"로 표시됨
print(name , "는 " , str(age) , "살이며," , hobby , "을 아주 좋아해요") # ,(콤마)는 띄어쓰기 형식 포함
print(name + "는 " + str(age) + "살이며," + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))
'''

#주석 (무시하는것-표기만되고 실행되지않음)
'''

이렇게 
''' ''' 혹은 """ """ 표시하면
긴주석

ctrl + / 일괄 #(주석)처리 <= 해제하는 경우에도 ctrl + / 하면 일괄 #(주석) 해제됨
'''

#연산자
'''
print(1+1) # 2
print(2-1) # 1
print(5*2) #10
print(6/3) #2

print(2**3) # **하게되면 2^3(2의3승) = 8
print(5%3) # %는 나누기 한 값의 나머지 즉 2
print(10%3) # 는 10나누기 3을 한 값의 나머지 즉 1
print(5//3) # //은 몫 구하기 <5나누기3 나머지를 제외한 1>
print(10//3) # 10 나누기 3한값 3

print(10 > 3) # 비교연산
print(4 >= 7) # 4는 7보다 크거나 같다 즉 False
print (10<3) # 3보다 작다 즉 False
print(5 <= 5) # 5는 5보다 작거나 같다 <= 이경우 5가 같기때문에 True

print(3==3) # (앞)3은 (뒤)3과 똑같다 즉 똑같기 때문에 True
print(2==4) # 2(앞)은 4(뒤)와 다르기 때문에 False
print(3+4 == 7) #이경우 3+4가 7이기때문에 True

print(1 != 3) # !=  <= 앞과 뒤가 같지 않을때 쓰는 기호
print(not(1 !=3)) # 앞(1)과 뒤(3)가 다르다 즉 True가 나와야하나 앞에 not이 붙어 False 가 출력됨

print(3 > 0 and 3<5) # and <= 앞 뒤 모두 만족하는경우에만 True <하나라도 만족하지 못하면 False
print(3 > 0 & (3 < 5)) # &으로도 and와 같은역활 

print((3 > 0) or (3 >5)) #or <= 둘중 하나라도 만족하는경우 True
print((3 > 0) | (3 > 5)) # (shift + 백슬래시) <= or 와 같은역활 (백슬래시가 두번 들어가면 escape sequence 에러 발생)

print( 5 > 4 > 3) #연속되는 값도 맞을경우 True
print(5 > 4 > 7) #이부분은 4 > 7 이 맞지 않기때문에 False
'''

#간단한 수식
'''
print(2 + 3 * 4) #이경우 3x4를 먼저 계산하고 2를 더함 = 14
print( (2+ 3) * 4) # 보라색괄호부터 계산하게도 가능 = 20
number = 2 + 3 * 4 # = 14

print(number) # 위에서 number 변수를 정해주고 밑에서 그 정한 변수에 더하는것도 가능
number = number + 2 
print(number) # = 16

number +=2 # 위와 동일하지만 바로 위 number에 더 쉽게 + 하는 쓰는코드방법 
print(number) # = 18
number *=2 # 바로 위의 number바로 곱하는방법
print(number) # = 36
number /=2 # 바로 위의 number을 바로 나누는 방법
print(number) # = 18
number -=2 #바로 위의 number을 - 하는방법 
print(number) # = 16
number %=5 # 바로 위의 number의 나눈 나머지 값(몫을 제외한)을 구하는방법
print(number) # = 1
'''

#숫자 처리 함수
'''
print(abs(-5)) # -5의 절대값을 구해줌 = 5

print(pow(4, 2)) # 4의2승 값을 구해줌 = 16

print(max(5, 12)) # 입력받은 두개의 값중에 최대값을 return = 12

print(min(5, 12)) # 입력받은 두개의 값중에 최소값을 retrun = 5

print(round(3.14)) # 반올림한 값을 구해줌 = 3

print(round(5.56)) # 반올림한 값을 구해줌 = 6 -위와동일-


from math import * # math 라이브러리를 이용하는방법 ( math 라이브러리의 모든것을 이용함(import) )
print(floor(4.99)) # 내림(뒤의값을 빼버림) = 4

print(ceil(3.14)) # 올림(뒤의값과 상관없이 올려버림) = 4

print(sqrt(16)) # 제곱근을 구해줌 = 4
'''

#랜덤함수 ( 무작위(난수)로 숫자를 뽑아줌 )
'''
from random import * # random 라이브러리를 사용해서 랜덤값 추출

print(random()) #  0.0 ~ 1.0 미만의 임의값 생성

print(random() *10) # 0.0 ~10.0 미만의 임의값 생성 

print(int(random() * 10)) # int를 해주면 소수점 자리를 생략 ( 0.0~10.0 미만 ) # 잘못된코드 - print(int(random()) *10) 이렇게하면 0만 출력됨

print(int(random() *10) +1 ) # 마지막에 +1을 해주면 1~10 이하의 임의값 생성

# ex) 로또값 추출하는 방법 [여러가지값 추출]
print(int(random() *45) +1)
print(int(random() *45) +1)
print(int(random() *45) +1)
print(int(random() *45) +1)
print(int(random() *45) +1)
print(int(random() *45) +1) 

# randrange ( random 모듈에 속한 함수로써 지정된 범위 내에서 임의의 정수를 반환 )
# randrange(start, stop) start값부터 stop값 미만의 값
print(randrange(1, 45)) # 1~ 45미만의 값을 생성

#randint ( 지정한 범위 내에서 임의의 정수를 생성 )
print(randint(1, 45)) # 1 ~ 45 이하의 값을 생성

# shuffle : 리스트의 항목을 임의로 섞음 (None을 반영)

# smaple: 주어진 시퀸스(리스트,튜플 등)에서 지정된 개수(1이면 1개, 2면 2개)만큼의 항목을 무작위로 선택하여 새로운 리스트로 반환

'''

# 문자열 (str)
'''

sentence = '나는 소년입니다' # 작은따옴표도 str
print(sentence)

sentence2 = "파이썬 easy" # 큰따옴표도 str
print(sentence2)

sentence3 = """나는 소년이고,파이썬 easy""" # 긴주석처리하는 방법으로 하게되면 한번에 많은 줄을 작성가능
print(sentence3)

sentence4 ="""
나는 소년이고, 
파이썬은 easy
""" # 이렇게 할경우 줄바꿈까지 출력되서 나옴 
print(sentence4)
'''

# 슬라이싱
'''

jumin = "970120-1234567"
print("성별 : " + jumin[7]) # 필요한것만 가져오고싶은경우 []를 사용 -> 이경우 1개만 출력가능

print("연 : " + jumin[0:2]) # 필요한것을 2개 이상 가져오고싶은경우 :(클론) 사용 ex-> 0:2는 0부터 2미만 즉 0~1까지임 

print("월 : " + jumin[2:4]) # 2~4직전까지 즉 (2,3) 값

print("일 : " + jumin[4:6]) # 4~6직전까지 즉 (4.5) 값 

print("생년월일 : " + jumin[:6]) # 0없이 :6로 사용가능 <처음부터 6직전까지 출력> 

print("뒤 7자리 : " + jumin[7:]) # 7: 으로 사용가능 <시작점부터 끝까지 출력>

print("뒤 7자리 (뒤부터) : " + jumin[-7:]) # 맨뒷자리는 -1부터 시작함 [맨뒤에서 7번째부터 끝까지]
'''

# 문자열(str) 처리 함수
'''
python = "Python is Amazing"
print(python.lower()) # lower() 는 전체 소문자처리

print(python.upper()) # upper() 는 전체 대문자처리

print(python[0].isupper()) # isupper() 는 [] 넣은값이 대문자인지 확인 -> 이때 변수뒤에 [] 를 넣어야함

print(python[0].islower()) # islower() 는 [] 넣은값이 소문자인지 확인 - ex) 변수[].islower()

print(len(python)) # len() 은 전체문자 길이수 확인 [이때 띄워쓰기까지 포함됨]

print(python.replace("Python", "Java")) # replace()는 (바꾸고싶은변수, 바꿀변수) 해주면 바꿔줌 -> 이경우 Python 에서 Java 로 변경

index = python.index("n")  #index 변수는 시퀀스 자료형의 요소들을 가리키는 번호 [ 어떤 문자가 어떤 위치(숫자)에 있는지 확인해줌 ]
print(index) # index("찾고싶은글자") 해주면 됨 위에선 "n"

index = python.index("n", index + 1) # 앞에서 찾은 위치(index)값 그 다음값(index+1) 즉 6다음부터 찾을수있음 
print(index) # index("찾고싶은글자", index+1) -> 즉 위에 g를 넣으면 위에 index 설정한 n(5) 그 다음값부터 찾는걸 시작함 = 16 

print(python.find("n")) # find()는 원하는 글자의 위치를 찾아줌 
print(python.find("Java")) # 만약 없는걸 찾는경우 -1값을 return
# print(python.index("Java")) # 파이썬이라는 변수에 Java가 없기때문에 Error 발생
print("hi") # 만약 위에서 없는걸 찾는경우 Error 지점부터 출력이안됨

print(python.count("n")) # count()는 내가 원하는 글자가 몇개(몇번) 있는지 출력해줌 -> 여기선 2번 
'''

#문자열 포맷
'''
# print("a" + "b") # + 이렇게 할경우 a와 b가 같이 출력(이경우는 붙어써짐) -> b앞에 띄워놓으면 띄워서 출력은 가능
# print("a","b") # , 로 할경우에도 a와 b가 같이 출력 (이경우는 띄워써짐)

#방법 1
print("나는 %d살입니다." %28) # %d 경우 뒤에붙은 %(원하는숫자)를 return 여기서 d는 정수를 의미(즉 정수값만 입력가능)
print("나는 %s를 좋아해요." %"파이썬") # %s 경우 뒤에붙은 %(원하는글자)를 return 여기서 s는 str을 의미
print("Aplle 은 %c로 시작해요." %"A" ) # %c 경우 한 글자만 받아서 return

# %s : %s로만 쓰면 정수, 문자 상관없이 출력가능
print("나는 %s살입니다." %28)

# %s로 두개이상의 값을 넣는방법
print("나는 %s색과 %s색을 좋아해요." %("파랑", "빨강")) # %(( , ))를 통해서 ("원하는값", "원하는값") 이 순서대로 출력됨

#방법2
print("나는 {}살입니다.".format(28)) # {}로 앞에 적어주고 .format("원하는값")을 하게되면 return해줌

# .format으로 두개이상(연속적으로)의 값을 넣는방법
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨강")) # {}를 원하는만큼 넣어주고 .format( , ) 하면됨

print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨강")) # {원하는숫자순서} 와 {원하는숫자순서} 를 해주게되면 그 값에 알맞게 바뀌어 출력됨

#방법 3
print("나는 {a}살이며, {b}색을 좋아해요".format(a = 20, b="빨강")) # .format(변수=(int) , 변수="(str)" 해줄경우 변수값을 괄호속에 집어넣을수도 있음 int str 상관은 없음
print("나는 {age}살이며, {color}색을 좋아해요".format(color ="빨강", age =20)) # 이때는 순서가 바뀌는게 아니라 정의한 값 그대로 순서상관없이 출력

#방법 4 (f-string은 파이썬 3.6 이상에서 사용할 수 있는 문자열 포매팅 방식으로 중괄호 내에 변수나 표현식을 집어넣을수 있음)
age = 20
color = "Red"
print(f"나는 {age}살이며, {color}색을 좋아해요") # f로시작 할경우 위에서 지정한 변수값을 출력
'''

# 탈출문자
'''
# \n : 줄 바꿈
print("백문이 불여일견 백견이 \n불여일타 ") # /n : 줄바꿈

# ""이나 ''을 포함해서 출력하는 방법
print("저는 '이진규'입니다") # 큰따옴표와 작은따옴표가 구분되어있는경우는 그냥 사용이 가능함

print("저는 \"이진규\"입니다") # (다만  같은 따옴표가 있어야하는(붙어서있는) 경우 \필요 \는 필요한 " 부분의 앞에다 써야함) 

# \\ : 문장 내에서 하나의 \로 출력됨

print("\\") # print("\") 할경우 Error
print("c:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories") # 마찬가지로 원하는 \앞에 \를 붙이는거
print("c:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories") # 이경우 원래 출력이 안되야하지만 출력이 되는데 이유는 모르겠음

# \r : 커서 맨앞으로 이동 (덮어씌워짐)
print("Red Apple\rPine") # \r을 통해서 맨앞으로 이동시킴( 이전에 출력한 내용을 덮어 씀 여기선 Red가 덮어짐 )

# \b : 백스페이스 (한글자 삭제) - 커서를 한 칸 앞으로 이동시켜 이전 문자를 지우는 역할
print("Redd\bApple") # \b앞글자를 지워줌
print("ABCD\b") # 이 경우 \b의 ABCD가 그대로 출력됨 아마 \b뒷글자가 없어서 그런거같음 (백스페이스의 동작 방식이 "D"를 지우지 않고 그대로 출력하는 경우)

# \t : 탭(tab)
print("Red\tApple") # 키보드에서 tab과 같은 효과를 냄
'''

# 리스트 [] - 순서를 가지는 객체의 집합
'''
# ex) 지하철 칸별로 10명, 20명, 30명 
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["유","조","박"] # 0, 1, 2
print(subway)

# ex) 조씨가 몇번째 칸에 있는가?
print(subway.index("조"))

# ex) 하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하") # append() : 맨뒤에 추가(+)하다
print(subway)

# 정씨를 유 / 조 사이에 태워봄
subway.insert(1, "정") # insert() : 지정한 숫자에 넣을수있음 1로 지정하면 1번 0으로 지정하면 0번
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
subway.pop() # pop() : 리스트에서 마지막 요소를(뒤에서부터) 제거(혹은 반환) 
print(subway)

# 같은 이름(변수)의 사람이 몇 명 있는지 확인
subway.append("유") # appned 함수로 추가
print(subway) 
print(subway.count("유")) # .count("")로 몇 명(몇 개) 인지 확인 

# 순서대로 정렬하는 방법 sort() : 오름차순으로 정렬
num_list = [5,2,4,3,1]
num_list.sort() # sort() : 작은숫자부터 큰숫자 순서대로 정렬 
print(num_list)

# 순서를 반대로 정렬하는 방법 (뒤집어서) reverse() : 내림차순으로 정렬
num_list.reverse() # reverse() : 큰숫자부터 작은숫자 순서대로 정렬ㅉ
print(num_list)

# 모두 지우기 .clear() : list안 모든것 지움
num_list.clear() # .clear() : list 초기화
print(num_list)

# 다양한 자료형과 함께 사용
mix_list = ["조",20,True] # str, int, 불리안과 함께 사용한경우 
print(mix_list)

# 리스트 확장(합치기) .extend() : 리스트의 끝에 다른 리스트의 요소를 추가 (다른 리스트나 이터러블 객체 모든 요소 추가)
num_list = [5,2,4,3,1]
mix_list = ["조",20,True]
num_list.extend(mix_list) # .extend : 이경우 num_list 뒤에 mix_list가 확장(뒤에 붙어)되어 나옴
print(num_list)
'''

#사전 {} 로 사용 (키의 대한 중복이 허용되지않음) -3번을 또 다른 데이터가 받을수 없음
'''
# {} : 원하는 key에 원하는값(value) 할당
cabinet = {3:"유재석", 100:"김태호"} # 키는 3이고 데이터는 유재석이다, 키는 100이고 데이터는 김태호다. (즉 3번은 유재석, 100은 김태호다.)
print(cabinet[3]) # 변수[ 입력할 키 번호 ]로 사용 -> 여기서는 cabinet이기 때문에 cabinet[]으로 사용함 이때는 [] 를 사용
print(cabinet[100]) # 이경우는 100번을 입력했으니 김태호가 출력됨

# .get() : key에 어떤값(value)이 있는지 출력
print(cabinet.get(3)) # .get( 입력할 key 번호 ) 으로도 사용이 가능함. 이때는 ()를 사용함
print(cabinet.get(5)) # .get( 없는 key ) 를 할경우에는 출력이 가능하지만 None으로 값이없다고 나옴.
print(cabinet.get(5, "사용가능")) # 없는 값을 가지고오고싶은경우 (기본값을 사용하려는 경우) 5뒤에 있는 값인경우 출력이되고 없는경우 원하는값, "뒷부분" 이 출력이됨
print(cabinet.get(3, "사용가능")) # 만약 있는 값을 입력하게 되면 뒷부분("사용가능")은 출력되지않고 입력한 값(3) 이 출력됨
# print(cabinet[5]) - cabinet[] 으로 없는 번호를 지정할경우에는 여기부터 프로그램이 종료됨
# print("hi") - 즉 hi가 출력되지 않게된다.

# in : in 함수로 값이 존재하는 여부를 확인하는 방법
print(3 in cabinet) # 여기서 (원하는key : 번호) in cabinet(변수) 를해주게되면 있는지 여부를 있는경우 T 없는경우 F 로 출력됨 -> 이 경우 있기때문에 T 가 출력
print(5 in cabinet) # 이경우 없기 때문에 F 가 출력됨

#정수(숫자)가아닌 str도 가능함
cabinet = {"A-3":"유", "B-3":"김"} # str로 사용할경우 ""를 사용하여 "원하는값":"원하는값" 해주면 됨
print(cabinet["A-3"]) # 이때는 []를 사용해서 출력을 한 예제임
print(cabinet["B-3"]) # 위와 마찬가지

# [] = "" : 새로운 값 추가 (새 손님)
print(cabinet)
cabinet["C-20"] = "조" # [원하는key] = "원하는값" 을 해줄경우 할당한 값에 추가가됨 (만약 추가하려는 값이 이미 있는경우 업데이트가 됨)
print(cabinet)
cabinet["A-3"] = "박" # 이미 있는값을 입력했기떄문에 "유" 가 "박" 으로 업데이트 되어 바뀌어 출력됨
print(cabinet)

# del : 값을 빼려는경우 (간 손님)
del cabinet["A-3"] # del 함수를 사용하면 내가 지정한값이 제외(빠짐)됨
print(cabinet) 

# .keys() : key 들만 출력 
print(cabinet.keys()) # .keys를 해줄경우 key의 대한 값만 출력됨

# .values() : value(지정한값) 들만 출력
print(cabinet.values()) # .values를 해줄경우 지정한값(value) 만 출력

# .items() : key, value 를 쌍(동시에)으로 출력
print(cabinet.items()) # .items 를 해줄경우 key와 value가 동시에 출력된다.

# .clear() : 지정한 모든 key 와 value를 초기화 (목욕탕 폐점)
cabinet.clear()
print(cabinet)
'''

# tuple : 값(value)들을 저장하는 컨테이너 -> ( , ) 로 사용함 [tuple은 값 추가(변경) 불가능] 한개의 요소를 가지는경우에도 마지막에 , 를 붙여야함 ex-> menu = (돈까스,)
'''
menu = ("돈까스", "치즈돈까스") # tuple을 사용할경우 ()로 열고닫고 ,로 구분하여 ( "value", "value") 해주면됨
print(menu[0]) # 출력하고자 사용할때는 변수[]로 사용한다 
print(menu[1])

# menu.add("생선까스") # tuple은 원하는값을 추가할수 없음 그래서 add 사용이 불가

name ="김종국"
age = 20
hobby = "코딩"
print(name, age, hobby) # ,로 구분하여 사용해야함
# print(name + age + hobby) + 로 사용이 불가능  

name, age, hobby = "김종국" , 20, "코딩" # ,를 사용하면 이렇게 한번에 값을 지정할수 있음 0,1,2 순서대로 0-0 , 1-1, 2-2 에 출력이 됨
print(name, age, hobby)
'''

# set : 집합 -> 중복 안됨, 순서 없음 [변수 = set([1,2,3]) 으로도 사용이가능함 -> 변수 =set 으로 사용할경우 (), [], {} 중 아무거나 사용가능
'''
a = set([1,2,3]) # set() : 변수 = set() 으로 사용할 경우는 (()), ([]), ({}) 전부 사용이 가능함
print(a)

my_set = {1,2,3,3,3} # _set : 변수_set 으로 사용할 경우엔 무조건 {} 을 사용해야함 [set의 경우에는 {}안에 값만 나열하면됨] 중복 허용X
print(my_set) # 중복이 허용되지 않기때문에 3이 1개만 출력

java = {"유","김","양"}
python = set(["유","박"])

# & : (교집합) -> 2개 이상의 변수값(value)에 동시(동일)하게 들어가있는 값을 출력해줌 [ 변수 와 변수 두개의 모두 있는경우]               ex)쉬운설명 : <java 와 python 을 모두 할수 있는 개발자>
print(java & python) # &을 사용하여 위의 값을 받아 교집합 값이 출력됨

# .intersection() : .intersection("변수") 로 교집합 값이 출력
print(java.intersection(python)) # .intersection() 으로 위와 마찬가지로 교집합 값을 출력해줌

# | : 합집합 (java 나 python 의 하나라도 있는 경우) -> 중복값은 같이출력                             ex)쉬운설명 : <java를 할수 있거나 python 할수 있는 개발자 (두개중 하나라도 할수 있는경우)>
print(java | python) # 이때는 입력한 2개 이상의 변수 모든값이 출력됨

# .union() : 합집합 (이경우도 위와 마찬가지로 2개 이상의 변수안의 모든값 출력)
print(java.union(python)) 

# 차집합 : 한 집합에서 다른 집합에 포함된 요소들을 제외한 나머지 요소들의 집합을 의미                                                  ex쉬운설명 : <java를 할수 있지만 python은 모르는 개발자>
# - : (변수 - 변수) 로써 사용됨 -> 즉 java엔 있지만 python엔 없는 값이 출력(결국 java값만 출력됨 중복을 제외)
print(java - python) # 이경우 java 변수에서 python 변수를 제외한 값 즉 {"양","김"} 이 출력 (즉 python 의 변수만 남게됨 중복값은 제외)
print(python - java) # 이경우 python 변수에서 java 변수를 제외한 값 즉 {"박"} 이 출력 (즉 java의 변수만 남게됨 중복값은 제외)

# .difference() : 변수.difference(변수) 로 사용됨 -> 위와 동일
print(java.difference(python))

# .add : 변수에 값을 추가                                                                                                          ex) 쉬운설명 : python 할줄 아는 사람이 늘어난 경우
python.add("김") # .add("value") 를 해주게되면 변수에 값이 추가됨
print(python)

# .remove() : 변수에 값을 뺌                                                                                                                 ex)쉬운설명 : java 를 까먹은경우 
java.remove("김") # .remove("value") 를 해주게되면 변수에 값이 빠짐()
print(java)
'''

#자료구조형의 변경
'''
# ex)커피숍
menu = {"커피", "우유", "주스"} # {} 를 사용하여 set로 정의됨
print(menu, type(menu)) # ,type() :  ,type(변수) 해주게되면 변수의 class가 나오게됨 -> 이경우는 set 

# class(type) 변경방법 
menu = list(menu) # set 을 list로 변경 : 변수 =list(변수) 해주게되면 type을 변환 -> 이경우 위의 set을 list로 변환
print(menu, type(menu)) 

menu =tuple(menu) # list 을 tuple로 변경 : 변수=tuple(변수) 해주게되면 tuple로 변환해줌
print(menu, type(menu))

menu = set(menu) # tuple 을 다시 set 으로 변경 : 변수 =set(변수) 해주게되면 set 로 변환
print(menu, type(menu))

'''

# if 
'''
weather = "맑음"                 
# weather = input("오늘 날씨는 어때요:") 하게되면 터미널로 값을 받아 그 값에 맞는 문구를 리턴 
if weather == "비" or weather == "눈": # 여기서 or는 또다른 변수값을 설정해주는것을 의미( or는 두개중 1개만)
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else :
    print("오늘은 날씨가 좋습니다")
'''
temp = int(input("기온은 어떤가요?")) # 기온은 숫자기때문에 int로 변환 => input은 항상 str로 받음
if 30 <= temp: # <= : 비교 연산자 (temp라는 변수의 값이 30보다 크거나 같은지를 확인)
    print("너무 더우니 나가지 마세요.")
elif 10 <= temp and temp < 30: # 10보다 크거나 같으면서 30보다 작거나 [여기서 temp는 그냥 변수임]
    print("괜찮은 날씨입니다")
elif 0 <= temp and temp <10: # 0보다 크거나 같으면서 10보다 작은
    print("외투를 챙기세요")
else: # 0보다 적을경우
    print("너무 추우니 나가지 마세요")