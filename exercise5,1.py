import time

t = time.time()

days = t // 86400
hours = (t % 86400) // 3600
minutes = (t % 3600) // 60
seconds = t % 60

print("days since epoch:", int(days))
print("time:", int(hours), ":", int(minutes), ":", int(seconds))