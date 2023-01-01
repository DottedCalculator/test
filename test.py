diamond_codes = []
for i in range(6):
  diamond_codes.append(input())
l = []
for i in diamond_codes:
  for j in i:
    l.append(ord(j))
for i in range(41):
  for j in range(100):
    l[i] += l[i+j]
  l[i] %= 100
l1 = [18, 100, 84, 46, 43, 35, 51, 95, 51, 26, 90, 92, 98, 98, 94, 95, 40, 36, 34, 29, 38, 29, -6, 64, 85, 103, 53, 106, 93, 87, 41, -6, -39, 27, 78, 89, 74, 21, 28, 19, 25]
ans = ''
for i in range(41):
  ans += chr(l[i]+l1[i])
print(ans)
