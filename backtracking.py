n, m = map(int, input().split())
s = []


def f():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i in s:
            continue
        s.append(i)
        f()
        s.pop()


f()

# 백트래킹(backtracking)이란? : 해를 찾는 도중 해가 아닐경우 막히면, 되돌아가서 다시 해를 찾아가는 기법. 최적화 문제와 결정 문제를 푸는 방법
