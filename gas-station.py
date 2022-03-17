class Solution:
    # O(n)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = [g - c for g, c in zip(gas, cost)]
        
        if sum(tank) < 0:
            return -1
        
        start, fuel = 0, 0
        for station in range(len(tank)):
            if fuel + tank[station] < 0:
                start = station + 1
                fuel = 0
            else:
                fuel += tank[station]
        
        return start

    # conditional brute force: O(n^2)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = [g - c for g, c in zip(gas, cost)]
        
        station = 0
        while station < len(tank):
            if tank[station] >= 0 and tank[station - 1] < 0:
                fuel = tank[station]
                s = (station + 1) % len(tank)
                while s != station:
                    fuel += tank[s]
                    if fuel < 0:
                        break
                    s = (s + 1) % len(tank)
                else:
                    return station

            elif len(tank) == 1 and sum(tank) >= 0:
                return 0
            
            station += 1
        
        return -1