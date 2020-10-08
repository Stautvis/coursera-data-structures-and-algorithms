# python3
import sys


def compute_min_refills(distance, tank, stops):
    last_stop = 0
    counter = 0
    #add finish distance
    stops.append(distance)

    if(distance <= tank):
        return 0 #there is no need to refill
    
    for i in range(len(stops) - 1):
        current_stop = stops[i]
        next_stop = stops[i + 1]
        
        if(next_stop - current_stop > tank):
            return -1
        if(next_stop - last_stop <= tank):
            continue
        else:
            last_stop = current_stop
            counter += 1
    return counter

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
