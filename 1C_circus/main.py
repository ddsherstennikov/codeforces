"""
http://codeforces.com/problemset/problem/1/A
"""

import sys
import math


def gcd(a, b):
	if a < b:
		a, b = b, a
		
	while b > 1:
		a, b = b, a % b
	
	return a


def square(arr):
	a = math.sqrt( (arr[2][0]-arr[1][0])**2 + (arr[2][1]-arr[1][1])**2 )
	b = math.sqrt( (arr[2][0]-arr[0][0])**2 + (arr[2][1]-arr[0][1])**2 )
	c = math.sqrt( (arr[1][0]-arr[0][0])**2 + (arr[1][1]-arr[0][1])**2 )
	p = 0.5 * (a+b+c)
	R = a*b*c / (4 * math.sqrt(p*(p-a)*(p-b)*(p-c)))
	
	alpha = math.acos(round((2 * R ** 2 - c ** 2) / (2 * R ** 2), 9)) * 180 / math.pi
	beta = math.acos(round((2 * R ** 2 - a ** 2) / (2 * R ** 2), 9)) * 180 / math.pi
	gamma = math.acos(round((2 * R ** 2 - b ** 2) / (2 * R ** 2), 9)) * 180 / math.pi
	delta = gcd(alpha, gcd(beta, gamma))
	
	n = 360 / delta
	i = 2
	
	while abs(round(n) - n) > 0.1:
		delta_loop = delta / i
		n = 360 / delta_loop
		i += 1
		
	n = round(n)
	s = (n/2)*(R**2)*math.sin(2*math.pi/n)
	
	return s


def main():
	arr = []
	
	for i in range(3):
		l = sys.stdin.readline()
		x, y = [float(t) for t in l.split()]
		arr.insert(i-1, (x, y))
	
	s = square(arr)
	print("%.6f" % s)


if __name__ == '__main__':
	main()