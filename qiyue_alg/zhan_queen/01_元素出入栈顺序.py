# from  stacks_xu import stack
import sys
sys.path.append("../../shujujiegou")
from x03_stack import stack

def posible(A,B):
    a = stack()
    i = 0
    j = -1
    while j < len(B):
        j = + 1
        while a.is_empty() or a.peek() != B[j]:
            if i >=len(A):
                return False
            else:
                a.push(A[i])
                i += 1
        a.pop()

    return True

if __name__ == '__main__':
    A = [1,2,3,4,5]
    B = [5,4,3,2,1]
    print(posible(A,B))