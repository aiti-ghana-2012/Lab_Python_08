"""
Little tool for playing around with regexs
"""

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

	def disable(self):
		self.HEADER = ''
		self.OKBLUE = ''
		self.OKGREEN = ''
		self.WARNING = ''
		self.FAIL = ''
		self.ENDC = ''

def error(message):
	return bcolors.FAIL + "ERROR: " + message + bcolors.ENDC

def header(message):
	return bcolors.HEADER + message + bcolors.ENDC
	
def blue(message):
	return bcolors.OKBLUE + message + bcolors.ENDC
	
def orange(message):
	return bcolors.WARNING + message + bcolors.ENDC

def ok(message=''):
	return bcolors.OKGREEN + "OK: " + message + bcolors.ENDC


print header("=" * 50)
print blue("Interactive Regex experimentation")
print blue("press Ctrl-C to bring up the menu")

print


import sys
import re

the_regex = None
	
def set_regex():
	global the_regex
	
	print header("-"*50)
	regex_string = raw_input(orange("Enter the regex to test: "))
	
	try:
		the_regex = re.compile(regex_string)
	except Exception as e:
		print error("Invliad Regex!\n" + str(e))
		set_regex()
		
	loop()
	
def loop():
	if the_regex is None:
		set_regex()
	
	while True:
		test = raw_input(orange("The regex is '%s'. Enter string to test >> " % the_regex.pattern))
		
		match = the_regex.search(test)
		
		if match:
			print ok("Match!")
			print blue("\tMatched:")
			print "\t\t'%s'" % match.group(0)
			if match.groups():
				print blue("\tGroups:")
				index = 1
				for val in match.groups():
					print "\t\t%s:\t'%s'" % (header(str(index)),repr(val))
					index += 1
			if match.groupdict():
				print blue("\tNamed Groups:")
				for key,val in match.groupdict():
					print "\t\t%s:\t'%s'" % (header(key),val)
		else:
			print error("No Match!")
			
def menu():
	print
	print header("-" * 50)
	print blue("Menu:")
	
	options = {
				"q" : ("to quit",quit),
				"n" : ("to pick a new regex", main)
				}
				
	
	def choices():	
		for k,v in options.items():
			print blue("Type '%s' %s" % (k,v[0]))
	
	choices()
	
	response = None
	while response not in options:
		if response is not None:
			print error("Invalid option.")
			choices()
		response = raw_input(orange("> "))
	
	options[response][1]()
	
	
def quit():
	print header("Bye Bye")
	sys.exit(0)
	

def main():
	try:
		set_regex()
	except KeyboardInterrupt:
		menu()


		

if __name__ == "__main__":
	main()


		
			
		

		
		
	
	
	
