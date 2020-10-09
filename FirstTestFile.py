# print("ok?")
# print (not  False)

# print( "sldfjlsdf" , end = " ") # 출력하고 출 안바꿈

# age = 15
# is_adult = age > 3
# print ("is_adult : ", is_adult)

# print ("내 나이는 " + str(age) + "입니다.")
# print ("내 나이는 " , age ,"입니다.")  # 콤마는 변수 변환을 안해도 되지만, 강제로 한 칸 띄운다.
 
# '''긴 주석입니다.
# gkgkkgkgkgk
# sdfsd
# fs
# f
# s
# '''
# print (5/3) # 1.6666666666666667
# print (5//3) # 1
# print (5%3) # 2
# print(3**3) # 27

# print ((3>0) or ( 2>3) )
# print ((3>0) | ( 2>3) )
# print ((3>0) and ( 2>3) )
# print ((3>0) & ( 2>3) )


# print (abs(-5))
# print(pow(4,2))
# max(5,11)
# min(5,11)
# round(3.32)


# #올림 내림 제곱근
# from math import *
# print(floor(2.55)) #내림 (정수)
# print(ceil(3.33)) #올림 (정수)
# print(sqrt(16)) #제곱근   (실수)


# #랜덤
# from random import *

# print(random())  # 0.0~ 1.0미만
# print ( random()*10) # 0.0~ 10.0미만
# print(int(random()*10))# 정수로 0~10 미만


# print (int(random() * 45) + 1) # 1~ 45 이하
# print (randrange(1,46)) # 1~ 46 미만
# print (randint(1,45)) # 1~45 이하 (양 끝 포함)

# #리스트를 다시 섞기 shuffle
# listtt = [1,2,3,4,5,6]
# shuffle(listtt)
# print ("shuffle : " , listtt)

# #리스트에서 무작위로 뽑기 sample
# print("pick : " , sample(listtt,2))  # 2개 무작위로 뽑기 (리스트로 반환)


# #문자열
# string1 = "하하하하"
# string2 = """무슨일인가 자네
# 응?"""   # 엔터와 스페이스 모두 인식함
# print(string1)
# print(string2)


# # 슬라이싱
# teststring = "01234567"
# print ( " 123 : " , teststring[3:5]) # 34  끝자리 포함x
# print ("[:3] : ", teststring[:3]) # 012  처음부터 인쇄
# print ("[3:] : ", teststring[3:]) # 34567  끝까지 출력
# print ("[-1] : ", teststring[-1]) # 7  


# teststring = "Mamamamama Hahahahaha"

# print(teststring.lower()) # 소문자
# print(teststring.upper()) # 대문자
# print(teststring[0].isupper()) # 대문자니? True
# print(len(teststring)) # 길이

# print(teststring.replace("a", "b")) # 교체 한 값을 반환 (원래 스트링은 변화 없음)
# index = teststring.index("H")   # 만약 없으면 오류남
# print("index(index) :" , index)  
# index = teststring.index("H", 3)   # 인덱스 3자리 부터 찾기시작해


# index = teststring.find("b") # 만약 없어도 오류 안 남   -1 을 반환함
# print("index (find):" , index)

# print("count : " , teststring.count("a"))  # 문자열에서 a 의 개수 수 갯수



 
# # 출력 변수 포함
# print ("내 이름 %s이다." %"윤윤")   #   아무거나 다 받을 수 있음.
# print ("내 이름 %s이다." %123123)
# print ("내 이름 %d이다." %123)
# print ("내 이름 %c이다." %"e")
# print ("내 이름 %s그리고 %s이다." %("123", "gkgkgk"))


# print ("나는 {}를 좋아해".format(123))
# print ("나는 {}를 좋아해".format("gkgk"))
# print ("나는 {}와 {}를 좋아해".format("gkgk", "aaaa"))
# print ("나는 {1}와 {0}를 좋아해".format("gkgk", "aaaa"))


# print ("나는 {aaa}를 좋아하고, {abc}는 싫어해".format(abc = "qqqq", aaa = "123123"))  # 선언 순서는 무관.


# aaa = "111"
# bbb = "bbbb"
# print(f"하하하ㅏ하{aaa} 그리고 {bbb} 는 뭐지") # 변수를 그대로 사용가능 ( 앞에 f 를 붙인거다.)


# # \\
# # \n
# # \r 커서 맨 앞으로 이동(이후 또 출력하면 덮어쓰게됨)
# # \t 

# #일부 문자 삭제는 교체를 이용함
# sstr = "abcdefgh"
# result = sstr.replace("bcd", "")
# print(result)




# ##### 리스트 ######
# # 만들기
# asdf = []
# asdf = list()


# llist = [ "가", "나나나", "다라"]
# print(llist.index("나나나")) # 1  위치찾기

# llist.append("캬캬캬")  # 원소 추가
# print(llist)

# llist.insert(1, "윤윤윤") # 넣을 위치 index  원소 삽입
# print(llist)


# print(llist.pop()) # 맨 뒤에 원소 꺼내어 반환
# print(llist)

# print(llist.count("나나나")) #나나나 원소 가 몇번 있는지

# # 원소들이 숫자일때 리스트 안 숫자 모두 더하기
# listt = [1,2,3,4,5]
# count = sum(listt)

# # 원소가 존재하는지 확인하기
# print(1 in listt)  #True

# # 정렬
# llist.sort()
# print(llist)
# llist.reverse()
# print(llist)

# llist.clear()  #모든 원소 삭제
# print(llist)


# #리스트 합치기 합체
# llist = ["123", "eeee", "ttttt"]
# llist2 = [1,2,3,4,5]
# llist.extend(llist2)
# print(llist)





# ####   사전   ####
# #만들기
# ddic = dict()
# ddic = {}

# ddict = { 1 : "aaa" , 200 : "bbb"}

# print(ddict[200])  #해당인덱스(키)가 없으면 에러남
# print(ddict.get(300)) # 에러 안 나고 None 을 반환
# print(ddict.get(300, "hi")) # 에러 안 나고 hi 을 반환

# print (200 in ddict) # 200 이라는 키가 존재하는지 True
# print (300 in ddict) # 200 이라는 키가 존재하는지 True

# ddict2 = { "A" : "aaa" , "B" : "bbb"}
# print(ddict2["A"])  
# ddict2["333"] ="윤윤윤" # 새로운 키의 새로운 값을 추가함
# print(ddict2)

# del ddict2["333"]   # 키를 이용해서 원소 삭제
# print(ddict2)

# print(ddict2.keys()) # 모든 키들을 출력
# print(ddict2.values()) # 모든 값들을 출력

# print(ddict2.items()) # 키. 값을 쌍으로 출력
# print(ddict2)

# ddict2.clear ()  # 모두 삭제


# ### 튜플 ###
# # 원소 추가 불가. 삭제 불가. 속도 빠름

# # 만들기
# asdf = tuple()
# asdf = ()

# tutu =("aaa", "bbb")
# print (tutu[0])

# a1 = "23234"
# a2 = "ddddd"
# a3 = "mmmmm"
# b1, b2 , b3 = "sd", "df", "fg"
# print ("b2 : ", b2)


# ### 집합 ( set)  ###
# #중복없음. 순서 없음 ( 연산 결과의 순서도 보장되지 않는다 )
# setset = {0, 1,1,2,3,4,4,5}
# print(setset)

# #리스트를 집합(세트)으로 만들기
# aaaa = set([1,2,3,3,3,4,5,6,7])
# print (aaaa)


# # 교집합
# print("hap : ", aaaa & setset)
# #같음 print("gyo : ", aaaa.intersection(setset))

# # 합집합
# print("hap : ", aaaa | setset)
# #같음 print("hap : ", aaaa.union(setset))

# # 차집합

# print("hap : ", aaaa - setset)
# #같음 print("hap : ", aaaa.difference(setset))


# # 원소 추가
# aaaa.add("카카카")
# print(aaaa)

# # 원소 제거
# aaaa.remove("카카카")
# print(aaaa)




# # 자료구조 변경

# menu ={ "aaa", "bbb" , "ccc"}
# print ( menu , type(menu))

# menu = list(menu)
# print ( menu , type(menu))

# menu = tuple(menu)
# print ( menu , type(menu))

# menu = set(menu)
# print ( menu , type(menu))
# users = range(1,21)    # 1~ 20   type : range
# users = list(users) # type : list



# answer = input("any question?") # 입력받기를 기다리며, 입력은 어제나 str로 받게 됨

# numbers = int(input("any number?")) # 숫자로 받기 


# # # if문 형식  ( 콜론을 빼면 안된다! )
# if 3 > 0 :
#     print("")
# elif 3 > -1 :
#     print ("")
# else : 
#     print("")



# # for문 형식 ( 콜론을 빼면 안된다! )
# for eachNum in [1,2,3,4,5]:
#     print("num : ", eachNum)

# for eachNum in range(1,7):   # 1,2,3,4,5,6
#     print("num : ", eachNum)


# # while 문 형식

# while True : 
#     print("")

#     break



# numset = [1,2,3,4,5]
# print(numset)
# numset = [i + 100 for i in numset]  # 모든 원소에 100 더하기
# print (numset)

# namelist = [ "Iron man" , "Thor", " I am groot"]
# namelist = [ len(i) for i in namelist]
# print(namelist)

# namelist = [ "Iron man" , "Thor", " I am groot"]
# namelist = [ i.upper() for i in namelist]  # 모두 대문자로
# print(namelist)




# ### 함수 ###
# def namedede (num, count) :
#     print("")

#     return False , 123, "sdkfj"   # 튜플 형식으로 반환 가능


# result1, result2, result3 = namedede(12,342) # 호출과 리턴받기


# #코드 줄바꾸기 팁 Tip
# # \ 하고 엔터하면 같은 줄로 인식함
# print("sdlkfjsldfjklsd\
# lllllllll")


# namedede (count = 123, num =222) #키워드를 명시해서 함수를 호출하면 순서가 틀려도 됨


# # 함수 기본값   : 입력받지 않았더라도 이 값을 사용함. self Q : 첫 변수를 기본값주면 뒤에도 다 줘야함, 즉 기본값 생략은 첫 변수 하나만 가능
# def namedede22 (numsdf, count=123, sdfsd=123) :
#     print("")

#     return False , 123, "sdkfj"   # 튜플 형식으로 반환 가능

# # print( "sldfjlsdf" , end = " ") # 출력하고 출 안바꿈 ( 한 칸 띔)
# # print("aaaa")


# gun =2 
# # 가변인자  (입력받을 변수의 수를 유동적으로 받을 수 있음)
# def func2 (num, count, *languages) :
#     global gun # 전역변수 gun 을 사용하겠다.
#     for lang in languages :
#         print (lang , end = " ")

# func2(1,2,"aaaa", "bbbb","cccc","dddd")
# print ("")


# ### 표준입출력 ###
# print ("python", "java", sep = ",",  end = "?")  # 둘을 이어줄 인자를 넣을 수 있음 (지정 안하면 그냥 띄어씀)
# print("")


# # 이해안됨 넘어감
# # import sys

# # print ("python", "java", file = sys.stdout)
# # print ("python", "java", file = sys.stderr)




# scores = { "수학 " : 0 , "영어" : 10, "코딩" : 9123234230}
# for sub, score in scores.items() :   # 쌍으로 튜플로 반환함
#     print(sub.ljust(8), str(score).rjust(4), sep = ":")    # 왼쪽의 8공간을 확보하고 왼쪽정렬함









# for i in range(999, 1005):
#     print(str(i).zfill(3)) # 3자리를 차지하도록 숫자를 출력하고 빈곳은 0 으로 채움 / 4자리 수가 입력되면 그냥 4자리 출력함.



# ### 표준입출력 ### ( 기호의 순서를 바꿀 수 없다.)
# print("{0: >10}".format(123456789)) # 빈칸은 공백으로 채우기 / 10자리 확보 /오른쪽 정렬
# print("{0: >+10}".format(123456789))  # + 부호도 표시 ( 기호도 한칸 차지함 )
# print("{0: >+10}".format(-123456789)) 

# print("{0:_>+10}".format(12346567)) # 빈칸을 _ 로 채우기
# print("{0:,}".format(1234567)) # 3자리마다 콤마 찍기
# print("{0:+,}".format(1234567)) # 3자리마다 콤마 찍기 / 부호 표시하기
# print("{0:^>+30,}".format(1234567)) # 빈칸은 ^로 채우기, 오른쪽 정렬 / 부호표시하기 / 30자리 확보/ 콤마 3자리마다 표시
# print("{0:f}".format(5/3))  # 소수점 출력 (7자리에서 반올림. 기본값임) 1.666667
# print("{0:.2f}".format(5/3))  # 3자리에서 반올림 1.67
# print(5/3) # 그냥 하면 15자리정도까지 나오는듯 1.6666666666666667



### 파일 입출력 ###

# score_file = open("score.txt", "w", encoding = "utf8") # w : 이걸 또 실행하면 파일을 덮어 쓴다.

# print("수학 : 0", file = score_file)
# # print("영어 : 20", file = score_file)
# # print("영어 : 20", file = score_file)
# score_file.close()



# score_file = open("score2.txt", "a", encoding = "utf8") # a : 실행하면 파일을 끝 줄부터 이어서 쓴다. 파일이 없으면 파일을 만들고 쓴다.
# score_file.write("hihihihiihi ")
# score_file.write("hihihihiihi ")
# score_file.write("\nhihihihiihi ") # print로 파일쓰기와의 차이점 : 이 방식으로 쓰면 출력이 끝나고 줄을 바꾸지 않는다.

# score_file.close()


# score_file = open("score2.txt", "r", encoding = "utf8") # r : 읽겠다.

# # print(score_file.read()) # 파일의 모든 내용을 불러 출력한다.
# print(score_file.readline()) # 파일의 한줄을 읽고 파일안에서 다음줄로 커서가 이동된다. 또 실행하면 그 커서위치부터 또 읽어옴.
# # print(score_file.readline(), end ="") 
# print(score_file.readline()) 
# print(score_file.readline()) 
# print(score_file.readline()) 
# print(score_file.readline()) 
# print(score_file.readline())   # 자료가 없으면 빈칸을 출력함. self
# score_file.close()




# # 파일의 내용이 몇줄인지 모를때
# score_file = open("score2.txt", "r", encoding="utf8")
# while True :
#     line = score_file.readline()
#     if not line :
#         break
#     print(line)

# score_file.close()



# score_file = open("score2.txt", "r", encoding="utf8")
# lines = score_file.readlines() # 파일을 모두 읽어와서 list형태로 반환
# for line in lines:
#     print(line, end =" ")
# score_file.close()



### pickle ####
## profile.pickle이라는 파일은 txt 처럼 열람이 안되네? self


# import pickle
# profile_file  = open("profile.pickle", "wb")  # b : 바이너리 타입 , 피클을 쓰기 위해서는 언제나 b를 지정해줘야한다., 피클에서는 인코딩설정할 필요가 없다.
# profile = { "이름" : "윤윤윤", "나이" : 23, "취미" : ["축구", "야구", "농구"]}
# print(profile)
# pickle.dump(profile, profile_file) # 프로필정보를 프로필파일에 저장
# profile_file.close()



# import pickle
# profile_file  = open("profile.pickle", "rb")   # 읽어오기
# profile = pickle.load(profile_file) # 파일에서 정보 읽어오기
# print("a", profile)
# profile_file.close()


###### with ####
# import pickle
# with open("profile.pickle", "rb") as profile_file : # 피클을 사용해서 파일을 받음
#     print(pickle.load(profile_file))
# #close 할 필요가 없음.
# #pickle을 이용한 with 활용


# with open("study2.txt", "w", encoding="utf8") as study_file:
#     study_file.write("반갑다 짜식") # 파일이 없으면 파일을 만들고 쓴다.(파일이 있으면 모든내용을 지우고 덮어씀)
# with open("study2.txt", "r", encoding="utf8") as study_file:
#     print("\n", study_file.read())


###### class ######

class Unit :
    def __init__ (self, name, hp):    # 생성자
        self.name = name # 멤버변수 (클래스 내에서 선언된 변수)
        self.hp = hp
        #  print("[{}]인스턴스가 생성되었다.".format(self.name))


# instance1 = Unit("윤윤", 110) # self 이외의 인자를 입력해야 생성된다.
# instance2 = Unit("김김", 1120)
# instance2.newvalue = True # instance2 에 newvalue 라는 새 변수를 만들 수 있다.(python)




class AttackUnit(Unit) :   # 상속
    def __init__ (self, name, hp, damage):    # 생성자
        Unit.__init__(self, name, hp) #  부모 클래스에서 받아올 것들
        self.damage = damage
    
    def attack(self, location): # 메소드
        print("{0} : {1} 방향으로 적군을 공격한다. [ 공격력 {2}]" \
            .format(self.name, location, self.damage)) #메소드 호출시 입력받을 변수는 self없이 표기

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0 :
            print("{0} : 파괴됨".format(self.name))


firebat = AttackUnit("파이어뱃", 50,22)

firebat.attack("10시")
firebat.damaged(25)
firebat.damaged(25)



# 30 분가량 문자로 스타크래프트 구현...class 연습


##### 예외 처리  ######



# 내장함수 구글검색  list of python builtins
# 외장함수 구글검색  list of python modules



