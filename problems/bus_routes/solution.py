from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        transfers = 0
        if source == target:
            return transfers

        # create a stop-to-buses map
        stop_to_bus = defaultdict(set)
        for bus_num in range(len(routes)):
            for i in range(len(routes[bus_num])):
                stop_to_bus[routes[bus_num][i]].add(bus_num)
        
        visited_buses = [False] * len(routes)
        bus_queue = deque([
            stop_to_bus[source] # set of buses
        ])
        while bus_queue[0]:
            current_buses = bus_queue.popleft()
            
            transfers += 1
            bus_queue.append(set())
            for bus in current_buses:
                visited_buses[bus] = True
                for stop in routes[bus]:
                    if stop == target:
                        return transfers

                    # add new bus to visit
                    for next_bus in stop_to_bus[stop]:
                        if not visited_buses[ next_bus ]:
                            bus_queue[-1].add( next_bus )
        return -1