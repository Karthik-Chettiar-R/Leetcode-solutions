class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()

        if not intervals:
            return []
        left,right=intervals[0][0],intervals[0][1]

        mergedIntervals=[]

        for i in range(1,len(intervals)):
            if intervals[i][0]<=right:
                if intervals[i][1]>right:
                    right=intervals[i][1]

            else:
                mergedIntervals.append([left,right])
                left,right=intervals[i][0],intervals[i][1]

        mergedIntervals.append([left,right])
        return mergedIntervals
        