class Solution:
    def singleNumber(self, nums):
        
        result = 0
        
        # check all 32 bits
        for i in range(32):
            
            bit_sum = 0
            
            for num in nums:
                
                # count set bit at ith position
                if (num >> i) & 1:
                    bit_sum += 1
            
            # remaining bit belongs to single number
            if bit_sum % 3:
                
                # handle negative numbers
                if i == 31:
                    result -= (1 << 31)
                else:
                    result |= (1 << i)
        
        return result