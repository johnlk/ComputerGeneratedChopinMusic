import torch
import torch.nn as nn
import numpy as np
from pathlib import Path
import argparse

class CharRNN(nn.Module):
  def __init__(self, vocab_size, embedding_dim=128, n_hidden=256, n_layers=2, dropout=0.2):
    super().__init__()
    self.n_layers = n_layers
    self.n_hidden = n_hidden
    
    self.embedding = nn.Embedding(vocab_size, embedding_dim)
    self.lstm = nn.LSTM(embedding_dim, n_hidden, n_layers, dropout=dropout, batch_first=True)
    self.dropout = nn.Dropout(dropout)
    self.fc = nn.Linear(n_hidden, vocab_size)
  
  def forward(self, x: torch.Tensor, hidden: tuple[torch.Tensor, torch.Tensor]) -> tuple[torch.Tensor, tuple[torch.Tensor, torch.Tensor]]:
    embed = self.dropout(self.embedding(x))
    lstm_out, hidden = self.lstm(embed, hidden)
    out = self.fc(lstm_out.reshape(lstm_out.size(0)*lstm_out.size(1), lstm_out.size(2)))
    return out, hidden
  
  def init_hidden(self, batch_size: int, device: torch.device) -> tuple[torch.Tensor, torch.Tensor]:
    return (torch.zeros(self.n_layers, batch_size, self.n_hidden, device=device),
            torch.zeros(self.n_layers, batch_size, self.n_hidden, device=device))

def load_text(file_path: str) -> tuple[str, list[str], dict[str, int], dict[int, str]]:
  text = Path(file_path).read_text(encoding='utf-8') 
  chars = sorted(list(set(text)))
  char_to_idx = {ch: i for i, ch in enumerate(chars)}
  idx_to_char = {i: ch for i, ch in enumerate(chars)}
  return text, chars, char_to_idx, idx_to_char

def get_batches(text: str, char_to_idx: dict[str, int], batch_size: int, seq_length: int, device: torch.device) -> tuple[torch.Tensor, torch.Tensor]:
  encoded = np.array([char_to_idx[ch] for ch in text])
  char_per_batch = batch_size * seq_length
  n_batches = len(encoded)//char_per_batch
  encoded = encoded[:n_batches*char_per_batch]
  encoded = encoded.reshape((batch_size, -1))

  dataset = torch.from_numpy(encoded).long().to(device)
  x = dataset[:, :-1]
  y = dataset[:, 1:]
  return x, y

def train(model: CharRNN, data: dict, optimizer: torch.optim.Optimizer, criterion: nn.Module, batch_size: int, seq_length: int, device: torch.device) -> float:
  model.train()
  x, y = get_batches(data['text'], data['char_to_idx'], batch_size, seq_length, device)
  hidden = model.init_hidden(batch_size, device)
  
  total_loss = 0
  for i in range(0, x.size(1)-seq_length, seq_length):
    inputs = x[:, i:i+seq_length]
    targets = y[:, i:i+seq_length].reshape(-1)
    
    hidden = tuple([h.detach_() for h in hidden])
    
    model.zero_grad() 
    
    output, hidden = model(inputs, hidden)
    
    loss = criterion(output, targets)
    loss.backward()
    
    nn.utils.clip_grad_norm_(model.parameters(), 5)   
    
    optimizer.step()
    total_loss += loss.item()
  
  return total_loss / (x.size(1)//seq_length)

def generate(model: CharRNN, prime_str: str, predict_len: int, temperature: float, data: dict, device: torch.device) -> str:
  model.eval() 
  
  chars = [ch for ch in prime_str]
  h, c = model.init_hidden(1, device) 
  
  for ch in prime_str:
    char_index = torch.tensor([[data['char_to_idx'][ch]]], device=device)
    _, (h, c) = model(char_index, (h, c))

  inp = char_index

  for p in range(predict_len): 
    output, (h, c) = model(inp, (h, c))
    
    output_dist = output.data.view(-1).div(temperature).exp()
    top_char = torch.multinomial(output_dist, 1)[0]
    predicted_char = data['idx_to_char'][top_char.item()]
    chars.append(predicted_char)
    
    inp = torch.tensor([[top_char]], device=device)

  return ''.join(chars)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--input_file', type=str, required=True)
  parser.add_argument('--n_epochs', type=int, default=20) 
  parser.add_argument('--batch_size', type=int, default=128)
  parser.add_argument('--seq_len', type=int, default=100)
  parser.add_argument('--embedding_dim', type=int, default=128)
  parser.add_argument('--n_hidden', type=int, default=256)
  parser.add_argument('--n_layers', type=int, default=2)
  parser.add_argument('--dropout', type=float, default=0.2)
  parser.add_argument('--lr', type=float, default=0.002)
  args = parser.parse_args()

  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  print(f'Using device: {device}')

  text, chars, char_to_idx, idx_to_char = load_text(args.input_file)
  data = {
    'text': text,
    'chars': chars, 
    'char_to_idx': char_to_idx,
    'idx_to_char': idx_to_char
  }
  print(f'Corpus length: {len(text):,}')
  print(f'Unique chars: {len(chars):,}')

  model = CharRNN(len(chars), args.embedding_dim, args.n_hidden, args.n_layers, args.dropout).to(device)
  optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
  criterion = nn.CrossEntropyLoss()

  for epoch in range(args.n_epochs):
    loss = train(model, data, optimizer, criterion, args.batch_size, args.seq_len, device)
    print(f'Epoch {epoch+1}/{args.n_epochs}, Loss: {loss:.4f}')
    
    if (epoch+1) % 5 == 0:
      temperature = 0.8
      print(f'\nSample text at temperature {temperature}:\n{generate(model, "The ", 500, temperature, data, device)}\n')
      
      temperature = 0.5 
      print(f'\nSample text at temperature {temperature}:\n{generate(model, "The ", 500, temperature, data, device)}\n')

  torch.save(model.state_dict(), 'char_rnn.pth')
  print('Model saved to char_rnn.pth')