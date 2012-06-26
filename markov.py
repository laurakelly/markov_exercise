import os, random

def process_file(filename):
	f = open(filename)
	output = {}

	line = f.readline()
	f.close()
	split_line = line.split()

	for index, word in enumerate(split_line):
		if split_line[index] == split_line[-2]:
			break
		else:
			next = split_line[index + 1]
			output[(word, next)] = [split_line[index + 2]]
	return output	

def shift(tuple, whatever):
	newple = (tuple[1], whatever)
	return newple

def build_sentence(d):
	prefix = random.choice(d.keys())
	suffix = d[prefix]
	string = prefix[0] + " " + prefix[1] + " " + suffix[0]

	print string
	return string

def main():
	#pass
	#process_file("sample2.txt")
	sample_dict = {"this is":"our", "sample":"string"}
	build_sentence(sample_dict)

if __name__ == "__main__": 
	main() 
