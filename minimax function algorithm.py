class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda x:x[0]-x[1])
        
        n = len(costs)
        cost = 0
        
        for c in costs[:int(n/2)]:
            cost += c[0]
        for c in costs[int(n/2):]:
            cost += c[1]
            
        return cost