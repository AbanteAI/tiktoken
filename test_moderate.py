import tiktoken

print("Testing with a moderately long repeated string...")
moderate_string = "X" * 100000  # 100k instead of 1M
encoder = tiktoken.get_encoding("cl100k_base")
token_count = len(encoder.encode(moderate_string))
print(f"Token count: {token_count}")
print("Test completed successfully!")
