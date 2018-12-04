from collections import defaultdict

def get_coordinate_info():
	text_input = open('input.txt', "r")
	all_inputs = []
	coordinate_info = []

	for line in text_input:
		all_inputs.append(line.rstrip())

	for line in all_inputs:
		line_input = line.replace(' ', '').replace('#', '').replace('@', ':').replace('x', ':').replace(',', ':')
		line_input = line_input.split(":")
		coordinate_info.append(line_input)

	return coordinate_info


def create_coordinate_mapping():
	coordinates = get_coordinate_info()
	fabric_squares = defaultdict(list)

	for coordinate in coordinates:
		claim_number, x, y, w, h = coordinate
		x_squares = [(i + int(x), int(y)) for i in range(int(w))]
		claimed_squares = [(int(x), int(y) + i) for x, y in x_squares for i in range(int(h))]
		for square in claimed_squares:
			fabric_squares[square].append(claim_number)

	return fabric_squares

# Part 1

def get_overlapping_squares():
	fabric_squares = create_coordinate_mapping()

	total_overlapping = 0
	for key, val in fabric_squares.items():
		if len(val) > 1:
			total_overlapping += 1

	return total_overlapping


# Part 2
def get_non_overlapping_claim():
	coordinates = get_coordinate_info()
	claim_ids = set([coordinate[0] for coordinate in coordinates])
	fabric_squares = create_coordinate_mapping()
	
	multiple_claims = set()
	for coordinate, claims in fabric_squares.items():
		if len(claims) > 1:
			for claim in claims:
				multiple_claims.add(claim)

	return claim_ids - multiple_claims


