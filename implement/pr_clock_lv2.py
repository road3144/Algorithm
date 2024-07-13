def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    now = h1 * 3600 + m1 * 60 + s1
    goal = h2 * 3600 + m2 * 60 + s2
    if now == 0 or now == 43200:
        answer += 1
    while now < goal:
        nh, nm, ns = now // 3600, (now % 3600) // 60, (now % 3600) % 60
        sp = ns * 3600
        mp = nm * 3600 + ns * 60
        hp = (nh % 12) * 5 * 3600 + nm * 60 * 5 + ns * 5

        nsp, nmp, nhp = sp + 3600, mp + 60, hp + 5

        if nmp == nhp:
            answer -= 1

        if sp < mp and nmp <= nsp:
            answer += 1
        if sp < hp and nhp <= nsp:
            answer += 1
        print()
        now += 1
    return answer


h1, m1, s1, h2, m2, s2 = 12, 0, 0, 12, 0, 30

print(solution(h1, m1, s1, h2, m2, s2))