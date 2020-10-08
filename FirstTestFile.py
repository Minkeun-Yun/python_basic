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
# llist = [ "가", "나나나", "다라"]
# print(llist.index("나나나")) # 1  위치찾기

# llist.append("캬캬캬")  # 원소 추가
# print(llist)

# llist.insert(1, "윤윤윤") # 넣을 위치 index  원소 삽입
# print(llist)


# print(llist.pop()) # 맨 뒤에 원소 꺼내어 반환
# print(llist)

# print(llist.count("나나나")) #나나나 원소 가 몇번 있는지




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