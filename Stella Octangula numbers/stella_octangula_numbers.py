#!/usr/bin/env python3

def print_single_term():
	t = int(input('[+] Enter the Index:'))
	print('[*] Term at Index '+str(t))
	print(t*(2*pow(t,2)-1))

def print_series():
	t = int(input('[+] Enter the Index:'))
	for i in range(t+1):
		print('[*] Term at Index '+str(i))
		print(i*(2*pow(i,2)-1))

print('Stella Octangula number series using python')
print('Enter your choice:')
print('[1] Print the single term of the series')
print('[2] Print series till term specified')
n = int(input())
if n == 1:
	print_single_term()
elif n == 2:
	print_series()
else:
	print('[!] Enter valid choice')