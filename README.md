# Computer Generated Chopin Music

This project uses deep learning to generate classical piano music in the style of Chopin through a novel text-based approach. Unlike traditional music generation methods that process raw audio or MIDI files directly, this project converts MIDI files into text representations that can be processed by Recurrent Neural Networks (RNNs).

## Technical Overview

### Architecture
The project leverages char-rnn, an LSTM-based character-level language model implementation by Andrej Karpathy. The model architecture consists of:
- Multi-layer LSTM network
- Configurable hidden layer size and number of layers
- Dropout regularization for preventing overfitting
- Mini-batch training with CUDA GPU support

### Data Processing Pipeline
1. **MIDI Collection**: Source MIDI files are stored in `data/midi/`
2. **Text Conversion**: MIDI files are converted to ASCII format using conversion tools in `src/conversion/`
3. **Data Preprocessing**: ASCII files are stored in `data/ascii/` and processed into training data
4. **Training**: The LSTM model is trained on the text representation for ~6 hours
5. **Generation**: New music is sampled from the model at different temperature settings

### MIDI-Text Format
The ASCII representation captures MIDI events with precise timing and musical parameters:

### Model Parameters
- Training duration: 6 hours initial run
- Temperature settings tested: 0.4, 0.8, 1.0
- Higher temperatures (e.g. 1.0) produce more creative but potentially error-prone compositions
- Lower temperatures (e.g. 0.4) generate more conservative, structured pieces

## Generated Outputs
Three MIDI files were generated with different temperature parameters:
- `output/generated/temp-0.4/`: Conservative generation
- `output/generated/temp-0.8/`: Balanced creativity/structure
- `output/generated/temp-1.0/`: Most experimental generation

The MIDI files can be played using standard music software like GarageBand or this [web player](https://midiplayer.ehubsoft.net/). The temperature parameter controls sampling randomness during generation - higher values produce more diverse but potentially less coherent music.

## Technical Roadmap
1. Extended Training: Increase training duration to 30+ hours
2. Architecture Tuning:
   - Experiment with larger hidden layer sizes
   - Test different dropout rates
   - Try additional LSTM layers
3. Data Augmentation: Add more Chopin compositions to training set
4. Evaluation Metrics: Implement quantitative measures of musical quality

## Implementation Details
The core LSTM implementation is based on the char-rnn architecture, which includes:
- Batch processing for efficient training
- CUDA optimization for GPU acceleration
- Configurable sequence length for capturing musical patterns
- Checkpoint saving/loading for iterative training

For detailed information about the char-rnn implementation, see the [original repository](https://github.com/karpathy/char-rnn).