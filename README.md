## Computer Generated Chopin Music

The goal of this personal project is to replicate the music of classical pianist Chopin using a unique approach that differs from traditional methods. While most approaches to replicating music utilize audio files and algorithms like Convolutional Neural Networks (CNNs), this project takes a distinctive path by converting audio files to text-based formats. By leveraging the power of Recurrent Neural Networks (RNNs), the text representation is used to generate music, which is then converted back into an audio file.

## Overview
The project utilizes an existing open-source LSTM algorithm called char-rnn, which can be accessed [here](https://github.com/karpathy/char-rnn). This machine learning algorithm is designed to work with text files for training and generating outputs. To adapt it for generating music, MIDI files of Chopin's compositions were used. The MIDI files are located in the `midiFiles/` directory and were converted into plain ASCII text files found in `midiTextFiles/`. Due to the large size of the concatenated ASCII files, a condensing process was implemented, resulting in a file named `input.txt`, which was then used as input for the LSTM algorithm.

## Output
After training the LSTM algorithm on the `input.txt` file for approximately 6 hours, three separate music files were generated as output. These files were in text format and needed to be expanded and converted back into MIDI format. The code for the condensing and un-condensing process can be found in the `fileShrinker/` directory.

The three generated music files are as follows:
- `output_temp-0.4.midi`: This file was created using a temperature parameter of 0.4 during the sampling process.
- `output_temp-0.8.midi`: This file was generated with a temperature parameter of 0.8.
- `output_temp-1.0.midi`: This file was generated with a temperature parameter of 1.0.

These MIDI files can be played using various music players, including GarageBand. The temperature parameter determines the aggressiveness of the machine's predictions during the sampling process. A higher temperature value, such as 1.0, is more likely to produce unique and interesting results, but it may also contain more mistakes or errors.

## Future Work
The initial results obtained from just 6 hours of training are promising, and further improvements can be expected with extended training periods. The project's next step involves training the algorithm for a longer duration, approximately 30 hours, with the aim of generating more pleasing and refined musical compositions.