import part2
import part3

def lp_program_test1():
    objective_fn = [3, 4]
    constraints = [[15, 10], [2.5, 5]]
    consts = [300, 110]
    lp = part2.LPSolution("max", objective_fn, constraints, consts)
    lp.solve()
    solution = lp.get_solution()
    
    assert(solution["x1"] == 8)
    assert(solution["x2"] == 18)
    assert(solution["z"] == 96)

def lp_program_test2():
    objective_fn = [-3, 1]
    constraints = [[1, 1], [2, 1]]
    consts = [5, 8]
    lp = part2.LPSolution("min", objective_fn, constraints, consts)
    lp.solve()
    solution = lp.get_solution()

    assert(solution["x1"] == 4)
    assert(solution["x2"] == 0)
    assert(solution["z"] == -12)

def db_test1():
    part3.collection.delete_many({})

    objective_fn = [3, 4]
    constraints = [[15, 10], [2.5, 5]]
    consts = [300, 110]
    lp = part2.LPSolution("max", objective_fn, constraints, consts)
    lp.solve()
    solution = lp.get_solution()

    entry = {"costFunction": "max",
           "objective_fn_coeff": objective_fn,
           "constraint_coeff": constraints,
           "constraint_consts": consts,
           "solution": solution}
    
    assert part3.collection.find_one() == None
    part3.collection.insert_one(entry)

    first_entry = part3.collection.find_one()
    assert first_entry["costFunction"] == "max"
    assert first_entry["constraint_coeff"] == [[15, 10], [2.5, 5]]


def db_test2():
    assert len(list(part3.collection.find())) == 1          #from db_test1

    search = part3.collection.find({"costFunction": "max",
                                         "objective_fn_coeff": [3, 4]})
    assert search[0]["costFunction"] == "max"
    assert search[0]["constraint_coeff"] == [[15, 10], [2.5, 5]]
    assert search[0]["solution"]["x1"] == 8
    assert search[0]["solution"]["x2"] == 18
    

def db_test3():
    objective_fn = [-3, 1]
    constraints = [[1, 1], [2, 1]]
    consts = [5, 8]
    lp = part2.LPSolution("min", objective_fn, constraints, consts)
    lp.solve()
    solution = lp.get_solution()

    entry = {"costFunction": "min",
           "objective_fn_coeff": objective_fn,
           "constraint_coeff": constraints,
           "constraint_consts": consts,
           "solution": solution}
    
    part3.collection.insert_one(entry)
    assert len(list(part3.collection.find())) == 2

    search = part3.collection.find()
    assert search[1]["costFunction"] == "min"
    assert search[1]["objective_fn_coeff"] == [-3, 1]
    assert search[1]["solution"]["x1"] == 4
    assert search[1]["solution"]["z"] == -12
    

def db_test4():
    assert len(list(part3.collection.find({"costFunction": "max",
                                  "objective_fn_coeff": [10, 10]}))) == 0
    assert len(list(part3.collection.find({"costFunction": "max",
                                  "objective_fn_coeff": [4, 3],
                                  "solution": {"x1": 8, "x2": 18, "z": 96}}))) == 0
    
def db_test5():
    obj_fn = [3, 4]
    constraints = [[15, 10], [2.5, 5]]
    consts = [300, 110]

    search = part3.collection.find({"costFunction": "max",
                                    "objective_fn_coeff": obj_fn,
                                    "constraint_coeff": constraints,
                                    "constraint_consts": consts})[0]

    solution = search["solution"]
    assert solution["x1"] == 8
    assert solution["x2"] == 18
    assert solution["z"] == 96

def db_lp_solver_test1():
    assert part3.db_lp_solver("min", [-3, 1], [[1, 1], [2, 1]], [5, 8]) == {"x1": 4, "x2": 0, "z": -12}
    assert part3.db_lp_solver("max", [3, 4], [[15, 10], [2.5, 5]], [300, 110]) == {"x1": 8, "x2": 18, "z": 96}

    objective_fn = [3, 4]
    constraints = [[15, 10], [2.5, 5]]
    consts = [300, 110]
    lp = part2.LPSolution("max", objective_fn, constraints, consts)
    lp.solve()
    assert part3.db_lp_solver("max", [3, 4], [[15, 10], [2.5, 5]], [300, 110]) == lp.get_solution()

if __name__ == "__main__":
    lp_program_test1()
    lp_program_test2()
    db_test1()
    db_test2()
    db_test3()
    db_test4()
    db_test5()
    db_lp_solver_test1()
    print("All test cases passed!")