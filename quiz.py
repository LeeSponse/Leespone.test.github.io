# quiz1) 변수를 이용하여 다음 문장을 출력하라
# 변수명 : station              변수값 : "사당,신도림,인천공항" 순서대로 입력(1번씩)
# 출력문장 : xx행 열차가 들어오고 있습니다

station = "인천공항"

print(station + "행 열차가 들어오고 있습니다")

# quiz2) 당신은 최근에 코딩 스터디 모임을 새로 만들었다.
# 월 4회 스터디를 하는데 3번은 온라인 1번은 오프라인으로 함
# 아래 조건에 맞게 오프라인 모임 날짜를 정해주는 프로그램을 작성하라

# 조건 1 : 랜덤으로 날짜 생성
# 조건 2: 월별 날짜는 다름을 감안하여 최소 28이내로 정함
# 조건 3: 매월 1~3일은 제외

#(출력문 예제) 오프라인 스터디 모임 날짜는 매월 x일로 선정됨

from random import*

a= randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" + str(a) + "일로 설정되었습니다")

# 혹은

date = randrange(4, 29)
print("오프라인 스터디 모임 날짜는" + str(date) + "일")

# quiz3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성

# ex) thtps://naver.com
# 규칙 1 : https:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                   nav               (5)              (1)          (!)
# ex) 생성된 비밀번호 : nav51!

url = "https://naver.com" # 1번 변수 생성
my_str = url.replace("https://", "") # my_str이라는 2번변수를 생성해서 1번변수 url의 https://를 ""로 바꾸겠다(변환) 즉 앞에 사라짐 
print(my_str)
my_str = my_str[:my_str.index(".")] # my_str이라는 변수에 들어가있는 문자열중에 처음부터 처음나오는 .의 직전까지 출력 my_str[0:5] -> 0~5직전까지(0.1.2.3.4) <변수 = 변수 중요>
print(my_str)
# my_str = my_str[0:5] 이렇게도 가능함 중요한건 변수 = 변수다 라고 꼭 해줘야함
# print(my_str) 

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # 이떄 str()로 감싸주는것 매우중요!
# [:3] 은 0~3미만(0~2)까지 
# len() 함수는 길이(글자갯수) 
# .count() 함수는 e가 몇개 있는지  
print("{0}의 비밀번호는? {1}입니다".format(url, password)) 
#결과값은 [:3]의 0.1.2 즉 nav + len() 즉 5글자니까 5 + .count() 여기서는 e가 들어갔고 e가 1개니까 1 + "!" 로써 nav51! 이 결과값으로 추출된다 
#마지막으로 print("{}과 {}".format(url, password)) 로 가져와주면 됨 (.format은 두개이상의 값을 가져옴)

# 이렇게도 위와 동일한 값을 구할수 있음
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

# quiz4) 당신의 학교에서는 파이썬 코딩 대회를 주최함
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 함
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게됨
# 추첨 프로그램을 작성하라

# 조건 1 : 편의상 댓글은 220명이 작성하였고 아이디는 1~20 이라고 가정
# 조건 2: 댓글 내용과 상관없이 무작위로 추첨하되 중복불가
# 조건 3 : ranaom 모듈의 shuffple 과 sample 을 활용

#(출력예제)
# --당첨자 발표--
# 치킨 당점자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다--

#(활용 예제)
# from random import*
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(sample(lst, 1))

'''
from random import*
lst = [1,2,3,4,5]
print(lst)
shuffle(lst) # shuffle() : shuffle(변수) 를 사용하게되면 list 값을 무작위로 섞어줌
print(lst)
print(sample(lst, 1)) # sample() : sample(변수, 원하는갯수) 해주게되면 원하는갯수 만큼 랜덤으로 값이 나옴
# print(sample(lst,2)) # -> 이경우는 2로 입력했기때문에 2개의 값이 반환
'''

from random import*
users = range(1,21) # range() : 1~20까지
print(type(users)) # type이 range라 list함수를 사용불가
users = list(users) # range 타입을 list 타입으로 변환
print(type(users)) # 즉 list로 바뀜

print(users) # users의 값 출력 (1~20까지)
shuffle(users) # shuffle 로 값을 랜덤하게 섞어줌(순서변경)
print(users)

winners = sample(users, 4) # sample(users, 4)로 4개의 값을 랜덤으로 추출해줌  ex) -> 4명중 1명은 치킨 3명은 커피를 주면됨

print( "-- 당첨자 발표 --")
print( "--치킨 당첨자 --: {0}".format(winners[0])) # "{}".format(변수[원하는번수])해주면 -> 0의 값을 가져옴 
print( "--커피 당첨자 --: {0}".format(winners[1:])) # "{}".format(변수[시작번수:])해주면 -> 1,2,3 가져옴 [여기선 4개의 값만 추출 즉 0,1,2,3 만 추출]
print("-- 축하 합니다 --")

