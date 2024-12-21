# Character-Level Text Generation with PyTorch

A modern PyTorch implementation of character-level text generation using LSTM networks. This model learns to generate text one character at a time by training on any text file you provide. Originally developed for musical MIDI-to-text generation, but can be used for any character-level text generation task.

## Directory Structure
```
src/
└── model/
    ├── train.py      # Training script and model definition
    ├── generate.py   # Text generation script
    └── README.md     # This file
```

## Requirements

```bash
pip install torch numpy
```

## Model Architecture

The CharRNN model consists of:
- Character embedding layer
- Multi-layer LSTM
- Dropout for regularization
- Linear output layer
- Automatic GPU support via PyTorch

## Training a Model

1. Prepare your text file (e.g., `input.txt`)

2. Train the model:
```bash
python train.py --input_file path/to/your/input.txt
```

### Training Options
- `--n_hidden`: Size of hidden layers (default: 256)
- `--n_layers`: Number of LSTM layers (default: 2)
- `--batch_size`: Training batch size (default: 128)
- `--seq_length`: Sequence length for training (default: 100)
- `--n_epochs`: Number of training epochs (default: 20)
- `--temperature`: Sampling temperature (default: 0.8)
- `--embedding_dim`: Size of character embeddings (default: 128)
- `--dropout`: Dropout rate (default: 0.2)

The model will be saved as `char_rnn_model.pt` after training.

## Generating Text

To generate text using a trained model:

```bash
python generate.py --input_file path/to/your/input.txt --prime_str "Start with this text"
```

### Generation Options
- `--predict_len`: Number of characters to generate (default: 1000)
- `--temperature`: Controls randomness (default: 0.8)
  - Lower (0.2-0.5): More focused, consistent text
  - Higher (0.8-1.0): More creative, diverse text
- `--model_path`: Path to trained model (default: 'char_rnn_model.pt')
- `--prime_str`: Starting text for generation (default: 'The ')

## Performance Tips

1. **GPU Acceleration**
   - The model automatically uses CUDA if available
   - For CPU-only training, no configuration needed
   - Multi-GPU support via `DataParallel` if needed

2. **Memory Optimization**
   - Adjust batch_size based on available memory
   - Use gradient accumulation for larger effective batches
   - Monitor CUDA memory usage with `nvidia-smi`

3. **Training Time**
   - Depends on:
     - Dataset size
     - Number of epochs
     - Hidden layer size
     - Hardware (GPU/CPU)

4. **Quality Control**
   - Start with default parameters
   - Increase model size for more complex patterns
   - Adjust temperature based on generation needs
   - Use longer sequence lengths for better context

## Troubleshooting

1. **Memory Issues**
   - Reduce batch_size
   - Reduce n_hidden
   - Reduce seq_length
   - Enable gradient accumulation

2. **Poor Generation Quality**
   - Train for more epochs
   - Verify input text size (100KB minimum recommended)
   - Adjust temperature
   - Increase model size (n_hidden, n_layers)
   - Check for data preprocessing issues
