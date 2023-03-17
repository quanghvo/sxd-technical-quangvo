class Solution:
    def constraints(self, x1, x2):
        if (x1 + x2 <= 5) and (2*x1 + x2 <= 8) and (x1>=0) and (x2>=0):
            return True
        return False
    
    def solve(self):
        x1_range = range(6)
        x2_range = range(9)
        min_z = float("inf")
        x1, x2 = None, None

        for i in x1_range:
            for j in x2_range:
                if self.constraints(i, j):
                    z = -3*i + j
                    if z < min_z:
                        min_z = z
                        x1 = i
                        x2 = j
        
        return x1, x2, min_z

lp = Solution()
solution = lp.solve()
print(f"Optimal Solution:\nx1 = {solution[0]}, x2 = {solution[1]}, min_Z = {solution[2]}")