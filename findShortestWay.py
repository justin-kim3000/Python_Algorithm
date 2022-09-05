from posixpath import split


x, y, w, h = map(int, input().split())


def findAbsoluteValue(x, y, w, h):
    result = []
    result.append(abs(h-y))
    result.append(abs(w-x))
    result.append(abs(x))
    result.append(abs(y))

    return min(result)


print(findAbsoluteValue(x, y, w, h))
