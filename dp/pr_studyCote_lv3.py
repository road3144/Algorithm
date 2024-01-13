# 답보고 작성 다시 검토 필요

def solution(alp, cop, problems):
    max_alp_req = max_cop_req = 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp_req = max(alp_req, max_alp_req)
        max_cop_req = max(cop_req, max_cop_req)

    dp = [[int(1e9)] * (max_cop_req + 1) for _ in range(max_alp_req + 1)]

    alp = min(alp, max_alp_req)
    cop = min(cop, max_cop_req)

    dp[alp][cop] = 0

    for i in range(alp, max_alp_req+1):
        for j in range(cop, max_cop_req+1):
            if i < max_alp_req:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop_req:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    nalp = min(max_alp_req, i + alp_rwd)
                    ncop = min(max_cop_req, j + cop_rwd)
                    dp[nalp][ncop] = min(dp[nalp][ncop], dp[i][j] + cost)
    return dp[max_alp_req][max_cop_req]


alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
print(solution(alp, cop, problems))
