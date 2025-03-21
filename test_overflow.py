import tiktoken

print("Testing with a very long repeated string...")
bad_string = "X" * 1000000  # Exactly what was in the issue
encoder = tiktoken.get_encoding("cl100k_base")
token_count = len(encoder.encode(bad_string))
print(f"Token count: {token_count}")

# Verify decoding works
sample = encoder.encode(bad_string[:1000])
full = encoder.encode(bad_string)
print(f"Sample token count: {len(sample)}")
print(f"Full token count: {token_count}")

# Verify numpy encoding
try:
    import numpy as np
    tokens_np = encoder.encode_to_numpy(bad_string)
    print(f"Numpy token count: {len(tokens_np)}")
except ImportError:
    print("Numpy not available")

print("Test completed successfully!")
