time = int(input())
h = time // 3600
m = (time % 3600) // 60
s = (time % 3600) % 60

print("%.2d:%.2d:%.2d" % (h, m, s))
