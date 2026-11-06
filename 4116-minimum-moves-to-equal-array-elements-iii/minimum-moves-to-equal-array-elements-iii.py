class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ma=max(nums)

        moves=0

        for num in nums:
            moves+=ma-num

        return moves
        