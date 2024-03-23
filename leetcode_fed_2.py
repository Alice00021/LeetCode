from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        array_of_strings = [""] * (n+1)
        array_of_strings[1:]
        for i in range(1, n+1):
            if i%3==0:
                array_of_strings[i]+="Fizz"
            if i%5==0:
                array_of_strings[i]+="Buzz"
            if not array_of_strings[i]:
                array_of_strings[i] += str(i)
        return array_of_strings[1:]
    
sol=Solution()
print(sol.fizzBuzz(15))