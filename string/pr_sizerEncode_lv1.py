def solution(s, n):
    answer = ''
    for i in s:
        if i.isalpha():
            if 65 <= ord(i) <= 90:
                i = chr((ord(i) + n - 65) % 26 + 65)
            else:
                i = chr((ord(i) + n - 97) % 26 + 97)
        answer += i
    return answer
