n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    mv = min(data)

    result = max(result, mv)

print(result)

#숫자 카드 게임