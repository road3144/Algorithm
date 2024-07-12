def solution(bandage, health, attacks):
    t, x, y = bandage
    answer = 0
    now = 0
    for attack_time, damage in attacks:
        heal_time = attack_time - now - 1
        health += heal_time * x
        health += (heal_time // t) * y

        health -= damage
        if health <= 0:
            answer = -1
            break

    return answer


bondage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
print(solution(bondage, health, attacks))
