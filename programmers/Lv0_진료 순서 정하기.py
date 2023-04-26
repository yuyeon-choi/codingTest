def solution(emergency):
    answer = []
    tmp = emergency.copy()      # copy() 안쓰면 정렬됨
    emergency.sort(reverse=True)
    for i in tmp:
        val = emergency.index(i)+1 # ***
        answer.append(val)    
    return answer

# # 답2
# def solution(emergency):
#     answer = []
#     emer_ls = {e: i + 1 for i, e in enumerate(sorted(emergency)[::-1])}
#     for e in emergency:
#         answer.append(emer_ls[e])
#     return answer