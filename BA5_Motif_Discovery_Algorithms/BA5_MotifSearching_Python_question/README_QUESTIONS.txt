This data is the result if a real experiment where Oct4 matching motifs were identified using ChIP-seq.  
A suitable set of sequences were identified that can act as background (non-motif containing)
Oct4 is known to bind to sequences that match the consensus- ATGCAAAT

So the idea is that we use a scanning window across the two sets of sequences to identify each k-mer- here each 8mer
Then we use a dictionary (python hash container) to count the occurrence of each k-mer.
Then we normalise the counts so they are expressed as a percent of total seqs- this is because background
has more sequence than foreground.

So we are using background counts as a simple empirical measure of the chance of encountering a given sequence without enrichment.
[We could use s simple statistic such as the hypergeometric distribution to give a p-value.]

Load the code file in a text editor eg Notepad++ and replace all the ??? bits with code.
We will look in detail at the answer before you are asked to try to repair the ??? comments.

Once you have got the code running then add headers, print useful comments from the code.
Use the time package to give some timings of the code

import time
t1= time.time() #UTC time in seconds
#do something
t2 = time.time()
elapsed = t2-t1 #etc

Make sure you understand the full code!

Then look at the output files and determine if the output is as expected.

What does the experiment show and what are the limitations of the approach?

No Pycharm this week so you should edit the code in Notepad++
Code can be run by simply opening a command line and typing

python simplemotif_v1.1.py  

Or similar!!
