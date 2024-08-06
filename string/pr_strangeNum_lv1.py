def solution(s):
    idx = 0
    for i in range(len(s)):
        if s[i] == ' ':
            idx = 0
            continue
        if idx % 2 == 0:
            s = s[:i] + s[i].upper() + s[i+1:]
        else:
            s = s[:i] + s[i].lower() + s[i+1:]
        idx += 1
    return s


s = "try hello world"
print(solution(s))
