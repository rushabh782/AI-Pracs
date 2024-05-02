def execute_action(action):
    global clear, on, on_table, hand
    if action[0] == "ON":  # ON 1 2
        if action[1] + "*" + action[2] in on:
            return
        else:
            execute_action(["CL", action[2]])  # Ensure block 2 is clear
            execute_action(["HL", action[1]])  # Ensure block 1 is held
            print(f"Stack({action[1]}, {action[2]})")
            clear.remove(action[2])
            clear.add(action[1])
            on.add(action[1] + "*" + action[2])
            hand = None
    elif action[0] == "CL":  # CLEAR 1
        if action[1] in clear:
            return
        else:
            a = action[1]
            b = None
            for item in on:
                if a == item[2]:
                    b = item[0]
                    break
            if b is None:
                return
            execute_action(["CL", b])
            execute_action(["ON", b, a])
            execute_action(["AE"])
            hand = b
            clear.add(a)
            clear.add(b)
            on_table.add(a)
            on.remove(b + "*" + a)
            print(f"UnStack({b}, {a})")
    elif action[0] == "AE":  # ARM EMPTY
        if hand is None:
            return
        else:
            print(f'PutDown({hand})')
            on_table.add(hand)
            hand = None
    elif action[0] == "ONT":  # ON TABLE 1
        if action[1] in on_table:
            return
        else:
            b = None
            a = action[1]
            for item in on:
                if a == item[2]:
                    b = item[0]
                    break
            if b is None:
                return
            execute_action(["CL", b])
            execute_action(["ON", b, a])
            execute_action(["AE"])
            hand = b
            clear.add(a)
            clear.add(b)
            on_table.add(a)
            on.remove(b + "*" + a)
            print(f'UnStack({b}, {a})')
    elif action[0] == "HL":  # Holding
        if hand == action[1]:
            return
        else:
            execute_action(["CL", action[1]])
            execute_action(["ONT", action[0]])
            execute_action(["AE"])
            hand = action[1]
            on_table.remove(hand)
            print(f'PickUp({hand})')
# Initial state and goal state representation
initial_state = [["B"], ["A", "C"]]
goal_state = [["A", "B", "C"]]
# Database initialization
on_table = set()
on = set()
clear = set()
hand = None
# Populate initial state in the database
for state in initial_state:
    clear.add(state[0])  # First in list is clear
    on_table.add(state[-1])  # Last in list is on table
    for i in range(len(state) - 1):
        on.add(state[i] + "*" + state[i + 1])  # Block on another block
# Print initial state
print("Initial State:")
print("Clear:", clear)
print("On Table:", on_table)
print("On:", on)
print("Hand:", hand)
# Print goal state
print("\nPLAN:")
# Start with satisfying goal state
for goal in goal_state:
    execute_action(["CL", goal[0]])
    for i in range(len(goal) - 2, -1, -1):
        execute_action(["ON", goal[i], goal[i + 1]])
    execute_action(["ONT", goal[-1]])
    execute_action(["AE"])
print("\nGoal state : ")
print("CLEAR : ",clear)
print("ON TABLE : ",on_table)
print("ON : ",on)
print("HAND : ",hand)