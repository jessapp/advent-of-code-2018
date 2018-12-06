def parse_input():
	letters = []
	text_input = open('input.txt', "r")
	for line in text_input:
		for letter in line.rstrip():
			letters.append(letter)
	return letters

# polymer_list = ["C", "c", "v", "V", "e", "G", "g", "R", "b", "B", "x", "C", "c", "X", "b", "J", "t","T"]
# polymer_list = ["d", "a", "b", "A", "c", "C", "a", "C", "B", "A", "c", "C", "c", "a", "D", "A"]


def are_opposites(first_letter, second_letter):
	return first_letter == second_letter.lower() or second_letter == first_letter.lower()


# def part_one():
# 	polymer_list = parse_input()

# 	first_index = 0
# 	last_index = len(polymer_list) - 1

# 	while first_index < last_index:
# 		first_letter = polymer_list[first_index]
# 		second_letter = polymer_list[first_index + 1]

# 		# If the two letters are the same 
# 		if are_opposites(first_letter, second_letter)
# 			# Delete the two keys
# 			del polymer_list[first_index + 1]
# 			del polymer_list[first_index]
# 			last_index = len(polymer_list) - 1

# 			# Move one step back, if possible, because the previous letter might match the next letter
# 			if first_index > 0:
# 				first_index -= 1

# 		# Otherwise, move forward
# 		else:
# 			first_index += 1



def part_one():
	polymer_list = parse_input()
	return_list = []
	for letter in polymer_list:
		if return_list and are_opposites(letter, return_list[-1]):
			return_list.pop()
		else:
			return_list.append(letter)

	return len(return_list)


# 11848 - too high