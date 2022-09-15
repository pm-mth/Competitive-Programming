class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=list(range(1, n+1))
        for i in answer:
            if i%5==0 and i%3==0:
                answer[i-1]="FizzBuzz"
            elif i%3==0:
                answer[i-1]="Fizz"
                
            elif i%5==0:
                answer[i-1]="Buzz"
            else:
                answer[i-1]=str(i)
        return answer
    
