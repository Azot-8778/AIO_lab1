string ='''aaaaaaaaab'''
sub ='''ab'''
index = -1
for i in range(len(string)-len(sub)+1):
    success = True
    for j in range(len(sub)):
        if sub[j]!=string[i+j]:
            success = False
            break
    if success:
        index = i
        break
print (index)
