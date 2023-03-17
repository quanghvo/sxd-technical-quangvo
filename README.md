# sxd-technical-quangvo
SXD Software Engineering Intern Technical Exercise
PART I: MATH

In this part, I used a naive and brute force approach to find the optimal solution of x1: 4, x2: 0, and z=-12. This is because it just asks us solve, so I implemented the most basic solution to solve the simple linear programming question.

PART II: Programming

I implemented the solution whilst practicing OOP practices by creating a LPSolution class that takes in the cost function, the objective_fn coefficients, constraints coefficients, and constraints constants to solve the linear programming problem depending on different inputs for X1 and X2. Through my tests, I checked it was able to successfully calculate the problem for similar equations.

PART III: Systems

I chose to implement a NoSQL database using MongoDB. I used a NoSQL database because it can handle large amounts of unstructured data and provide fast querying capabilities as compared to a relational SQL database. We wanted a database to store and retrieve solutions for previously solved optimization problems, so we need to choose a suitable database that can handle quick lookups and retrieval of data. NoSQL databases like MongoDB are optimized for fast reads and writes, and scale horizontally to handle large amounts of data and high traffic, which is perfect in our case. 

I created a function to query the database and check if a problem with the same coefficients and constraints already exist. If it does, we can just return the stored solution; if not, we can just calculate it using part 2's function and store the solution in the database for future use.

If our target user audience are all math students in the US, we would have to size our database largely up accordingly. To prevent overloading a single database instance with requests, we can use sharding and replication to distribute the data across multiple servers, and use a load balancer to distribute the traffic evenly. To further increase performance, we could also add caching to store frequently accessed solutions in memory, or use indexing to optimize query performance. Although in my code I set up the database locally, to accomodate to an audience of all math students, we would definitely prefer to set up our database on cloud infrastructure because of its scalability, reliability and accessibility.

I also included an integration test in which I passed my test cases.