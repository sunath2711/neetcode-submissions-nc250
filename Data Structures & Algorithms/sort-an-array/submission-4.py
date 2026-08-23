#Heap sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # this loop for creating the max heap once O(n)
        for i in range(n//2 - 1,-1,-1):
            self._heapify(nums,n,i)

        # now to swap , each step we get max at nums[0] , swap that and reduce the nums to make comparisons
        for i in range(n-1,0,-1):
            nums[0], nums[i] = nums[i], nums[0]

            self._heapify(nums,i,0)

        return nums

    def _heapify(self, nums: List[int], n: int,i: int):
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and nums[left] > nums[largest]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right
        # if root is not the largest, swap and push down recursively
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self._heapify(nums, n , largest)


