## Computer Generated Chopin Music
The goal of this project was to feed a computer a bunch of musical works by classical pianist Chopin, and see if this music
could be replicated by a machine learning algorithm.

## Overview
This project uses an already created and open source machine learning algorithm called an LSTM. The code can be found
[here](https://github.com/karpathy/char-rnn).

The Long Short Term Memory Machine Learning algorithm uses text files to train and later outputs text files. I was able 
to use music files with extension ".mid". All Chopin midi files are in `midiFiles/`. These midi files I was next
able to convert to plain ascii text files found in `midiTextFiles/`. All my ascii files congregated together were very large
and needed to be condensed. Once condensed to a size of around 4 MB I was able to give it to the Machine Learning algorithm.
The file given to the LSTM was `input.txt`.

## Output
After letting the computer learn from `input.txt` for around 6 hours I output three separate music files. These were text
files and needed to be uncondensed and converted back into midi format. Code for condensing and un-condensing is found in
the `fileShrinker/` directory. 

The three files outputted are `output_temp-0.4.midi`, `output_temp-0.8.midi`, and `output_temp-1.0.midi` which can be played
by most music players including garage band. The "temp-X" naming convention is denoting the files' temperature parameters when 
sampling. Temperature is how aggressive the machine predictions will be and ranges from 0-1.0. An output file with temperature
1.0 is a lot more likely to be unique and interesting while also being equally more likely to have more mistakes or errors. 

## Future Work
Having a decent output from only 6 hours of training has me hopeful for what 30 hours of training could produce. I will later
push files generated from a lot more training with hopefully slightly more pleasing musical results.
