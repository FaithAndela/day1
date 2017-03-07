

def solution(N):
   for num in range(2, N + 1):
   
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                   break
            else:
                print(num)
print(solution(8))
                  