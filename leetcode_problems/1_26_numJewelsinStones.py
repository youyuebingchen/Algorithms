

def NumJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    J = list(J)
    S = list(S)
    count = 0
    for i in range(len(J)):
        for j in range(len(S)):
            if J[i] == S[j]:
                count += 1
    return count


if __name__ == '__main__':
    J = "aAb"
    S = "aAAbabb"
    NumJewelsInStones(J,S)