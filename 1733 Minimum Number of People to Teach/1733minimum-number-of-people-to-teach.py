def common(list1,list2):
    for i in list1:
        if i in list2:
            return True
    return False

class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """

        
        toTeach=set()
        for friendship in friendships:
            if common(languages[friendship[0]-1],languages[friendship[1]-1]):
                continue
            else :
                
                toTeach.add(friendship[0])
                toTeach.add(friendship[1])

        c=len(languages)+1
        
    

        for language in range(1,n+1):
            count=0
            done =[False]*len(languages)
            for friendship in friendships:
                if (friendship[0] in toTeach):
                    if not (language in languages[friendship[0]-1]) and not(done[friendship[0]-1]):
                        count+=1
                        done[friendship[0]-1]=True

                if (friendship[1] in toTeach):
                    
                    if not (language  in languages[friendship[1]-1]) and not(done[friendship[1]-1]):
                        count+=1
                        done[friendship[1]-1]=True

            if count<c:
                c=count
        return c
                        
                        
                    
                    
            
            
        