
### NOTE ###
I did not use the build frame from the website since I just found it after I finish my codes. 
I don't have enough time to transfer the codes to the frame. Sorry about that. 


### ENVIRONMENT ###
python 3 

Modules needed are all in requirements.txt; You can still run pip3 install -r requirements.txt
to install if you find some modules are not defined. 


### RUN ###
Run from command line: python3 ./runner.py lij007@eng.ucsd.edu <Running_times>

For example: python3 ./runner.py lij007@eng.ucsd.edu 100 Means run the game for 100 times 


### Algorithm ###

--------Process word frequency dictionary---------
Convert the word_frequency.txt file to a json file (processed_word_frequency.json).
The format of this json file is {length_of_word:{word: frequency}}

--------Gaming logic---------
How to find the correct parttern which should be filled at first?
1. If all pattern are in mystery, choose the shortest one. 
2. If some patterns have clue, choose the pattern with highest known rate (known rate = known number/unknown number). The rate should be a float. This will increate the successful rate. 

--------Choose letter--------
1. First get all candidates part with the same length. 
2. Filter all unsatisfied candidates by checking if the known part is the same. (eg: aaccb is not a candidate for __bbe)
3. Sort the satisfied candidates according to the word frequency to get a sorted_candidates. Then create a candidate letter list with the following standards:
   i) The word frequency is the most important order. 
   ii) Count the number of these candidate letters and create a reversed sorted list. 

   eg: {"hellc": 10000, "hallr":300.....}. The pattern is 'h_ll_'
   hellc has higher rank than hallr since this word appears more frequently. Which means hellc has higher wright. Then, the candidate letter is e, c, a, r. Count the candidate letter frequency for the whole dictionary. Create a new dictionray, the foramt is: {(candidate letter, the frequency of word which candidate letter appears): letter frequency}

   Then, we can get a new list of candidate letter: sort the dictionary with the priority[the frequency of word which candidate letter appears,letter frequency], order is reversed which means decreasing order. Finally return this list. 

  In the runner.py, get this list and choose the letter from left to right until find the correct one or dead. 

  Do the same thing until game end. 


  -------Some possible improvement-------
1. Can use regular expression rather than for loop. Avoid redundent codes and save time. 
2. Choose better word frequency dictionary. 
...










