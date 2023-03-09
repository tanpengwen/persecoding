k = []
for x in range(3):
  if x%2 == 0:
    s = int(input())
    k.append(s)
  else:
    s = input()
    k.append(s)
if k[1] == "+":
  print(k[0]+k[2])
else:
  print(k[0]*k[2])
