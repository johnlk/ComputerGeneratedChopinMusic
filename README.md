# Computer Generated Chopin Music

This project uses deep learning to generate classical piano music in the style of Chopin through a novel text-based approach. This project converts MIDI files into text representations that can be easily processed by RNNs.

Best output found here: `output/2024-pytorch-rnn/temp-0.8/tmp.mid`

## Project History & Evolution

### 2017 Version
The project originally used Andrej Karpathy's char-rnn implementation for generating music. This version produced interesting results (preserved in `output/2017-karpathy-LSTM/`) but relied on external dependencies and older deep learning frameworks.

### 2024 Update
After 7 years, the project was modernized with a custom PyTorch-based implementation. The new version features:
- Simplified architecture using PyTorch's built-in LSTM modules
- More efficient training pipeline
- Better code organization and documentation
- Improved generation quality through modern deep learning practices

## Technical Overview

### Architecture
The current implementation uses a character-level RNN built with PyTorch, consisting of:
- Embedding layer for character encoding
- Multi-layer LSTM network
- Dropout regularization for preventing overfitting
- Linear output layer for character prediction
- Mini-batch training with CUDA GPU support

### Data Processing Pipeline
1. **MIDI Collection**: Source MIDI files are stored in `data/midi/`
2. **Text Conversion**: MIDI files are converted to ASCII format using conversion tools in `src/conversion/`
3. **Data Preprocessing**: ASCII files are stored in `data/ascii/` and processed into training data
4. **Training**: The PyTorch model is trained on the text representation
5. **Generation**: New music is sampled from the model at different temperature settings

### Model Parameters
- Training options:
  - Hidden layer size: 256 (configurable)
  - Number of LSTM layers: 2 (configurable)
  - Dropout rate: 0.2
  - Batch size: 128
  - Sequence length: 100
- Temperature settings tested: 0.4, 0.8, 1.0
  - Higher temperatures produce more creative but potentially error-prone compositions
  - Lower temperatures generate more conservative, structured pieces

## Generated Outputs
The project maintains both historical and current outputs:
- `output/2018-karpathy-LSTM/`: Original char-rnn generated pieces
- `output/2024-pytorch-rnn/`: New PyTorch model generations
  - `temp-0.4/`: Conservative generation
  - `temp-0.8/`: Balanced creativity/structure
  - `temp-1.0/`: Most experimental generation

The MIDI files can be played using standard music software like GarageBand or this [web player](https://midiplayer.ehubsoft.net/).

## Technical Roadmap
1. Extended Training: Increase training duration and dataset size
2. Architecture Tuning:
   - Experiment with larger hidden layer sizes
   - Test different dropout rates
   - Try additional LSTM layers
3. Data Augmentation: Add more Chopin compositions to training set
4. Evaluation Metrics: Implement quantitative measures of musical quality

## Implementation Details
The core implementation is in `src/model/`, featuring:
- `train.py`: Model definition and training logic
- `generate.py`: Text generation utilities
- Efficient batch processing
- CUDA optimization for GPU acceleration
- Configurable sequence length for capturing musical patterns
- Checkpoint saving/loading for iterative training

For detailed usage instructions and parameters, see the model documentation in `src/model/README.md`.