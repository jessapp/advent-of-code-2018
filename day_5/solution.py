import string
import re

# def parse_input():
# 	letters = []
# 	text_input = open('input.txt', "r")
# 	for line in text_input:
# 		for letter in line.rstrip():
# 			letters.append(letter)
# 	return letters

# def are_opposites(first_letter, second_letter):
# 	return first_letter == second_letter.lower() or second_letter == first_letter.lower()


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


# def part_one():
# 	polymer_list = parse_input()
# 	return_list = []
# 	for letter in polymer_list:
# 		if return_list and are_opposites(letter, return_list[-1]):
# 			return_list.pop()
# 		else:
# 			return_list.append(letter)

# 	return len(return_list)


# part 1
def regex(polymer):
	lower = string.ascii_lowercase
	upper = string.ascii_uppercase
	pat = "|".join(
	    a + b for a, b in list(zip(lower, upper)) + list(zip(upper, lower)))
	ss = re.sub(pat, "", polymer)
	while polymer != ss:
	    polymer = ss
	    ss = re.sub(pat, "", polymer)

	return len(polymer)


def part_two():
	shortest_length = None

	for x in string.ascii_lowercase:
		text_input = open("input.txt").read().strip()
		text_input = text_input.replace(x, "")
		text_input = text_input.replace(x.upper(), "")
		reduced_length = regex(text_input)

		if not shortest_length or reduced_length < shortest_length:
			shortest_length = reduced_length

	return shortest_length
