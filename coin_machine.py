#!/usr/bin/env python2.7

#The coin machine or coin change-making problem addresses the following question: how can a given amount of money be made with the least number of coins of given denominations?

import numpy as ny

#use dictionary for memoization
know_solution = {0:{"count":0, "coins":[]}}
def opt_fund(X, coin_set):
	"""
	X: (input) Int 
	"""
	if X in know_solution.keys():
		return know_solution[X]

	for d in coin_set:
		if X == d:
			return {"count":1, "coins": [d]}
				
	
	sub_problems = [{"count":ny.inf, "coins":[d]} for d in coin_set]
	i = 0
	for d in coin_set:
		if X >= d:
			s = opt_fund(X-d, coin_set)
			sub_problems[i]["count"] = 1 + s["count"]
			sub_problems[i]["coins"] = sub_problems[i]["coins"] + s["coins"]

		i = i + 1


	only_counts = ny.array([d["count"] for d in sub_problems])
	opt_sub_problem = sub_problems[ny.where(only_counts == only_counts.min())[0][0]]

	know_solution[X] = opt_sub_problem
	return opt_sub_problem

coin_sets_read = raw_input("Some input the coin set (separate them with ,): ")
coin_sets = [int(d) for d in coin_sets_read.split(',')]

flag = True

while(flag):
	user_input = raw_input("Some input please (negative value to exit): ")
	v = int(user_input)
	if v < 0:
		flag = False
	else:
		print opt_fund(int(user_input), coin_sets)
