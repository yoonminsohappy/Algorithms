# 프로그래머스 체육복, Greedy


def solution(n, lost, reserve):
    # new_reserve = n - len(lost)
    # answer = 0

    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    answer = n - len(lost)
    print(answer)
    return answer


solution(5, [2, 4], [1, 3, 5])
