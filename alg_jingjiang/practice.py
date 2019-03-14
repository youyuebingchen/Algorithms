# def binar(a):
# #     if a <= 1:
# #         return (str(a))
# #     else:
# #         return (binar(a // 2) + str(a % 2))
# # def xory(x,y):
# #     x = list(x)
# #     y = list(y)
# #     xn = len(x)
# #     yn = len(y)
# #     new = []
# #     if xn < yn:
# #         for i in range(yn-xn):
# #             x.insert(0,"0")
# #     elif xn >yn:
# #         for i in range(xn-yn):
# #             y.insert(0,"0")
# #     for i in range(len(x)):
# #         if x[i] == y[i]:
# #             new.append(0)
# #         else:
# #             new.append(1)
# #     return(new)
# # def peak(A):
# #     for i in range(1, len(A) - 1):
# #         if A[i] > A[i-1] and A[i] > A[i+1]:
# #             return (i)
# # if __name__ == '__main__':
# #     A = "111"
# #     a = list(A)
# #     for i in range(len(a)):
# #         a[i] = int(a[i])
# #     print(a)
a = 3
b = 4
c= (a+b)//2
print(c)