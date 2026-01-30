class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        length = len(candies)

        result = []

        for i in range(length) :
            temp1 = []
            temp2 = candies.copy()
            temp2[i] += extraCandies

            if temp2[i] == max(temp2):
                result.append(True)
            
            else:
                result.append(False)

        return result