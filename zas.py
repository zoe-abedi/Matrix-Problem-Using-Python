# Python program to add two Matrices
# Aim : Program to compute the sum of two matrices and then print it in Python. 
# Examples: 

# Input :
#  X= [[1,2,3],
    # [4 ,5,6],
    # [7 ,8,9]]
 
# Y = [[9,8,7],
    # [6,5,4],
    # [3,2,1]]
 
# Output :
#  result= [[10,10,10],
        #  [10,10,10],
        #  [10,10,10]]
# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# We can perform matrix addition in following ways in Python.  



# Using for loop: 

# Program to add two matrices using nested loop
 
# X = [[1,2,3],
    # [4 ,5,6],
    # [7 ,8,9]]
 
# Y = [[9,8,7],
    # [6,5,4],
    # [3,2,1]]
 
 
# result = [[0,0,0],
        # [0,0,0],
        # [0,0,0]]
 
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)
# Output:

# [10, 10, 10]
# [10, 10, 10]
# [10, 10, 10]
# Time Complexity: O(len(X) * len(X[0]))

# Auxiliary Space: O(len(X) * len(X[0]))

# Another Approach:

# Explanation :- 
# In this program we have used nested for loops to iterate through each row and each column. At each point we add the corresponding elements in the two matrices and store it in the result.
# Using nested list comprehension : In Python, we can implement a matrix as nested list (list inside a list). We can treat each element as a row of the matrix. 
 

# Program to add two matrices
# using list comprehension
  
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
  
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
result = [[X[i][j] + Y[i][j]  for j in range
(len(X[0]))] for i in range(len(X))]
  
for r in result:
    print(r)
Output: 

[10, 10, 10]
[10, 10, 10]
[10, 10, 10]
Another Approach:

# Explanation :- 
# The output of this program is the same as above. We have used nested list comprehension to iterate through each element in the matrix. List comprehension allows us to write concise codes and we must try to use them frequently in Python. They are very helpful.
# Using zip() and sum 

# Program to add two matrices
# using zip()
  
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
  
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
result = [map(sum, zip(*t)) for t in zip(X, Y)]
  
print(result)
Output: 

[[10, 10, 10], [10, 10, 10], [10, 10, 10]]