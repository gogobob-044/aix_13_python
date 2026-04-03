####입력값이 공백
ans = input("나이를 입력: ")
print(f"/{ans}/") #/로 값의 시작과 끝을 앎

ans = ans.strip() #공백글자삭제, 공백인데 스페이스 등 눌렷을 때
if ans : #공백이면 Flase
    pass #정상입력 아닌거 찾기 (비워짐 상태)
    print(f"입력값은 {ans}")
else:
    print("입력안함")

