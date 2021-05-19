# MarkovifyTest
Simple markov testing program. Sotf of documented below, but more changes will come to make this structured and include a running section and such things.

## Notes:
Use pip install -r requirements.txt inside this dir to get all of those.

run.bat runs this. To generate another bit of text, press enter.

To go into the data folder and grab a file, use something like:
```
"data/sc.txt"
```

Now you can use the command line flag/switch thingy. You can use something like:
```
python main.py data/constitution.txt
```
That will bypass the older method of the asking you for input after exicution thing, using data/constitution.txt as its text file to search for words to markov.

run.bat will probably have this as another demonstration of how it works; will use one of the files in the data folder as expected.

It will save all things generated to that saved strings file, asooming that it is not trying to save a None object and you've gone through all 10 generations. Also it will print out just how many bytes have been written to said log. And no, I am not going to convert this as I am far too lazy.

The generator will now try to generate something 40 times instead of the 10 it used to, so you should have less bad things such as that.

Files here are random files from around.

Good enjoyment.
