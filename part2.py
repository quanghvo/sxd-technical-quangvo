from pulp import *

class LPSolution():
    def __init__(self, min_or_max, obj, constraints, constants):
        if min_or_max == "min":
            self.model = LpProblem("LP_Problem", LpMinimize)
        elif min_or_max == "max":
            self.model = LpProblem("LP_Problem", LpMaximize)
        self.obj = obj
        self.constraints = constraints
        self.constants = constants
        self.variables = [LpVariable(f"x{i+1}", lowBound=0) for i in range(len(self.constraints[0]))]
        self.solution = None

    def solve(self):
        #add objective function
        self.model += self.obj[0] * self.variables[0] + self.obj[1] * self.variables[1]

        #adds the constraints
        for i in range(len(self.constraints)):
            self.model += self.constraints[i][0] * self.variables[0] + self.constraints[i][1] * self.variables[1] <= self.constants[i]

        self.model.solve(PULP_CBC_CMD(msg=False))

        self.solution = {}
        for var in self.variables:
            self.solution[var.name] = var.value()
        self.solution['z'] = self.model.objective.value()
    
    def get_solution(self):
        return self.solution


