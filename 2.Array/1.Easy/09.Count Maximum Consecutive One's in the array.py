#Count Maximum Consecutive One's in the array
# also find consective any number in array like 1,2,3,4,5 

class solution:
	
	def Count_Maximum_Consecutive_One_in_the_array(self, nums: List[int]) -> int:
		cnt = 0
		maxi = 0
		for i in range(len(nums)):
			if nums[i] == 1:
				cnt += 1
			else:
				cnt = 0
			maxi = max(maxi,cnt)
			
		return maxi

# Example usage
if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    obj = Solution()
    ans = obj.Count_Maximum_Consecutive_One_in_the_array(nums)
    print(f"The maximum consecutive 1's are {ans}")
