import time
import tiktoken

def test_repetitive_encoding(length):
    text = "X" * length
    encoder = tiktoken.get_encoding("cl100k_base")
    
    start_time = time.time()
    tokens = encoder.encode(text)
    end_time = time.time()
    
    print(f"Encoded {length} 'X's into {len(tokens)} tokens")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print(f"Tokens per second: {len(tokens) / (end_time - start_time):.2f}")

print("Testing with medium repetitive string (50,000 Xs)")
test_repetitive_encoding(50000)
