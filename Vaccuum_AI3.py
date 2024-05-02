def left_dirty():
    print("Left room is dirty... Sucking dirt")
    print("Done")

def left_clean():
    print("Left room is already clean")

def right_dirty():
    print("Right room is dirty... Sucking dirt")
    print("Done")

def right_clean():
    print("Right room is already clean")

def vaccuum():
    initial_loc = input("Enter the initial location of the vaccuum cleaner (left/right) : ").lower()
    left_state = input("Enter the state of left room (clean/dirty) : ").lower()
    right_state = input("Enter the state of right room (clean/dirty) : ").lower()
    if initial_loc == "right" :
        if left_state == "clean":
            if right_state == "dirty":
                right_dirty()
                print("Moving left...")
                left_clean()
                print("Both rooms are clean... Exiting...")
            elif right_state == "clean":
                right_clean()
                print("Moving left...")
                left_clean()
                print("Both rooms are clean... Exiting...")
        elif left_state == "dirty":
            if right_state =="dirty":
                right_dirty()
                print("Moving left...")
                left_dirty()
                print("Both rooms are clean... Exiting...")
            elif right_state =="clean":
                right_clean()
                print("Moving left...")
                left_dirty()
                print("Both rooms are clean... Exiting...")

    if initial_loc == "left" :
        if right_state == "clean":
            if left_state =="clean":
                left_clean()
                print("Moving right...")
                right_clean()
                print("Both rooms are clean... Exiting...")
            elif left_state =="dirty":
                left_dirty()
                print("Moving right...")
                right_clean()
                print("Both rooms are clean... Exiting...")
        elif right_state == "dirty":
            if left_state =="clean":
                left_clean()
                print("Moving left...")
                right_dirty()
                print("Both rooms are clean... Exiting...")
            elif left_state =="dirty":
                left_dirty()
                print("Moving right...")
                right_dirty()
                print("Both rooms are clean... Exiting...")

                
if __name__=="__main__":
    vaccuum()