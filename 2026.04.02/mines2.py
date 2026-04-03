# 10x10 영역에 3개의 지뢰를 매설
# 최소의 시도로 모두 터트리기
# 초급(5x5-2), 중급(7*7-4), 고급(10*10-7)
# #레벨을 선택하세요
# 1 초급(5x5) 지뢰2개
# 2 중급(7X7) 지뢰4개
# 3 고급(10X10) 지뢰6개
# #레벨 선택>>


def read_level():
    global level
    msg='''
레벨을 선택하세요
1 초급(5x5) 지뢰2개
2 중급(7X7) 지뢰4개
3 고급(10X10) 지뢰6개
레벨 선택>> '''
    while True:
        try:
            level = int(input(msg))

        except:
                print('레벨을 선택하세요(1~3)')
        else:
            if level not in [1,2,3]:continue
            break
    return level
read_level()

# 선택에 따른 설정값 부여
sizes=[0,5,7,10]
size = sizes[level]
mine_counts = [0,2,4,6]
total_mines = mine_counts[level]

mines = [] #출력용
for i in range(size): #행개수
    mines.append(['+']*size) #열개수
nums = [] #계산용
for i in range(size):
    nums.append([0]*size)
# 임의의 지점에 지뢰 저장(3개)
mine_count = 0
while mine_count < total_mines:
    import random
    row = random.randint(0,size-1)
    col = random.randint(0,size-1)

    #폭탄이 같은 자리인 경우 배치취소
    if nums[row][col] >= size-1: continue
    mine_count += 1 #배치폭탄 갯수 1 증가
    nums[row][col]=size-1
    # 이웃한 8개 방의 숫자를 1증가
    if row != 0 and col !=0 : nums[row-1][col-1] += 1
    if row != 0  : nums[row-1][col] += 1
    if row != 0 and col != size-1 : nums[row-1][col+1] += 1
    if col != size-1 : nums[row][col+1] += 1
    if row != size-1 and col != size-1 : nums[row+1][col+1] += 1
    if row != size-1  : nums[row+1][col] += 1
    if row != size-1 and col != 0 : nums[row+1][col-1] += 1
    if col != 0 : nums[row][col-1] += 1
# 확인
# for n in nums:
#     print( n )
remain_mine = total_mines #남은 폭탄갯수
try_count = 0
while remain_mine != 0:
    while True:
        try:
            print(f"\n[ 남은 지뢰 개수 : {remain_mine} ]")
            msg=f'지뢰의 좌표를 입력하세요(0~{size-1},0~{size-1})  x,y>> '
            ans = input(msg)
            u_row, u_col = ans.split(',')
            u_row, u_col = int(u_row), int(u_col)
            try_count += 1 # 시도 횟수 증가
        except:
            print('좌표 오류입니다')
        else:
            if (u_col not in range(size) or u_row not in range(size)) :
                print('행열범위를 넘었습니다.')
                continue 
            break

    if nums[u_row][u_col] >= size-1: #지뢰 찾으면
        mines[u_row][u_col]="$"
        print(" 지뢰를 찾았습니다! ")
        remain_mine -= 1 #남은 폭탄수1감소
    else:
        mines[u_row][u_col]=str(nums[u_row][u_col])
    # mines 리스트 출력
    header = 'x ' +' '.join([str(i) for i in list(range(size))])
    print(header)
    rcnt = 0 #행번호
    for m in mines:
        print(str(rcnt)+' '+" ".join(m))
        rcnt+=1

print("모든 지뢰를 제거했습니다.")
print(f"게임 종료. 총 시도 횟수: {try_count}회")