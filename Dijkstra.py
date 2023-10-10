import sys
from datetime import time, timedelta, datetime
from copy import copy


"""
Tiago is a dedicated student of comedy. He doesn't like to be late in any way
and always tries to arrive no later than 6:00 pm, which is the start time of comedy class.
Tiago leaves the CDS building at 5:00 pm, and it takes walk_time_to_station minutes
for him to get to the bus stop from his office.
Buses leave from the nearest station to the office
only once at 5:30 and another time at 5:50 PM.
Tiago needs to know when he will arrive at the comedy center by choosing the best route and if he will be late.

Your task is, considering N possible bus connections,
to determine at what time Tiago will arrive at the comedy center taking the fastest route.
His trip starts by a walk from the office to the bus stop.
Then, he takes bus trip starting from the `cds' station at either 5:30 or 5:50.
Assume no walk time between connecting trips.
Note that the time T from station A to station B is not the same as from station B to station A because traffic in the opposite direction may be different.
Assume that Tiago will always reach the bus stop at most 5:50 and that there will always be a route between CDS to the comedy center.

INPUT:
    integer value indicating Tiago's walking time from the office to the station, and
    adjacency list of the graph representing the directed bus connections and time for each connection

OUTPUT:
    Your function should output a pair of string and boolean values.
    The string should be the arrival time at the comedy center in the format HH:MM.
    The boolean value should be True iff Tiago will be late.
"""

#!!!!!!!!You are allowed to import and use datetime Python library!!!!!!!!!

#Test Case 1:
"""
walk_time_to_station = 35
{
'cds': {'harvard': 5, 'comedycenter': 25},
'harvard': {'airport': 5},
'airport': {'comedycenter': 5},
'comedycenter': {}
}

OUTPUT:
(18:05, True)
"""

#Test Case 2:
"""
walk_time_to_station = 15
{
'cds': {'harvard': 10, 'comedycenter': 30},
'harvard': {'airport': 15},
'airport': {'comedycenter': 10},
'comedycenter': {}
}

OUTPUT:
(18:00, False)
"""


"""
This is the function that will be autograded. It computes Tiago's arrival time and whether he will be late.
Parameters:
walk_time_to_station: time Tiago takes to walk from CDS building to CDS station
adj_list: adjacency list of all bus connections
Returns:
pair of values indicating arrival time (HH:MM format) and whether Tiago is late
"""
def convert_to_preferred_format(sec):
   sec = sec % (24 * 3600)
   hour = sec / 3600
   sec %= 3600
   min = sec / 60
   sec %= 60
   return "%02d:%02d" % (hour, min)



def compute_arrival_time(walk_time_to_station, adj_list):
    #run shortest path algorithm
    #You do not have to implement this function, but it is encouraged.
    is_late = False
    shortest_distances_to_comedy_center = compute_shortest_distances_with_dijkstra(adj_list, 'cds','comedycenter')
    #look up shortest distance to comedycenter
    seconds_total = 0
    
    
    
    if walk_time_to_station > 30 and walk_time_to_station <= 50:
        total_time = timedelta(hours = 17,minutes=50)
        
        time_var = timedelta(minutes=shortest_distances_to_comedy_center)
        total_time += time_var
        seconds_total = total_time.total_seconds()
        if shortest_distances_to_comedy_center > 10:
            is_late = True
    if walk_time_to_station <= 30:
        total_time = timedelta(hours = 17,minutes=30)
        time_var = timedelta(minutes=shortest_distances_to_comedy_center)
        total_time += time_var
        seconds_total = total_time.total_seconds()
        if shortest_distances_to_comedy_center > 30:
            is_late = True
    converted = convert_to_preferred_format(seconds_total)

    """
    Your code here ....
    these are the variables to be returned
    arrival_time_at_comedycenter_str = ... #string in format HH:MM
    is_late = ... #boolean variable
    """
    return (converted, is_late)


"""
Compute shortest distances from a starting node in directed graph.
You do not have to implement this function, but it is encouraged.
Parameters:
adj_list: adjacency list of the graph
start: starting vertex
Returns:
table of the shortest paths of all nodes in the graph
"""
def compute_shortest_distances_with_dijkstra(adj_list, start, end):
    keys={} 
    order={}
    for i in adj_list.keys():
        if i == start: 
            keys[i] = 0 
        else: 
            keys[i] = float("inf") 
    copy_of_keys = copy(keys) 
    while len(copy_of_keys) > 0:
        minimum = min(copy_of_keys, key = copy_of_keys.get)
        for i in adj_list[minimum]:
            if keys[i] > (keys[minimum] + adj_list[minimum][i]):
                keys[i] = keys[minimum] + adj_list[minimum][i]
                copy_of_keys[i] = keys[minimum] + adj_list[minimum][i]
                order[i] = minimum
        del copy_of_keys[minimum] 
    return keys[end]

G = {
'cds': {'harvard': 10, 'comedycenter': 30},
'harvard': {'airport': 15},
'airport': {'comedycenter': 10},
'comedycenter': {}
}

G2 = {
'cds': {'harvard': 5, 'comedycenter': 25},
'harvard': {'airport': 5},
'airport': {'comedycenter': 5},
'comedycenter': {}
}

print(compute_arrival_time(15,G))
print(compute_arrival_time(30,G2))

G3 = {'cds': {'harvard': 500, 'comedycenter': 25000}, 'harvard': {'airport': 1000}, 'airport': {'comedycenter': 500}, 'comedycenter': {}}
print(compute_arrival_time(30, G3))