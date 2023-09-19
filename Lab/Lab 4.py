## Lab 4 Exercises ##
import numpy as np

## 1.
x = np.array([[1,2,0,0],[5,6,0,0],[0,0,3,4],[0,0,7,8]])
# (a) Create a copy of top left 2 by 2 subarray and assign it to x_block1.
x_block1 = x[:2,:2]

# (b) Create a copy of bottom right 2 by 2 subarray and assign it to x_block2.
x_block2 = x[2:,2:]

# (c) Do a matrix multiplication, x_block1 times x_block2 and assign in to x_new.
x_new = np.dot(x_block1,x_block2)
# (d) Find a transpose of x_new and assign in to x_new_t.
x_new_t = x_new.T
# (e) Find a minimum values in each row of x_new_t.
row_min = np.min(x_new_t, axis =1 )
# (f) Find a maximum values in each column of x_new_t.
row_max = np.max(x_new_t,axis=0)
# (g) Find a sum of all values in x_new_t.
total_sum = np.sum(x_new_t)
# (h) Count how many values in x_new_t is either less than 20 or greater than 60.
count = x_new_t[(x_new_t <20)|(x_new_t>60)].size
# (i) If the values in x_new_t is greater than 30 then change it to 1 otherwise 2 and assign it to x_final.
x_final= np.where(x_new_t >30,1,2)

# (j) Sort each row of x_final in ascending order and assign it to x_final_sorted.
x_final_sorted = np.sort(x_final)

## 2.
np.random.seed(seed=1)
y = np.random.randint(0, 100, 20)

# (a) Find a subset of y which only contain numbers in the odd positions. For example, if your y = [5,10,15,20,25] then write a code to find [5,15,25].
odd_positions = y[1::2]
# (b) Find the mean and standard deviation of the subset you found in (a).
mean_odd_posistions = np.mean(odd_positions)
std_odd_positions = np.std(odd_positions)
