import torch
import argparse
from pathlib import Path

# Import the CharRNN class definition from the training script
from train import CharRNN

def load_model_and_vocab(model_path: str, input_file: str) -> tuple[CharRNN, dict[str, int], dict[int, str]]:
    # Load vocabulary
    text = Path(input_file).read_text(encoding='utf-8') 
    chars = sorted(list(set(text)))
    char_to_idx = {ch: i for i, ch in enumerate(chars)}
    idx_to_char = {i: ch for i, ch in enumerate(chars)}
    
    # Initialize model with default hyperparameters
    model = CharRNN(len(chars))
    
    # Load trained weights
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    
    return model, char_to_idx, idx_to_char

def generate_text(model: CharRNN, prime_str: str, char_to_idx: dict[str, int], 
                 idx_to_char: dict[int, str], predict_len: int = 1000, 
                 temperature: float = 0.8) -> str:
  model.eval()
  device = next(model.parameters()).device
  
  chars = [ch for ch in prime_str]
  h, c = model.init_hidden(1, device)
  
  for ch in prime_str:
    char_index = torch.tensor([[char_to_idx[ch]]], device=device)
    _, (h, c) = model(char_index, (h, c))
  
  inp = char_index
  
  for p in range(predict_len):
    output, (h, c) = model(inp, (h, c))
    
    output_dist = output.data.view(-1).div(temperature).exp()
    top_char = torch.multinomial(output_dist, 1)[0]
    predicted_char = idx_to_char[top_char.item()]
    chars.append(predicted_char)
    
    inp = torch.tensor([[top_char]], device=device)
  
  return ''.join(chars)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--model_path', type=str, default='char_rnn.pth',
                      help='Path to trained model checkpoint')
  parser.add_argument('--input_file', type=str, required=True,
                      help='Path to original input text file used for training')
  parser.add_argument('--prime_str', type=str, default='The ',
                      help='Initial string to start generation with')
  parser.add_argument('--predict_len', type=int, default=1000,
                      help='Number of characters to generate')
  parser.add_argument('--temperature', type=float, default=0.8,
                      help='Temperature for sampling (higher is more random)')
  args = parser.parse_args()

  # Load model and generate text
  model, char_to_idx, idx_to_char = load_model_and_vocab(
    args.model_path, args.input_file
  )
  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  model.to(device)

  print(f"Loaded model from {args.model_path}")
  print(f"Generating {args.predict_len} characters with prime string: '{args.prime_str}'")
  print(f"Using temperature: {args.temperature}")
  print(f"Using device: {device}")

  generated_text = generate_text(
    model, args.prime_str, char_to_idx, idx_to_char, args.predict_len, args.temperature
  )

  print("\nGenerated text:")
  print("=" * 80)
  print(generated_text)
  print("=" * 80)