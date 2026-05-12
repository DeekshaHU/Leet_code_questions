class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        max_c = 0
        ans = len(nums)

        for num in set(nums):

            count = nums.count(num)

            if count >= max_c:

                count1 = 0

                for i in range(len(nums)):
                    if nums[i] == num:
                        count1 = 1
                        s = i
                        break

                l = []
                l.append(nums[s])

                i = s + 1

                while count1 != count:

                    l.append(nums[i])

                    if nums[i] == num:
                        count1 += 1

                    i += 1

                if count > max_c:
                    max_c = count
                    ans = len(l)

                else:
                    ans = min(ans, len(l))

        return ans