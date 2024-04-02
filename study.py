# quiz2) 당신은 최근에 코딩 스터디 모임을 새로 만들었다.
# 월 4회 스터디를 하는데 3번은 온라인 1번은 오프라인으로 함
# 아래 조건에 맞게 오프라인 모임 날짜를 정해주는 프로그램을 작성하라

# 조건 1 : 랜덤으로 날짜 생성
# 조건 2: 월별 날짜는 다름을 감안하여 최소 28이내로 정함
# 조건 3: 매월 1~3일은 제외

#(출력문 예제) 오프라인 스터디 모임 날짜는 매월 x일로 선정됨

from random import* # random 이라는 라이브러리를 입력해줌(그래야 받아올수있다) - 여기서 조건1번 클리어

date = randint(4, 28) # randint를 사용하면 4~28까지의 값이 나온다 - 여기서 조건 2,3번이 클리어
print(date) # date 변수를 출력

print("오프라인 스터디 모임 날짜는 매월" + str(date)  + "일로 선정됨") # 이때 str() 함수를 사용해서 str(date)로 묶어주지 않으면 문자열로 인식이 안되기때문에 str()함수사용이 필요함
#str(date)를 사용하여 date 변수의 정수값을 문자열로 변환해줌 <date값이 int이기 때문>

#이렇게도 구할수 있다
'''
date = randrange(4, 29) # randrange를 사용하면 4~29미만까지 값이 나온다
print(date)
'''


# quiz3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성

# ex) thhps://naver.com
# 규칙 1 : https:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                   nav               (5)              (1)          (!)
# ex) 생성된 비밀번호 : nav51!

#규칙1
'''
url = "https://naver.com" # url이라는 변수를 생성해서 "" 지정해주고
a = url.replace("https://", "") # a 를 url (a = url.replace) 이라고 값을 받아준다 
print(a) # 이렇게 해주면 url 이 a로 받아져서 a의 값이 출력된다

#규칙2
a = a[:5] # 이값을 구할땐 a는 naver이기 때문에 nav의 값을 얻기 위해서 다시 a = a[:5]으로 값을 정의해준다 a[:5] 도 되긴하는데 이경우는 안되는듯
print(a) # 이렇게하면 naver 이 정상적으로 출력된다 (0.1.2.3.4)의 값

password = a[:3] + str(len(a)) + str(a.count("e")) + "!" # a[:3]은 = nav + str(len(a)) = 5 + str(a.count("e")) = 1 즉 nav51 마지막에 +"!" 가 되서 nav51! 이 된다 
# 이떄 str()함수를 써주는 이유는 len()길이함수 즉 int고 .count()도 int로 나오기때문에 문자열인 str로 변환해줘야 한다
print("{}의 비밀번호는 {}이다".format(url, password)) 
'''

# 이렇게도 값을 구할수 있음
'''
url = "https://naver.com"
a = url.replace("https://", "")
print(a)

a1 = a[:5]
print(a1)

a2 = a[:3]
print(a2)

a3 = str(len(a1))
print(a3)

a4 = str(a.count("e"))
print(a4)

password = a2 + a3 + 
print("{0}의 비밀번호는{1}".format(url, password))a4 + "!"
'''