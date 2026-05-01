class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]

        time = 0
        count = 0
        for t in times:
            if t > time:
                count += 1
                time = t
        return count
        