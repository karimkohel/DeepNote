# DeepNote
A collection of all findings during my research for auto-regressive generative model for music generation

## Data
Being a professional DJ proved convenient while gathering the data required for learning.

Data will consist mainly of techno music segments that has no quite gaps between notes as to not confuse the network.


### NOTES
 - starting with a sanity test we acquired 2 techno tracks from my personal techno library 
 - training data has to be wave files only, [reference paper]
 - we chose techno music to be cutted into around 30 sec segments with similar structure for dribbling beats
 - using free mp3 cutter the music where cut into the specific segments and turned into wav format
 - working with ibab implimentation was hard as tf1 is not working unless you change the requirements.txt
 - installing gpu drivers was a nightmare
 - changing the code that uses tensorflow to referenece tensorflow version 1 compatability