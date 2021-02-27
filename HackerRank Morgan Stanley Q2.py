Given the savings, current value and future value of a stock this returns the maximum profit possible.

def selectStock(saving, currentValue, futureValue):
    mem = {}
    for i, j in enumerate(currentValue):
        mem[j] = futureValue[i] - j
    
    global_max = 0
    
    for i in currentValue:
        bank = saving
        seen = []
        values = currentValue.copy()
        values.remove(i)
        bank -= i
        stack = sorted([j for j in values if j <= bank])
        stack_1 = []
        temp_max = mem[i]
        
        while stack:
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
        
        global_max = max(global_max, temp_max)
        
    return global_max
                
            
        
                
            
            
            
print(selectStock(250, [175,133,109,210,97, 24], [200,125,128,228,133, 30]))
            
    
   

    
    
    
