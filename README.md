## Computer Generated Chopin Music

The goal of this project was to feed a computer a bunch of musical works by classical pianist Chopin, and see if this music
could be replicated by a machine learning algorithm.

## Overview
This project uses an already created and open source machine learning algorithm called an LSTM. The code can be found
[here] (https://github.com/karpathy/char-rnn)

The Long Short Term Memory Machine Learning algorithm uses text files to train and later outputs text files. I was able 
to use music files the were extension ".midi". All chopin midi files are in `midiFiles/`. These .midi files I was next
able to convert to plain ascii text files found in `midiText/`.All my ascii files congregated together were very large
and needed to be condensed. Once condensed to a size of around 4 MB I was able to give it to the Machine Learning algoirithm.
This file given to the LSTM is `input.txt`.

