def minDeletionSize(A):
    A = [list(A[i]) for i in range(len(A))]
    D = []
    n = len(A) - 1
    m = len(A[1])
    while i <=n:
        i = 0
        for j in range(m):
            if ord(A[i][j]) <= ord(A[i + 1][j]):
                i +=1
                D.append(i)
            return (len(D))


if __name__ == '__main__':
    A = ["zyx","wvu","tsr"]
    # A = [list(A[i]) for i in range(len(A))]
    # print(len(A))
    minDeletionSize(A)
