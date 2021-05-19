import markovify, sys
data=""

fn=sys.argv[1]
#If you don't enter a filename as the command line flag, we fall back to our older method of asking the user via Python's input.
if fn=="": fn=input("Enter the file you want to search for.")
if fn=="": sys.exit("ERROR blank field")
with open(fn) as f:
	text=f.read()
	f.close()
for x in range(10):
	text_model = markovify.Text(text)
	tempstring=text_model.make_sentence(tries=50)
	print(tempstring)
	if tempstring!=None: data+=tempstring+"\r\n"
	input()
#Write to our saves file.
f=open("savedStrings.txt", "a")
f.write(data)
f.close()
print(str(len(data))+" bytes of new text have been written to the saved strings file.")
