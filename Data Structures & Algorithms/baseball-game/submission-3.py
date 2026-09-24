class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for n in operations:
            if n.lstrip("-").isdigit():
                points.append(int(n))
            elif n == "+":
                points.append(points[-1] + points[-2])
            elif n == "D":
                points.append(2 * points[-1])
            elif n == "C":
                points.pop()

        res = 0

        for i in points:
            res += int(i)
        return res


                



        