# 3 water jugs capacity -> (x,y,z) where x>y>z 
# initial state (12,0,0) 
# final state (6,6,0)
print("******WATER JUG PROBLEM******")

"""Begin the operations to empty Jug A.
a. If Jug A has water (a > 0):
- Try to empty Jug A into Jug B:
- If the sum of the water levels in Jug A and Jug B is less than or equal to the capacity of Jug B (a+b <= y), proceed:
- Call the get_all_states function recursively with the new state (0, a+b, c).
- If the recursive call returns True, append the current state to the ans list and return True.
- If the sum of the water levels in Jug A and Jug B exceeds the capacity of Jug B (a+b > y), proceed:
- Call the get_all_states function recursively with the new state (a-(y-b), y, c).
- If the recursive call returns True, append the current state to the ans list and return True.
- Try to empty Jug A into Jug C:
- If the sum of the water levels in Jug A and Jug C is less than or equal to the capacity of Jug C (a+c <= z), proceed:
- Call the get_all_states function recursively with the new state (0, b, a+c).
- If the recursive call returns True, append the current state to the ans list and return True.
- If the sum of the water levels in Jug A and Jug C exceeds the capacity of Jug C (a+c > z), proceed:
- Call the get_all_states function recursively with the new state (a-(z-c), b, z).
- If the recursive call returns True, append the current state to the ans list and return True.
Repeat the same operations for emptying Jug B and Jug C."""

capacity = [12,8,5]
# Maximum capacities of 3 jugs -> x,y,z 
x = capacity[0] 
y = capacity[1] 
z = capacity[2] 

# to mark visited states 
memory = {} 

# store solution path 
ans = []

#Define the get_all_states recursive function that takes a state
#(a tuple of water levels in jugs) as input
def get_all_states(state):
    
# Let the 3 jugs be called a,b,c 
    a = state[0] 
    b = state[1] 
    c = state[2]
    """Check if the desired state (a=6 and b=6) is reached.
If so, append the state to the ans list and return True"""
    
    if(a==6 and b==6): 
        ans.append(state) 
        return True 
    
# if current state is already visited earlier 
    if((a,b,c) in memory): 
        return False 
    memory[(a,b,c)] = 1


    #empty jug a 
    if(a>0): 
        #empty a into b 
        if(a+b<=y): 
            if( get_all_states((0,a+b,c)) ): 
                ans.append(state) 
                return True 
        else: 
            if( get_all_states((a-(y-b), y, c)) ): 
                ans.append(state) 
                return True 
        #empty a into c 
        if(a+c<=z): 
            if( get_all_states((0,b,a+c)) ): 
                ans.append(state) 
                return True 
        else: 
            if( get_all_states((a-(z-c), b, z)) ): 
                ans.append(state) 
                return True 
    
    #empty jug b 
    if(b>0): 
        #empty b into a
        if(a+b<=x): 
            if( get_all_states((a+b, 0, c)) ): 
                ans.append(state) 
                return True 
        else: 
            if( get_all_states((x, b-(x-a), c)) ): 
                ans.append(state) 
                return True 
    
        #empty b into c 
        if(b+c<=z): 
            if( get_all_states((a, 0, b+c)) ): 
                ans.append(state) 
                return True 
        else: 
            if( get_all_states((a, b-(z-c), z)) ): 
                ans.append(state) 
                return True 
    
    #empty jug c 
    if(c>0): 
        #empty c into a 
        if(a+c<=x): 
            if( get_all_states((a+c, b, 0)) ): 
                ans.append(state) 
                return True 
        else: 
            if( get_all_states((x, b, c-(x-a))) ): 
                ans.append(state) 
                return True 
    
        #empty c into b 
        if(b+c<=y): 
            if( get_all_states((a, b+c, 0)) ): 
                ans.append(state) 
                return True 
        else: 
            if( get_all_states((a, y, c-(y-b))) ): 
                ans.append(state) 
                return True 
    return False
    
initial_state = (12,0,0) 
print("Starting work...\n") 
get_all_states(initial_state) 
ans.reverse() 
for i in ans: 
    print(i) 
