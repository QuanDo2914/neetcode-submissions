class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number = {}
        for num in nums:
            number[num] = number.get(num, 0) +1
        sorted_number = sorted(number, key = number.get, reverse = True)

        result =[]
        for n in range(k):
            result.append(sorted_number[n])
        return result
        
    
        