import json
import random
from pprint import pprint 
from operator import itemgetter

with open('books.json') as data_file:
	books = json.load(data_file)

def generatePickPath(length):
	book_list = []
	
	# Create a list with {length} random books:
	for i in range(length):
		random_pick = random.choice(books)
		while random_pick["author"] is None:
			random_pick = random.choice(books)
		book_list.append(random.choice(books))

	# Isolate author last name and set it as sort key:
	for i in range(length):
		current_author = book_list[i]["author"]
		processed_author = ""
		for char in str(current_author):
			if not char.isdigit() and char != "-" and char != ".":
				processed_author += char
		processed_author = processed_author.rstrip()
		last_name = processed_author[processed_author.rfind(" ") + 1 :]
		book_list[i]["last_name"] = last_name

	book_list = sorted(book_list, key=itemgetter('last_name'))
	return book_list

pprint(generatePickPath(14))


