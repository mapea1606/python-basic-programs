if __name__ == '__main__':
    n = int(input())
    while n < 2 or n > 10:
        n = int(input())

    arr = map(int, input().split())
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    primero = arr.pop()
    runner_up = max(arr)

    print(runner_up)
