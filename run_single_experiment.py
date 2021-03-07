"""
Script to run the stimulus experiment for fNIRS with HEGDuino

How this works:
- Every couple of seconds, a word will be shown - when it is, it flashes on the screen for a predetermined number of seconds
- After the word is shown, then an X replaces the word in the text for an unspecified (8 - 20 seconds) amount of time
- Rinse and repeat for several words until the end of the experiment
"""

from psychopy import visual, core
from stimulus_experiments import *

if __name__ == '__main__':
    # Parameters
    word = "look"
    seed = 40
    stimmy = SingleStimulusExperiment(word, seed)
    stimmy.run_test()
    
