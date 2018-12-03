def checksum():
	text_input = open('input.txt', "r")

	letter_count = {2: 0, 3: 0}

	for line in text_input:
		line = line.rstrip()
		line_dict = {}
		two_count = False
		three_count = False
		for letter in line:
			line_dict[letter] = line_dict.get(letter, 0) + 1

		for letter, count in line_dict.items():
			if count == 2:
				two_count = True
			if count == 3:
				three_count = True

		if two_count:
			letter_count[2] += 1
		if three_count:
			letter_count[3] += 1


	return letter_count[2] * letter_count[3]


def find_similar_ids():
	text_input = open('input.txt', "r")
	all_inputs = []

	for line in text_input:
		all_inputs.append(line.rstrip())

	similar_codes = []

	for i in range(len(all_inputs)):
		current_code = all_inputs[i]
		other_codes = all_inputs[i:]
		for code in other_codes:
			count_diffs = 0
			for a, b in zip(current_code, code):
				if a!= b:
					count_diffs += 1
			if count_diffs == 1:
				similar_codes.append(current_code)
				similar_codes.append(code)

	seen_letters = []

	for index, letter in enumerate(similar_codes[0]):
		if letter == similar_codes[1][index]:
			seen_letters.append(letter)

	return "".join(seen_letters)
