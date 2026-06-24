class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited=set()
        
        queue=[]
        for i in rooms[0]:
            queue.append(i)
            visited.add(i)
        visited.add(0)
        
        for i in queue:
            for j in rooms[i]:
                if j not in visited:
                    queue.append(j)
                    visited.add(j)
        return len(visited)==len(rooms)



