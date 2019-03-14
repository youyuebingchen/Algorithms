def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    even = []
    odd = []
    for i in A:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    A = even.extend(odd)
    return A

if __name__ == '__main__':
    A = [1,2,3,4]
    a = sortArrayByParity(A)
    print(a)