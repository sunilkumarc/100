def get_all_substrings(input_string):
	length = len(input_string)
	return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

T = int(input().strip())

for i in range(T):
	M, N = map(int, input().strip().split())
	string = input().strip()

	substrings = get_all_substrings(string)
	Rres = 0
	Kres = 0
	for sub in substrings:
		RCount = 0
		KCount = 0
		for char in sub:
			if char == 'R':
				RCount += 1
			elif char == 'K':
				KCount += 1
		
		if RCount == M:
			Rres += 1
		if KCount == N:
			Kres += 1
			
  print(str(Rres) + " " + str(Kres))
