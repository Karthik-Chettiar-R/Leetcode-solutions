class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        # cost of both greater than sum of individual
        if costBoth>=cost1+cost2:
            return cost1*need1+cost2*need2

            

        cost=0
        # cost of both less than cost1
        if costBoth<=cost1:
            # cost of both less than cost 2
            if costBoth<=cost2:
                return costBoth*max(need1,need2)
            # cost of both greater than cost 2
            else:
                cost+=costBoth*need1
                need2-=need1
                if need2>0:
                    cost+=need2*cost2
                return cost  

        cost=0

        # cost of both less than cost2
        if costBoth<=cost2:
            # cost of both less than cost 1
            if costBoth<=cost1:
                return costBoth*max(need1,need2)
            # cost of both greater than cost 1
            else:
                cost+=costBoth*need2
                need1-=need2
                if need1>0:
                    cost+=need1*cost1
                return cost 

            
        cost=0

        # cost of both greater than both the individuals

        

        if need1>=need2:
            cost+=need2*costBoth
            need1-=need2
            cost+=need1*cost1
            return cost

        cost+=need1*costBoth
        need2-=need1
        cost+=need2*cost2

        return cost
            

        