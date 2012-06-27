import os, random

def process_file(filename):
	f = open(filename)
	output = {}

	lines = f.read()
	f.close()
	split_line = lines.split()

	for index in range(len(split_line)-2):
		prefix = split_line[index], split_line[index+1]
		suffix = split_line[index+2]
		if output.get(prefix):
			output[prefix].append(suffix)
		else:
			output[prefix] = [suffix]

	return output

def shift(tuple, whatever):
	newple = (tuple[1], whatever)
	return newple

def build_sentence(d):
	if len(d.keys()) == 0:
		return ""

	prefix = random.choice(d.keys())
	suffix = d[prefix]
	string = prefix[0] + " " + prefix[1] + " " + suffix[0]
	terminators = "?!."
	while string[-1] not in terminators:
		prefix = (prefix[1], suffix[0])
		suffix = d[prefix]
		string += " " + random.choice(suffix)
	return string.capitalize()

def build_paragraph(d, integer):
	paragraph = ""
	for i in range(integer):
		paragraph += build_sentence(d) + " "
	return paragraph

def build_tweet(dict):
	tweet = ""
	sentence = build_sentence(dict)
	while len(sentence) > 140:
		sentence = build_sentence(dict)
	while len(sentence) < 140:
		new_sentence = build_sentence(dict)
		if len(sentence + " " + new_sentence) > 140:
			return sentence
		else:
			sentence += new_sentence

def main():
	emma = process_file("emma.txt")
	print build_tweet(emma)

if __name__ == "__main__": 
	main() 
