def create_network(b,e,a,j,m):
    b = "burglary"
    e = "earthquake"
    a = "alarm_rings"
    j = "john_calls"
    m = "mary_calls"
    net = [[b,a],[e,a],[a,j],[a,m]]
    print()
    for i in range(len(net)):
        print(f"{net[i][0]} -> {net[i][1]}")

def joint_prob(b,e,a,j,m):
    burg_p = 0.001
    earth_p = 0.002
    p_alarm_given_be = {(True,True) : 0.95,(True,False):0.94,(False,True):0.29,(False,False):0.001}
    p_johncalls_given_alarm = {True:0.90,False:0.05}
    p_marycalls_given_alarm = {True:0.70,False:0.01}

    p_burglary = burg_p if b else (1-burg_p)
    p_earthquake = earth_p if e else (1-earth_p)
    p_alarm = p_alarm_given_be[(b,e)] if a else (1-p_alarm_given_be[(b,e)])
    p_johncalls = p_johncalls_given_alarm[j]
    p_marycalls = p_marycalls_given_alarm[m]
    return p_burglary*p_earthquake*p_alarm*p_johncalls*p_marycalls


b = True if input("Burglary happened (T/F) : ") == "T" else False
e = True if input("Earthquake happened (T/F) : ") == "T" else False
a = True if input("Alarm rang (T/F) : ") == "T" else False
j = True if input("John calls (T/F) : ") == "T" else False
m = True if input("Mary calls (T/F) : ") == "T" else False
create_network(b,e,a,j,m)
p = joint_prob(b,e,a,j,m)
print(f"\nProbability of Burglary = {b}, Earthquake = {e}, Alarm = {a}, JohnCalls = {j}, MaryCalls = {m} : {p}")
