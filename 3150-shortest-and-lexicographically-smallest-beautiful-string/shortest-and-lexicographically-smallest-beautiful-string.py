class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        ones=0
        i=0
        j=0

        smallest=float('inf')

        candidates=[]

        while(j<len(s)):
            if s[j]=='0':
                
                j+=1
                continue

            else:
                ones+=1

            if ones==k:
                smallest=min(smallest,j-i+1)
                candidates.append(s[i:j+1])

                if s[i]=='0':
                    while(s[i]!='1'):
                        i+=1
                    smallest=min(smallest,j-i+1)
                    candidates.append(s[i:j+1])

                

            elif ones>k:
                while(ones>k):
                    if s[i]=='1':
                        ones-=1
                    i+=1

                while(s[i]!='1'):
                    i+=1
                smallest=min(smallest,j-i+1)
                candidates.append(s[i:j+1])


            j+=1

        candi=[]

        for i in candidates:
            if len(i)==smallest:
                candi.append(i)

        candi.sort()
        if candi:
            return candi[0]
        return ''





                        




                
