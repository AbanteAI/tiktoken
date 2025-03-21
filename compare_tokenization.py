import tiktoken

def test_with_repetitive_strings():
    """Test different sizes of repetitive strings and verify token counts match."""
    print("Testing tokenization equivalence:")
    
    for length in [1000, 10000, 50000, 100000]:
        text = "X" * length
        encoder = tiktoken.get_encoding("cl100k_base")
        tokens = encoder.encode(text)
        print(f"Length {length} -> {len(tokens)} tokens")
        
        # Check the ratio
        # Note: For most strings, the tokens should be about 1/8 the length
        # for a single repeated character because bytes are merged efficiently
        print(f"  Character-to-token ratio: {length / len(tokens):.2f}")
        
    # Also try with some mixed content
    text = "Hello world! " + ("X" * 10000) + " This is a test."
    tokens = encoder.encode(text)
    print(f"Mixed content (mostly repetitive): {len(tokens)} tokens")
    
    # Try with a more complex repetitive pattern
    text = ("ABC" * 10000) 
    tokens = encoder.encode(text)
    print(f"'ABC' repeated 10000 times: {len(tokens)} tokens")

# Run the tests
test_with_repetitive_strings()
