import tiktoken
import time

print("Testing the Rust-level fix for stack overflow...")

# Test with increasing sizes to see where/if it breaks
for size in [1000, 10000, 100000]:
    print(f"\nTesting with {size} repeated chars...")
    test_string = "X" * size
    encoder = tiktoken.get_encoding("cl100k_base")
    
    start_time = time.time()
    try:
        tokens = encoder.encode(test_string)
        end_time = time.time()
        print(f"Success! Encoded to {len(tokens)} tokens in {end_time - start_time:.2f} seconds")
        
        # Verify decoding works too
        decoded = encoder.decode(tokens)
        if decoded == test_string:
            print("Decoding successful and matches original")
        else:
            print(f"Decoding failed: lengths match? {len(decoded) == len(test_string)}")
    except Exception as e:
        print(f"Error: {e}")

print("\nTests completed!")
