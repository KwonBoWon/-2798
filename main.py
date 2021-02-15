from itertools import combinations

N, M=map(int , input().split())

cards=list(map(int , input().split()))

com=list(combinations(cards,3))

maxi=0
for i in com:
  if i[0]+i[1]+i[2]<=M:
    maxi=max(i[0]+i[1]+i[2], maxi)

print(maxi)
