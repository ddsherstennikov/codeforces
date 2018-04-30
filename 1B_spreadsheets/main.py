"""
http://codeforces.com/problemset/problem/1/B
"""

import sys
import re


def to_letters(digits):
	n = int(digits)
	res = ""
	
	while n > 0:
		c = 'Z' if n % 26 == 0 else chr(ord('A') + n % 26 - 1)
		n = n // 26 - (1 if c == 'Z' else 0)
		res = c + res
		
	return res


def from_letters(letters):
	res = 0
	
	for c in letters:
		if res:
			res *= 26
		res += ord(c) - ord('A') + 1
		
	return str(res)


def translate(s):
	match = re.search('R(\d+)C(\d+)', s)
	res = ""
	
	# R22C55
	if(match):
		row = match.group(1)
		col = match.group(2)
		
		res += to_letters(col)
		res += row
		
	# AB53
	else:
		match = re.search('([A-Z]+)(\d+)', s)
		if(not match):
			return res
		
		col = match.group(1)
		row = match.group(2)
		
		res += 'R' + row + 'C' + from_letters(col)
	
	return res


def main():
	n = int(sys.stdin.readline())
	sa = []
	
	for i in range(n):
		sa.append(sys.stdin.readline())
	
	for s in sa:
		print(translate(s))


if __name__ == '__main__':
	main()