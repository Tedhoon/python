lion_works = [
'송상호',
'송준호',
'오남철',
'윤권인',
'윤치원',
'이민정',
'이민주',
'이승원',
'이승혜',
'이영화',
'장미선',
'전준현',
'정새미',
'정혜연',
'조성우',
'주우석',
'최규석',
'최현철',
'황성욱']



def check_lion(is_com):
    if is_com in lion_works:
        lion_works.remove(is_com)
        print(lion_works)


if __name__ == '__main__':
    print("사람입력하셈")
    print("끝 << 치면 끝남")
    while True:
        is_com = input()
        if is_com == "끝":
            break;
        check_lion(is_com)

