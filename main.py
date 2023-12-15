# 이스터에그 값인지 확인하는 함수
def isEasteregg(val):
    if val == "1111":
        print("[EVENT]\"11/11 is Pepero Days!\"")
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
        print("[System] ERROR!")
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
        print("[System] ERROR!")
    else:
        print(result)


def multi(result):
    error_occured = False

    while True:
        num = input()

        # num 에 "=" 입력시 error발생 및 while문 탈출
        if num == "=":
            error_occured = True
            break
        elif isEasteregg(num):
            return

        op = input()

        if op == "=":
            result *= int(num)
            break

        elif op == "*":
            # num이 정수인지 확인
            if num.isdigit():
                result *= int(num)
            else:
                error_occured = True
        else:
            error_occured = True

    if error_occured:
        print("[System] ERROR!")
    else:
        print(result)


def simple_calculator():
    isError = False

    # 1. 초기값을 입력받는 부분
    val = input()
    if val == "=":
        print("[System] ERROR!")
    elif isEasteregg(val):
        return
    elif val.isdigit():
        result = int(val)
    else:
        isError = True

    # 2. 최초 연산자를 입력받는 부분
    if not isError:
        opr = input()
        if opr == "=":
            print(result)
            return
        if isEasteregg(opr):
            return
        if opr == "+":
            add(result)
            return
        if opr == "-":
            sub(result)
            return
        if opr == "*":
            multi(result)
            return

    # 3. 초반부터 에러가 난 경우 "="이 나올 때까지 반복하는 부분
    while True:
        if input() == "=":
            print("[System] ERROR!")
            return

if __name__ == '__main__':
    simple_calculator()
