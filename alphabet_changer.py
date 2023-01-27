# 입력한 영문에서 원하는 알파벳을 대문자 또는 소문자로 만들기
# 데이터 과학을 위한 파이썬 프로그래밍 교재 chapter 6 예제 2번 보고 생각해본 거
sentence_input = input("원하는 영문을 입력하여 주십시오 :")
changer = input("바꾸고자 하는 알파벳을 입력하여 주십시오 :")
alphabet = input("대문자로 바꾸고 싶으면 1, 소문자로 바꾸고 싶으면 0을 입력하여 주십시오 :")

sentence = list(sentence_input)

if changer.isalpha() :
    if alphabet == '1' :      # 대문자
        for i in range(len(sentence)) :
            if ord(sentence[i]) >= 97 and ord(sentence[i]) <= 122 :
                if sentence[i].upper() == changer.upper() :
                    result = sentence[i].upper()
                    del sentence[i]
                    sentence.insert(i, result)
        
        sentence_result = ''.join(sentence)
        print("결과 :", sentence_result)

    elif alphabet == '0' :    # 소문자
        for i in range(len(sentence)) :
            if ord(sentence[i]) >= 65 and ord(sentence[i]) <= 90 :
                if sentence[i].upper() == changer.upper() :
                    result = sentence[i].lower()
                    del sentence[i]
                    sentence.insert(i, result)

        sentence_result = ''.join(sentence)
        print("결과 :", sentence_result)

    else :
        print("대문자(1), 소문자(0) 여부를 정확히 입력하여 주십시오.(3번째 항목)")

else :
    print("알파벳을 정확히 입력하여 주십시오.(2번째 항목)")

