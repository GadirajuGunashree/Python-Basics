g=[111,12,13,43,-12,33,54,12]
n=len(g)
target =54
for i in range(n):
    print(g[i])
    if g[i]==target:
        print("found")
        visited=1
        break
if visited==0:
    print("not found")
# Output
# 111
# 12
# 13
# 43
# -12
# 33
# 54
# found
