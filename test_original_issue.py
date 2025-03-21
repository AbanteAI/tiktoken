import tiktoken
import time

print("Testing the original issue case: 1 million repeated X's...")

# Recreate the exact case from the issue
test_string = "X" * 1000000
encoder = tiktoken.get_encoding("cl100k_base")

start_time = time.time()
try:
    print("Starting encoding...")
    tokens = encoder.encode(test_string)
    end_time = time.time()
    print(f"Success! Encoded 1M repeated X's to {len(tokens)} tokens in {end_time - start_time:.2f} seconds")
except Exception as e:
    print(f"Error: {e}")

print("Test completed!")
