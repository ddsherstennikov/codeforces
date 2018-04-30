"""
http://codeforces.com/problemset/problem/1/A
"""

import sys


def find_min_plates(n, m, a):
	q_n = int(n / a)
	q_m = int(m / a)
	d_n = (1 if n % a > 0 else 0)
	d_m = (1 if m % a > 0 else 0)
	
	count = q_n * q_m + d_n * (q_m + d_m) + d_m * q_n
	
	return count

def main():
	l = sys.stdin.readline()
	n, m, a = [int(t) for t in l.split()]
	print(find_min_plates(n, m, a))

if __name__ == '__main__':
	main()