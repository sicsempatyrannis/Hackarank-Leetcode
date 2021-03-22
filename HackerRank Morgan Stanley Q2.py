
## Iterative solution
def selectStock(saving, currentValue, futureValue):
    mem = {}
    for i, j in enumerate(currentValue):
        mem[j] = futureValue[i] - j
    
    global_max = 0
    

    for i in currentValue:
        bank = saving
        seen = []
        bank -= i
        stack = sorted([j for j in currentValue if j <= bank and j != i])
        stack_1 = []
        temp_max = mem[i]
        
        while stack:
            global_max = max(global_max, temp_max)
            top = stack.pop()

            if top > bank and top not in seen:
                add = stack_1.pop()
                bank += add
                temp_max -= mem[add]
                stack.append(top)
                
            else:
                bank -= top
                seen.append(top)
                stack_1.append(top)
                temp_max += mem[top]
               
    return global_max

print(selectStock(250, [175,133,109,210], [200,125,128,228]))

## Recursive solution
class Solution:
    def __init__(self):
        self.global_max = 0
        self.visited = None
        
    def selectStock(self, saving, currentValue, futureValue):
        self.current = currentValue
        
        self.path ={}
        
        mem = {}
        for i, j in enumerate(currentValue):
            mem[j] = futureValue[i] - j
      
        self.visited = [0] * len(currentValue)
        
        def dfs(i, bank, profit, track):
            
            
            if bank < self.current[i]:
                self.global_max = max(profit, self.global_max)
                self.path[profit] = track.copy()
                return
            
            track.append(self.current[i])
            bank -= self.current[i]
            profit += mem[self.current[i]]
            self.visited[i] = -1
            
            for m, n in enumerate(currentValue):
                if self.visited[m] != -1:
                    dfs(m, bank, profit, track.copy())
                    
            self.visited[i] = 1
            
        for v, k in enumerate(currentValue):
            if k <= saving:
                dfs(v, saving, 0, [])
         
        print(self.path)
        return self.global_max
            
print(Solution().selectStock(6000, [1000, 400, 786, 876, 456, 854, 6584], [2000, 52, 788, 885, 800, 521, 1000, 542])) 
    


    
    
    
