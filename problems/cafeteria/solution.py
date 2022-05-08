"""
A cafeteria table consists of a row of N seats, numbered from 1 to N from left to right.

Social distancing guidelines require that every diner be seated such that K seats to their left and K seats to their right (or all the remaining seats to that side if there are fewer than K) remain empty.

There are currently M diners seated at the table, the iith of whom is in seat Si. No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.

Constraints
1 ≤ N ≤ 100000
1 ≤ K ≤ N
1 ≤ M ≤ N
1 ≤ S_i ≤ N

Sample test case #1
N = 10
K = 1
M = 2
S = [2, 6]
Expected Return Value = 3

Sample test case #2
N = 15
K = 2
M = 3
S = [11, 6, 14]
Expected Return Value = 1

Sample Explanation
In the first case, the cafeteria table has N=10 seats, with two diners currently at seats 22 and 66 respectively. The table initially looks as follows, with brackets covering the K=1 seat to the left and right of each existing diner that may not be taken.
  1 2 3 4 5 6 7 8 9 10
  [   ]   [   ]
Three additional diners may sit at seats 44, 88, and 1010 without violating the social distancing guidelines.
In the second case, only 11 additional diner is able to join the table, by sitting in any of the first 33 seats.
"""



import math
from typing import List
# Write any import statements here

def get_max_additional_diners_count(N: int, K: int, M: int, S: List[int]) -> int:
    # S.sort()

    guests = 0
    start = 1
    range_ = None

    for seated_diner in S:
        range_ = seated_diner - start
        guests += math.floor(range_ / (K + 1))
        start = seated_diner + K + 1


    range_ = N - start + 1
    guests += math.ceil(range_ / (K + 1))

    return guests


N = 15
K = 2
M = 3
S = [11, 6, 14]
x = get_max_additional_diners_count(N, K, M, S)
print(x)


# solutio in rust:

