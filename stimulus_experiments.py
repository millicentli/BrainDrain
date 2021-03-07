"""
File to hold the class for stimulus experiments, with a few utility functions.
"""

from psychopy import visual, core
import re
import random

class MultiStimulusExperiment:
    """
    Class to hold the stimulus experiment for multiple words.
    """
    
    def __init__(self, text, seed, lower_rand=8.0, upper_rand=20.0, limit=10, start_time=5.0, end_time=5.0, show_time=4.0):
        """
        @param text: the text to use for the experiment
        @param seed: the seed to use for the timing so that the randomized timings are all consistent 
                     (in the case of repeating the experiment multiple times)
        @param limit: numerical limit for the number of words that can show up in a single experiment
        @param start_time: the time to wait at the very beginning of the experiment
        @param end_time: the time to wait at the very end of the experiment
        @param show_time: the time that each word is shown
        """
        self.seed = seed
        self.lower_rand=lower_rand
        self.upper_rand=upper_rand
        self.limit = limit
        self.start_time = start_time
        self.end_time = end_time
        self.show_time = show_time
        self.processed_text = self.preprocess_text(text)

    def preprocess_text(self, text):
        """
        Preprocesses any extraneous text, especially any special characters that we don't want

        @param text: the text used for the experiment
        """

        cleaned_text = re.sub(r'([^\s\w]|_)+', '', text)
        return cleaned_text.split()[:self.limit]

    def run_test(self):
        """
        Invoke to run the experiment
        """

        random.seed(self.seed)
        win = visual.Window(fullscr=True)
        message = visual.TextStim(win, text='X')
        message.autoDraw = True
        core.wait(self.start_time)
        for word in self.processed_text:
            message.text = word
            win.flip()
            core.wait(self.show_time)
            
            message.text = 'X'
            win.flip()
            core.wait(random.randint(self.lower_rand, self.upper_rand + 1))

        core.wait(self.end_time)



class SingleStimulusExperiment:
    """
    Class to hold the stimulus experiment for just a single word.
    """
    
    def __init__(self, word, seed, lower_rand=8.0, upper_rand=20.0, limit=10, start_time=5.0, end_time=5.0, show_time=4.0, num_iters=10):
        """
        @param text: the text to use for the experiment
        @param seed: the seed to use for the timing so that the randomized timings are all consistent 
                     (in the case of repeating the experiment multiple times)
        @param limit: numerical limit for the number of words that can show up in a single experiment
        @param start_time: the time to wait at the very beginning of the experiment
        @param end_time: the time to wait at the very end of the experiment
        @param show_time: the time that each word is shown
        """
        self.seed = seed
        self.lower_rand=lower_rand
        self.upper_rand=upper_rand
        self.limit = limit
        self.start_time = start_time
        self.end_time = end_time
        self.show_time = show_time
        self.num_iters = num_iters
        self.processed_word = word.strip()

    def run_test(self):
        """
        Invoke to run the experiment
        """

        random.seed(self.seed)
        win = visual.Window(fullscr=True)
        message = visual.TextStim(win, text='X')
        message.autoDraw = True
        core.wait(self.start_time)
        for it in range(self.num_iters):
            message.text = self.processed_word
            win.flip()
            core.wait(self.show_time)

            message.text = 'X'
            win.flip()
            core.wait(random.randint(self.lower_rand, self.upper_rand + 1))

        core.wait(self.end_time)

