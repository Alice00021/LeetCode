class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
    
        result = [0] * (len(num1) + len(num2))
  
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
         
                mul = int(num1[i]) * int(num2[j])
                total = mul + result[i+j+1]
            
                result[i+j] += total // 10
                result[i+j+1] = total % 10

        result_str = ''.join(map(str, result))
        result_str = result_str.lstrip('0')
    
        return result_str 
    
    
sol=Solution()
sol.multiply("12", "18")