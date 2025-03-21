import tiktoken

# Create a smaller string that shouldn't trigger stack overflow
# but would be large enough to test our chunking mechanism
print("Testing with a small repeated string...")
small_string = "X" * 20000  # 20k repeated X's
encoder = tiktoken.get_encoding("cl100k_base")

# First encode normally to make sure it works
try:
    tokens = encoder.encode(small_string)
    print(f"Success! Encoded {len(small_string)} characters to {len(tokens)} tokens")
    
    # Then verify that our chunking mechanism works by forcing it to use the chunking code path
    # by temporarily modifying the CHUNK_SIZE to be very small
    original_func = encoder._core_bpe.encode
    
    def mock_encode(*args, **kwargs):
        # This will simulate a stack overflow by raising the exception
        raise RuntimeError("RuntimeError(StackOverflow)")
    
    # Replace the encode function with our mock
    encoder._core_bpe.encode = mock_encode
    
    # Now when we call encode, it should use our chunking mechanism
    chunked_tokens = encoder.encode(small_string)
    print(f"Success! Chunking mechanism encoded to {len(chunked_tokens)} tokens")
    
    # Verify the results are consistent
    if len(tokens) == len(chunked_tokens):
        print("Great! Both methods produced the same number of tokens")
    else:
        print(f"Warning: Different token counts: {len(tokens)} vs {len(chunked_tokens)}")
        
except Exception as e:
    print(f"Error: {e}")

print("Test completed!")
