# m1 = {
#     "name": "어벤저스 엔드게임",
#     "type": "히어로 무비"
#     }
# # print(m1)

# st1 = {"name": "홍길동", "hakbun":1120}
# print(st1["name"])
# print(st1["hakbun"])
# scoreDict = {
#     "홍길동":[80,70,90],
#     "김길동":[70,70,90], #파이썬은 , 뒤에 뭐 없어도 오류 X
#     }
# print(scoreDict['홍길동'])
# #홍길동의 과목 점수를 알 수 없을 때 구조 변경
# scoreDict = {
#     "홍길동" : { "korean" : 80, "english" : 70, "math" : 90},
#     "김길동" : { "korean" : 70, "english" : 70, "math" : 90},
#     }
# print(scoreDict['홍길동']['korean'])

# n = '홍길동'
# #키는 immutable Object만 가능. 불변객체
# dic1 = {
#     n : 90
# }
# print(dic1)
# dic2 = {
#     (1,3) : 90 #튜블은 수정불가라 가능
# }

# dict3 = dict()
# print(dict3)
# dict3["a"] = 70
# dict3["b"] = 80
# print(dict3)
# dict3["b"] = 100
# print(dict3)
# del dict3['a']
# print('삭제후', dict3)
# # del dict3['a'] #없는 키 접근 에러

# ##### 학생점수관리
# scores = dict()
# scores["홍길동"] = {
#     'guk': 70, 'math': 80, 'eng': 90
# }
# name = input('학생이름>> ')
# # if name in scores:
# #     print(f'{name}의 점수 {scores[name]}')
# # else :
# #     print(f'{name}은 미등록 학생')

# #get() 
# value = scores.get(name)
# if value == None: 
#     print(f'{name}은 미등록 학생')
# else:
#     print(f'{name}의 점수 {scores[name]}')

####
scores2 = {
    "홍":70, "김":80, "강": 75, "권":90
}
for k in scores2: #키만 들어감
    print(f"{k} {scores2[k]}")

    