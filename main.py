import markovify, sys, os, traceback
data=""

fn=sys.argv[1]
#If you don't enter a filename as the command line flag, we fall back to our older method of asking the user via Python's input.
if fn=="": fn=input("Enter the file you want to search for.")
if fn=="": sys.exit("ERROR blank field")
if os.path.isfile( fn)==False:
	print("Error! File "+fn+" doesn't exist.")
	sys.exit()
with open(fn) as f:
	text=f.read()
	f.close()
for x in range(10):
	text_model = markovify.Text(text)
	try:
		tempstring=text_model.make_sentence(tries=50)
	except: sys.exit("There was an error with the file you've selected. Please try again or, if the problem persists, open an issue on GitHub.")
	print(tempstring)
	if tempstring!=None: data+=tempstring+"\r\n"
	print("Press return to generate more output.")
	input()
#Write to our saves file.
f=open("savedStrings.txt", "a")
f.write(data)
f.close()
print(str(len(data))+" bytes of new text have been written to the saved strings file.")
