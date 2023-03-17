import pymongo
import part2

try:
    client = pymongo.MongoClient()
except:
    print("Could not connect to MongoDB")

db = client["lpdatabase"]
collection = db["lp"]

# Checks db for the function and constraint coefficients to quickly solution first; if not, calculate it normally
def db_lp_solver(min_or_max, obj, constraints, constants):
    search = collection.find({"costFunction": min_or_max,
                              "objective_fn_coeff": obj,
                              "constraint_coeff": constraints,
                              "constraint_consts": constants})
    if len(list(search)) > 0:
        solution = collection.find({"costFunction": min_or_max,
                              "objective_fn_coeff": obj,
                              "constraint_coeff": constraints,
                              "constraint_consts": constants})[0]["solution"]
        return solution
    else:
        lp = part2.LPSolution(min_or_max, obj, constraints, constants)
        lp.solve()
        collection.insert_one({"costFunction": min_or_max,
                               "objective_fn_coeff": obj,
                               "constraint_coeff": constraints,
                               "constraint_consts": constants,
                               "solution": lp.get_solution()})
        return lp.get_solution()
    
