import pytest
import tiktoken


def test_long_repetitive_string():
    """Test that encoding a very long repetitive string doesn't crash with stack overflow."""
    # A shorter version for faster testing, but still long enough to potentially cause problems
    bad_string = "X" * 100000  # 100k repeated X's (shorter than reported bug but should test the fix)
    encoder = tiktoken.get_encoding("cl100k_base")
    
    # Test regular encode
    tokens = encoder.encode(bad_string)
    # The exact token count may depend on the tokenizer, but we just care that it completes
    assert len(tokens) > 0
    
    # Reconstruct the original string and verify it's correct
    decoded = encoder.decode(tokens)
    assert decoded == bad_string
    
    # Also test encode_to_numpy to make sure that works too
    try:
        import numpy as np
        tokens_np = encoder.encode_to_numpy(bad_string)
        assert len(tokens_np) > 0
        assert (tokens_np == np.array(tokens, dtype=np.uint32)).all()
    except ImportError:
        # Skip numpy test if numpy is not available
        pass


def test_long_repetitive_with_special():
    """Test that long repetitive strings with special tokens are handled correctly."""
    # Mix in some special tokens to ensure the chunking handles them properly
    prefix = "<|endoftext|>"
    suffix = "<|endoftext|>"
    bad_string = prefix + "X" * 50000 + suffix
    
    encoder = tiktoken.get_encoding("cl100k_base")
    tokens = encoder.encode(bad_string, allowed_special="all")
    
    # Check that we still have the special tokens at start and end
    assert tokens[0] == encoder.encode_single_token("<|endoftext|>")
    assert tokens[-1] == encoder.encode_single_token("<|endoftext|>")
    
    # Verify decoding works
    decoded = encoder.decode(tokens)
    assert decoded == bad_string
