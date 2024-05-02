import copy

initial_state = [['1','2','3'],['4','5','6'],['7','8','-']]
goal_state = [['1','2','3'],['4','8','5'],['-','7','6']]

def cal_cost(current_state,g):
    cost = 0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] != goal_state[i][j] and current_state[i][j] != "-":
                cost+=1
    return g+cost

def print_cost(current_state,g):
    cost = 0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] != goal_state[i][j] and current_state[i][j] != "-":
                cost+=1
    print(f"g(n) = {g+1}")
    print(f"h(n) = {cost}")
    print(f"f(n) = {g+1+cost}")
    return g+cost

def find_index(matrix, element):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == element:
                return (i, j)

def check(current_state,g):
    m,n = find_index(current_state,'-')
    temp_state_left = copy.deepcopy(current_state)
    temp_state_right = copy.deepcopy(current_state)
    temp_state_up = copy.deepcopy(current_state)
    temp_state_down = copy.deepcopy(current_state)  
    cost_left = 0
    cost_right = 0
    cost_up = 0
    cost_down = 0
    #Move left
    if (n-1) == 0 or (n-1) == 1 or (n-1) == 2:
        temp_state_left[m][n] = temp_state_left[m][n-1]
        temp_state_left[m][n-1] = "-"
    #Move right
    if (n+1) == 0 or (n+1) == 1 or (n+1) == 2:
        temp_state_right[m][n] = temp_state_right[m][n+1]
        temp_state_right[m][n+1] = "-"
    #Move up
    if (m-1) == 0 or (m-1) == 1 or (m-1) == 2:
        temp_state_up[m][n] = temp_state_up[m-1][n]
        temp_state_up[m-1][n] = "-" 
    #Move down
    if (m+1) == 0 or (m+1) == 1 or (m+1) == 2:
        temp_state_down[m][n] = temp_state_down[m+1][n]
        temp_state_down[m+1][n] = "-"
    
    if temp_state_left != current_state:
        cost_left = g+cal_cost(temp_state_left,g)
    if temp_state_right != current_state:
        cost_right = g+cal_cost(temp_state_right,g)
    if temp_state_up != current_state:
        cost_up = g+cal_cost(temp_state_up,g)
    if temp_state_down != current_state:
        cost_down = g+cal_cost(temp_state_down,g)

    min_cost = min(cost for cost in [cost_left, cost_right, cost_up, cost_down] if cost != 0)
    if cost_left == min_cost:
        new_state = temp_state_left
        dir = "left"
    elif cost_right == min_cost:
        new_state = temp_state_right
        dir = "right"
    elif cost_up == min_cost:
        new_state = temp_state_up
        dir = "up"
    elif cost_down == min_cost:
        new_state = temp_state_down
        dir = "down"
    return new_state,dir


def astar():
    current_state = initial_state
    g = 0
    print(f"Level {g} : \n")
    for i in range(3):
        for j in range(3):
            print(f"{current_state[i][j]}",end=" ")
        print("\n")
    print_cost(current_state,g=-1)
    while(1):
        if current_state == goal_state:
            print(f"\nSolution found at level {g}")
            break
        elif current_state != goal_state:
            print(f"\nLevel {g+1} : \n")
            current_state,dir = check(current_state,g)
            for i in range(3):
                for j in range(3):
                    print(f"{current_state[i][j]}",end=" ")
                print("\n")
            print("Move : ",dir) 
            print_cost(current_state,g)
        g+=1

if __name__=="__main__":
    astar()
