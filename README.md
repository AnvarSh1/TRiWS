# TRiWS
Tandem Repeats in Weighted Sequences

Below are extracts from my MSc Individual Project at King's College London 


"Tandem repeat is a consecutively repeated string which is not empty. For e.g. www, 0101, and

TAGCTAGC. Any string containing such repeated sequences as a substring is called repetition-containing;

otherwise, a string is repetition-free (Barton et al., 2014). A tandem repeat in this case, is a string of the

form , where  is a non-empty string (Barton et al., 2014). Considering some string x, questions

regarding tandem repeats in x may arise. For e.g. if x contains tandem repeats and a possible number of

such repetitions, it has been demonstrated by Crochemore (1981) that there exists a chance of having O

(n log n) maximal repetitions within a string of length n. Eventually, Kolpakov and Kucherov (1999) devised

an O (n) time algorithm to calculate the compact representation for all such repetitions denoted by runs.

Usually, these algorithms work on regular strings. We will currently focus on locating tandem repeats in

weighted sequences. The first step is to understand what a weighted sequence is. A weighted sequence

may be defined as a type of string that allows characters of a given alphabet to occur at a particular

position with respective probability, unlike fixed single characters in a normal string. This model allows us,

among other things, to use the idea of equivalence classes in weighted sequences, introduced by Zhang,

Guo and Iliopoulos (2012) to calculate tandem repeats of all possible lengths."


Modules Overview.

"To make both implementation and further application more convenient, solution is divided into separate modules. Such model allows to use separate functions without bulking main code, develop and improve each one of them separately while avoiding interference with other modules. Python (version 3.5.1) was used during development; usage of external libraries was limited where possible, to create completely independent code.
Input model
The very first step in our calculations is input of the weighted string. Considering the mixture of different data types in one sequence, it is not always possible to process input string "as is"; consistent weighted string model is needed to start calculations.
For this task module rwtstr.py is created, which reads a string directly from a file and outputs a sequence with separated nested values.
Simple template was considered, according to examples from previous chapters, with addition of delimiter:
Each position i in sequence x is separated from next by “;” symbol, making it possible to process each concerning different types of data. Taking into account that positions that show only letters are having occurrence probability equal to 1, numbers and missing syntax will be added
After syntax corrections are made, next step is present each element as an object that we can address. We use Python’s built-in eval() function for this purpose, which evaluates a given string as pure Python expression.
Above manipulations result in list of lists of tuples, where each nested list is position x[i] of the string, and each tuple is a letter with its given occurrence probability. While first reason for using tuples as (letter, occurrence) pairs resulted from syntax itself, it was decided to use this model further. Main reason is tuples are, unlike lists, immutable, which gives us additional safety over accidental modifications.
At this point, we successfully read our sequence and made it available for further manipulations. Next, we implement second module naivestrcr.py, which allows us to find the maximal repetition in a given string. Algorithm uses the idea of naïve implementation of Crochemore’s algorithm. At the current moment, naivestrcr.py is the only module that uses additional library – we import Python’s re library, which allows us to use regular expressions within our code.

After regular string is passed to internal function NaiveCr(), two nested loops compare substring, starting from size of 1. With additional use of regular expressions, it is easier to compare the substring with the whole sequence. After maximum comparison is made, function will print maximal repeated substring.
Main module
Now, as all supplementary modules are implemented, we can move to the main file. Algorithm implemented here is the short variant of the algorithm developed by Barton, Iliopoulos and Pissis (2014).
The difference between approaches is, patternalgo.py works nearly as sub-problem solver.
After successful filtering colouring stages, algorithm starts to assemble extended factor from each given black position and appends each factor to the list of extended factor.
Next, we simply pass this list, item by item, to naivestrcr.py, which will compute maximal repeating substring for given factor."
