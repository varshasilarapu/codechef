t=int(input())
for i in range(t):
    n=int(input())
    heights = list(map(int,input().split()))
    tallest = max(heights)
    print(tallest)
