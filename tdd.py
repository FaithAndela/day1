def solution(x):
    number = []
    for num in range(2,x+1):
        if num>1:
            for k in range(2,num):
                if (num%k)==0:
                    break
                else:
                    print(num)
print(solution(4))
