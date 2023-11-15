result = 0
#while문 첫 실행 구분(result값이 0이 됨을 방지)
count = 0
error_occured = False

while True:
    
    num = input()

    #num 에 "=" 입력시 error발생 및 while문 탈출
    if num=="=":
        error_occured = True
        break
    
    op = input()

    if op=="=":
        result*=int(num)
        break
    
    elif op=="*":
        #num이 정수인지 확인
        if num.isdigit():
            #첫 실행 시 result 값을 num으로 초기화
            if count==0:
                result=int(num)
                count=1
            else:
                result*=int(num)
        else:
            error_occured=True
    else:
        error_occured = True

if error_occured:
    print("error!")
else:
    print(result)
    
    

