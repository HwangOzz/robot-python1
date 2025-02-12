#369 게임로직

#처음 단계 설정 후 게임 시작
#먼저 사용자 입력 받고 컴퓨터가 자동 출력
#3,6,9 숫자가 들어갈때마다 "짝" 입력 받아야함
#잘못된 입력 받을 시 패배처리

# iuput #게임 단계 설정
x = input("원하는 길이를 입력해주세요: ")
y = int(x) + 1

# for #게임 반복횟수(위 input에서 받아온 변수를 받아서 설정)
for i in range(1, y):

    a = i // 10
    b = i % 10

# if #유저와 컴퓨터의 순서를 정하기 위해 변수를 2로 나눔
    if i % 2 != 0:
        user = input("다음 숫자를 입력해주세요: ")

# if, input #if와 input을 사용하여 사용자가 입력한 값과 현재 단계가
          #동일한지 확인 
          #3,6,9가 2번씩 들어갈 경우 "짝짝"입력하도록 함
          #컴퓨터 순서에는 입력한 값이 보이도록 출력
          #각 if구문별 else에는 실패 출력
    else:
        if '3' in str(i) or '6' in str(i) or '9' in str(i):
            user = "짝"
        elif ('3' in str(a) or '6' in str(a) or '9' in str(a)) and ('3' in str(b) or '6' in str(b) or '9' in str(b)):
            user = "짝짝"
        else:
            user = str(i)
        print(f"컴퓨터가 입력한 값: {user}")

    if ('3' in str(a) or '6' in str(a) or '9' in str(a)) and ('3' in str(b) or '6' in str(b) or '9' in str(b)):
        if user == "짝짝":
            print("패스")
        else:
            print("실패1")
            break
    elif '3' in str(i) or '6' in str(i) or '9' in str(i):
        if user == "짝":
            print("패스")
        else:
            print("실패2")
            break
    else:
        if user == str(i):
            print("패스")
        else:
            print("실패3")
            break
#브런치용1