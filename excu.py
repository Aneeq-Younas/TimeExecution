
import time

def sec(b):
    Time_S = time.time()
    a= 0

    for x in range (2, b +2):
        a= a + x

    Time_E = time.time()
    return a, Time_S-Time_E

b= 10
print("The code Execution time is: ", sec(b))
