def solution(bandage, health, attacks):
    t, x, y = bandage
    last_time = 0
    now_health = health

    for time, damage in attacks:
        flow = (time - last_time) - 1
        now_health += (flow * x) + (y * (flow // t))
        if now_health >= health:
            now_health = health

        now_health -= damage
        if now_health <= 0:
            now_health = -1
            break
        last_time = time

    if now_health <= 0:
        now_health = -1
    return now_health


bondage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
print(solution(bondage, health, attacks))
