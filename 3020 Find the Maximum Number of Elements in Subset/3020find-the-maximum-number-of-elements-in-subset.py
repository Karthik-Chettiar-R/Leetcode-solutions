import heapq

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        retMax=0
        if nums:
            retMax=1
        else :
            return 0
        
        frequency={}

        elements=set(nums)
        candidates=set()

        for element in nums:
            if element not in frequency:
                frequency[element]=1
            else :
                frequency[element]+=1

        if 1 in frequency:
            if frequency[1]%2==1:
                retMax=max(retMax,frequency[1])
            else :
                retMax=max(retMax,frequency[1]-1)
       
            

        pQueue=[]

        for key in frequency :
            if frequency[key]>=2 and key is not 1:
                heapq.heappush(pQueue,key)
                candidates.add(key)
        
        done=set()
        
        for i in range(len(pQueue)):
            currMax=2
            if pQueue[i] in done:
                continue
            else :
                ele=pQueue[i]
                done.add(ele)
            while(ele**2 in candidates):
                currMax+=2
                done.add(ele**2)
                ele=ele**2
            if ele**2 in elements:
                currMax+=1
            else:
                currMax-=1
            retMax=max(currMax,retMax)
        
        return retMax
                


                

        