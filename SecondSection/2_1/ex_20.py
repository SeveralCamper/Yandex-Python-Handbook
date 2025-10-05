weight = int(input())
cost_all = int(input())
cost_1 = int(input())
cost_2 = int(input())

# { x + y = N 
# { x * K1 + y * K2 = M * N

# x * K1 + (N - x) * K2 = M * N 
# x * K1 + N * K2 - x * K2 = M * N
# x * K1 - x * K2 = M * N - N * K2
# x * (K1 - K2) = M * N - N * K2
# x = (M * N) - (N * K2) / (K1 - K2)
# x = (N * (M - K2)) / (K1 - K2)

x = int((weight * (cost_all - cost_2)) / (cost_1 - cost_2))

# y * K2 = M * N - x * K1
# y = (M * N - x * K1) / K2

y = int((cost_all * weight - x * cost_1) / cost_2)

print(f"{x} {y}")
