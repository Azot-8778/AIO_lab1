def kmp_table(word):
    cnd = 0
    T = [-1] * (len(word) + 1)
    
    for pos in range(1, len(word)):
        if word[pos] < word[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and word[pos] != word[cnd]:
                cnd = T[cnd]
        cnd += 1
    
    T[pos + 1] = cnd
    
    return T

def kmp_search(S, W):
    k = 0
    T = kmp_table(W)
    P = []
    
    np = 0
    
    for j in range(len(S)):
       
        if W[k] == S[j]:
            k += 1
            if k == len(W):
                P.append(j + 1 - k)
                np += 1
                k = T[k]
                
        else:
            k = T[k]
            if k < 0:
                k += 1
    
    return P

i = kmp_search(string, sub)
print(i)
