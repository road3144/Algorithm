def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        if city.lower() in cache:
            answer += 1
            idx = cache.index(city.lower())
            cache[idx:(len(cache)-1)] = cache[idx+1:(len(cache))]
            cache[len(cache)-1] = city.lower()
        else:
            answer += 5
            if cacheSize != 0:
                if len(cache) < cacheSize:
                    cache.append(city.lower())
                else:
                    cache.remove(cache[0])
                    cache.append(city.lower())
    return answer


cacheSize = 1
cities = ["Jeju", "jeju", "jeJu", "JEJU"]
print(solution(cacheSize, cities))