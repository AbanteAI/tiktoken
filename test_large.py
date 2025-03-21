import tiktoken

def test_large_string():
    print("Testing with 1 million 'X' characters...")
    text = "X" * 1000000
    encoder = tiktoken.get_encoding("cl100k_base")
    
    try:
        tokens = encoder.encode(text)
        print(f"Successfully encoded to {len(tokens)} tokens")
        print(f"Character-to-token ratio: {len(text) / len(tokens):.2f}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

test_large_string()
