#지뢰찾기(빨리 터트리기)
# 10x10 영역에 3개의 지뢰를 매설
# 최소의 시도로 모두 터트리기
mines = [] #출력용
for i in range(10):
    mines.append(['+']*10)
nums = [] #계산용
for i in range(10):
    nums.append([0]*10)
# 임의의 지점에 지뢰 저장(3개)
mine_count = 0
while mine_count < 3:
    import random
    row = random.randint(0,9)
    col = random.randint(0,9)
    #폭탄이 같은 자리인 경우 배치취소
    if nums[row][col] >= 9: continue
    mine_count += 1 #배치폭탄 갯수 1 증가
    nums[row][col]=9
    # 이웃한 8개 방의 숫자를 1증가
    if row != 0 and col !=0 : nums[row-1][col-1] += 1
    if row != 0  : nums[row-1][col] += 1
    if row != 0 and col != 9 : nums[row-1][col+1] += 1
    if col != 9 : nums[row][col+1] += 1
    if row != 9 and col != 9 : nums[row+1][col+1] += 1
    if row != 9  : nums[row+1][col] += 1
    if row != 9 and col != 0 : nums[row+1][col-1] += 1
    if col != 0 : nums[row][col-1] += 1
# 확인
# for n in nums:
#     print( n )
remain_mine = mine_count #남은 폭탄갯수
while remain_mine != 0:
    print(f"\n[ 남은 지뢰 개수 : {remain_mine} ]")
    msg='지뢰의 좌표를 입력하세요(0~9,0~9)  x,y>> '
    ans = input(msg)
    u_row, u_col = ans.split(',')
    u_row, u_col = int(u_row), int(u_col)
    if nums[u_row][u_col] >= 9: #지뢰 찾으면
        mines[u_row][u_col]="$"
        print(" 지뢰를 찾았습니다! ")
        remain_mine -= 1 #남은 폭탄수1감소
    else:
        mines[u_row][u_col]=str(nums[u_row][u_col])
    # mines 리스트 출력
    for m in mines:
        print(" ".join(m))

print("모든 지뢰를 제거했습니다.")
print(f"게임 종료. 총 시도 횟수: {try_count}회")