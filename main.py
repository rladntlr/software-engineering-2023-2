def simple_calculator():
    result = 0
    error_occurred = False

    while True:
        # 입력 받기
        input_str = input()

        # 마지막에 엔터 눌러서 프로그램 종료
        if input_str == "":
            break
        # 특정숫자 입력시 이스터에그 메세지 출력
        elif input_str == "1111":
            print("=> 11/11 is Pepero Days!")
            return 0

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
        print("= error!")
    else:
        print("=", result)

simple_calculator()
