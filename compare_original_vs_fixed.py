import tempfile
import os
import subprocess
import tiktoken
import time

def run_test_with_code_version(version, code_to_test):
    """Run specified test code with a specific version of the Rust code."""
    # Create temp file to store current lib.rs
    with tempfile.NamedTemporaryFile(suffix='.rs', delete=False) as temp:
        temp_path = temp.name
    
    # Backup current lib.rs
    subprocess.run("cp src/lib.rs " + temp_path, shell=True)
    
    try:
        if version == "original":
            # Checkout original version
            subprocess.run("git checkout origin/main -- src/lib.rs", shell=True)
        else:
            # Our current version is already the fixed one
            pass
            
        # Build the code
        subprocess.run("pip install -e . > /dev/null", shell=True)
        
        # Run the test code
        start = time.time()
        result = eval(code_to_test)
        end = time.time()
        
        return result, end - start
    finally:
        # Restore our version
        subprocess.run("cp " + temp_path + " src/lib.rs", shell=True)
        os.unlink(temp_path)
        subprocess.run("pip install -e . > /dev/null", shell=True)

# Compare tokenization of a few test cases using both original and fixed code 
test_cases = [
    ("X" * 1000),
    ("X" * 10000),
    ("X" * 50000),
    ("Hello world! " + ("X" * 1000) + " This is a test."),
    ("ABC" * 1000)
]

print("Comparing tokenization between original and fixed code:")
print("------------------------------------------------------")

for i, text in enumerate(test_cases):
    print(f"Test case #{i+1}:")
    
    # Get tokens with original code
    code = "len(tiktoken.get_encoding('cl100k_base').encode(text))"
    orig_tokens, orig_time = run_test_with_code_version("original", code)
    
    # Get tokens with fixed code 
    fixed_tokens, fixed_time = run_test_with_code_version("fixed", code)
    
    print(f"  Original: {orig_tokens} tokens in {orig_time:.4f} seconds")
    print(f"  Fixed:    {fixed_tokens} tokens in {fixed_time:.4f} seconds") 
    
    if orig_tokens == fixed_tokens:
        print("  ✓ Tokenizations match!")
    else:
        print(f"  ✗ Tokenizations differ! Original: {orig_tokens}, Fixed: {fixed_tokens}")
    print()
