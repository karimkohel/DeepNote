# DeepNote
A collection of all findings during my research for auto-regressive generative model for music generation

## Data
Being a professional DJ proved convenient while gathering the data required for learning.
Data will consist mainly of techno music segments that has no quite gaps between notes as to not confuse the network.

The data chosen for training and generation is techno music as athe initial thought was that the repetetivness of the techno genre in dribbling has a predictable nature that would help the network in generating said genre.
Data was segmented into varying length files of musical segments in wav format.


### Running the network for now
 - Training:
 `python train.py --data_dir=techno --logdir=logging/train/2021-12-26T15-27-51 --checkpoint_every=1000`
 - Generating
 `python generate.py --wav_out_path=generated.wav --logdir=logging --samples 32000 logging/train/2021-12-23T02-22-52/model.ckpt-15`


### Dependencies 
 - tensorflow-gpu==1.15.0
 - librosa==0.5
 - cudatoolkit==10.0.130
 - cudnn==7.6.5

### NOTES
 - starting with a sanity test we acquired 2 techno tracks from my personal techno library 
 - training data has to be wave files only, [reference paper]
 - we chose techno music to be cutted into around 30 sec segments with similar structure for dribbling beats
 - using free mp3 cutter the music where cut into the specific segments and turned into wav format
 - working with ibab implimentation was hard as tf1 is not working unless you change the requirements.txt
 - installing gpu drivers was a nightmare
 - changing the code that uses tensorflow to referenece tensorflow version 1 compatability
 - collecting data: 1 GB of data mark
   - music files were ripped off of youtube as mp3 files 
   - preprocessed on audacity to trim the wanted segments from audio files and convert files to wav
   - each music file can be used to collect up to 3 or 4 music segments as different wav files 
