#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 12:35:36 2020

@author: shambhavisingh
"""
def precedence(operator):
	
	if operator == '+' or operator == '-':
		return 1
	if operator == '*' or operator == '/':
		return 2
	return 0

def calc(x, y, operator):
	
	if operator == '+':
         return x + y
	if operator == '-': 
         return x - y
	if operator == '*': 
         return x * y
	if operator == '/': 
         return x / y

def evaluate(exp):
	
	values = []
	ops = []
	i = 0
	
	while i < len(exp):
		if exp[i] == ' ':
			i += 1
			continue
		
		elif exp[i] == '(':
			ops.append(exp[i])
		
		elif exp[i].isdigit():
			val = 0
			
			while (i < len(exp) and
				exp[i].isdigit()):
			
				val = (val * 10) + int(exp[i])
				i += 1
			
			values.append(val)
			
			
			i-=1
		
		elif exp[i] == ')':
		
			while len(ops) != 0 and ops[-1] != '(':
			
				num2 = values.pop()
				num1 = values.pop()
				op = ops.pop()
				
				values.append(calc(num1, num2, op))
			
			
			ops.pop()
		
		else:
		
			while (len(ops) != 0 and
				precedence(ops[-1]) >=
				precedence(exp[i])):
						
				num2 = values.pop()
				num1 = values.pop()
				op = ops.pop()
				
				values.append(calc(num1, num2, op))
			
			
			ops.append(exp[i])
		
		i += 1
	
	
	while len(ops) != 0:
		
		num2 = values.pop()
		num1 = values.pop()
		op = ops.pop()
				
		values.append(calc(num1, num2, op))
	
	
	return values[-1]

print("Welcome to Calculator")
num = input("Enter expression: ")

print(evaluate(num))
