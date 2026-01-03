class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l=[]
        nums.sort()
        nums1=nums
        i=0

        while(i<len(nums1)-2):
            if i>0 and nums1[i]==nums1[i-1] :
                if i <len(nums1)-1:
                    i+=1
                    continue
            j=i+1
            k=len(nums1)-1
            while(j<k and k>i and j<len(nums1)-1):
                if nums1[i]+nums1[j]+nums1[k]>0:
                    k-=1
                elif nums1[i]+nums1[j]+nums1[k]<0:
                    j+=1
                elif nums1[i]+nums1[j]+nums1[k]==0:
                    l.append([nums1[i],nums1[j],nums1[k]])
                    j+=1
                    k-=1
                    while(j<len(nums1)-1 and nums1[j]==nums1[j-1]):
                        j+=1
                    while(k>j and nums1[k]==nums1[k+1]):
                        k-=1
            i+=1


        return l
