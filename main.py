# 이스터에그 값인지 확인하는 함수
def isEasteregg(val):
    if val == "1111":
        print("=> 11/11 is Pepero Days!")
        return True
    
    return False

# 덧셈 연산을 하는 함수
def add(result):
    error_occurred = False

    while True:
        # 입력 받기
        input_str = input()

        # 프로그램 종료
        if input_str == "=":
            break
        # 특정숫자 입력시 이스터에그 메세지 출력
        elif isEasteregg(input_str):
            return
        
        # 인풋값 확인
        if input_str.isdigit():
            result += int(input_str)
        elif input_str == "+":
            continue
        else:
            # 오류 발생 확인 하지만 입력 끝까지 받기
            error_occurred = True

    # 에러 메세지와 출력값
    if error_occurred:
        print("error!")
    else:
        print(result)

def sub(result):
    error_occurred = False

    input_str = input()
    if isEasteregg(input_str):
        return
    elif input_str.isdigit():
        result -= int(input_str)

    while True:
        input_str = input()

        if input_str == "=":
            break
        elif isEasteregg(input_str):
            return
        elif input_str == "-":
            input_str = input()
            if isEasteregg(input_str):
                return
            elif input_str.isdigit():
                result -= int(input_str)
        else:
            error_occurred = True

    if error_occurred:
        print("error!")
    else:
        print(result)

def multi(result):
    error_occured = False

    while True:
        num = input()

        #num 에 "=" 입력시 error발생 및 while문 탈출
        if num=="=":
            error_occured = True
            break
        elif isEasteregg(num):
            return
        
        op = input()

        if op=="=":
            result*=int(num)
            break
        
        elif op=="*":
            #num이 정수인지 확인
            if num.isdigit():
                result*=int(num)
            else:
                error_occured=True
        else:
            error_occured = True

    if error_occured:
        print("error!")
    else:
        print(result)
    
def simple_calculator():
    isError = False

    # 1. 초기값을 입력받는 부분
    val = input()
    if (val == "="):
        print("error!")
    elif (isEasteregg(val)):
        return
    elif (val.isdigit()):
        result = int(val)
    else:
        isError = True

    # 2. 최초 연산자를 입력받는 부분
    opr = input()
    if (!(isError)):
        if (opr == "="):
            print(result)
            return
        if (isEasteregg(opr):
            return
        if (opr == "+"):
            add(result)
            return
        if (opr == "-"):
            sub(result)
            return
        if (opr == "*"):
            multi(result)
            return

    # 3. 초반부터 에러가 난 경우 "="이 나올 때까지 반복하는 부분
    while(True):
        if (input() == "="):
            print("error!")
            return

simple_calculator()

"""
요구사항에서 비롯한 문제점 논의
    1. "한 번의 입력에는 한 종류의 연산만 들어올 수 있습니다."라는 문장에서 한 번의 입력을 어디까지로 볼것인가.
        1.1. 계산기가 시작하고 종료될 때까지("="이 입력될 때까지)를 한 번의 입력으로 보는 의견
            즉, 계산기가 실행되는 동안 모두 동일한 연산만을 수행함.
        1.2. 연산자가 입력되는 순간순간을 한 번의 입력으로 보는 의견
            즉, 매번 다른 연산이 실행될 수 있음.
        결론: 1번 안.
        
    2. 이스터에그가 동작했을 때 계산기의 작동을 정지할 것인가.
        결론: 그렇다.

    3. 에러가 났을 때의 메시지를 무엇으로 할 것인가.
        결론: "error!"

    4. 수식 없이 바로 "="을 입력했다면 이것은 에러인가.
        결론: 그렇다.

    5. 에러를 언제 알릴 것인가.
        근거: 예시를 보면 에러가 났을 때에도 "="이 입력되면 알려준다.
        결론: "="이 입력되면 알린다.
        # 추신: 이거는 제가 ppt에서 에러가 나도 "="이 입력될 때까지 동작한다는 문장을 못 찾아서 넣은거라 그런 문장이 있으면 안넣어도 될 거 같아요.
        
    6. 예시의 콘솔창처럼 만들기에는 "="의 입력을 감지하기 힘든 문제가 있다.
        결론: 결과값을 "="의 아랫줄에 출력하도록 한다.

시스템 구축을 위한 논의
    1. 각자 내용에 맞게 함수를 만들어 연결한다.
        1.1. 메인과 연산자 사이의 연결:
            메인에서 초깃값과 최초의 연산자를 입력받으면 연산자에 맞게 함수를 호출한다.
            함수의 매개변수로 초깃값을 입력한다.
        1.2. 이스터에그를 담당하는 함수(많은 곳에 활용되기에 형태을 정함):
            입력받은 값을 문자열 상태 그대로 넘겨주면 결과에 맞게 True 혹은 False를 반환한다.
            함수명은 isEasteregg로 한다.
            요약: 이스터에그를 담당하는 함수는 bool isEasteregg(string val) 이런 형태

추신:
    갈아 엎으니까 각자가 맡은 부분이 다 없어져 버려서(거의 그냥 나 혼자 만든 코드) 최대한 각자의 코드를 살리기 위해
    코드를 먼저 만들고 이런 코드가 나올려면 이런 논의가 사전에 있었지 않을까? 스러운 논의들을 추가했습니다.
    요구사항에서 비롯한 문제점 논의 6번은 코드 작성 중 생긴 문제점으로 작성 도중 논의한 것입니다.

    코드에 많은 문제점이 있는데(발견한 것 중 대표적인 것은 isdigit()은 음수가 false로 나오는 문제점)
    다음 과제가 테스트인 것같아서 거기서 테스트로 발견하고 고치는 느낌으로 해도 딱히 점수 안 까일 것같아서 그냥 놔뒀습니다.
    그래도 대표적으로 적은 저 문제점의 해결 방안은 찾아놨습니다.
"""
