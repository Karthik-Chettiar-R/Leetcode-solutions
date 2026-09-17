class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
          

        prefix=[float('inf')]
        suffix=[]

        current=0
        mi=float('inf')

        i=0
        j=0

        while(j<len(arr)-1 and i<len(arr)-1):
            current+=arr[j]

            if current==target:
                mi=min(mi,j-i+1)
                j+=1
                prefix.append(mi)

            elif current<target:
                j+=1
                prefix.append(mi)

            elif current>target:
                while(current>target and i<=j):
                    current-=arr[i]
                    i+=1

                if current==target:
                    mi=min(mi,j-i+1)

                j+=1
                prefix.append(mi)
        
        suffix=[]
        ma=float('inf')
        current=0

        i=len(arr)-1
        j=len(arr)-1


        while(j>=0 and i>=0):
            current+=arr[i]

            if current==target:
                ma=min(ma,j-i+1)
                i-=1
                suffix.append(ma)

            elif current<target:
                i-=1
                suffix.append(ma)

            elif current>target:
                while(current>target and j>=i):
                    current-=arr[j]
                    j-=1

                if current==target:
                    ma=min(ma,j-i+1)

                i-=1
                suffix.append(ma)


        

        suffix=suffix[::-1]

        su=float('inf')

  
        
        for i in range(len(arr)):
            su=min(su,suffix[i]+prefix[i])

        if su==float('inf'):
            return -1

        return su
            




