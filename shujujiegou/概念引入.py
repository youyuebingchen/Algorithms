# 如果a+b+c = 1000 a^2+b^2 = c^2 如何求出a,b,c的可能组合
# 方案一
import time
# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c == 1000 and a**2 + b**2 == c**2:
#                 print("a=%d,b=%d,c=%d"%(a,b,c))
# end_time =time.time()
# print("time:%d"%(end_time-start_time))


# 方案二 不对c进行试探
# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         c = 1000 - a - b
#         if c**2 == b**2 +a**2:
#             print("a=%d,b=%d,c=%d"%(a,b,c))
# end_time = time.time()
# print("time:%.3f" % (end_time - start_time))
