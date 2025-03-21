#!/bin/bash
# This script runs checks before committing changes to tiktoken.
# It checks that the manifest is correct and runs a basic test suite.

set -e  # Exit on error

# Make sure Rust binaries are in PATH
export PATH="$HOME/.cargo/bin:$PATH"

# Source cargo env if it exists
if [ -f "$HOME/.cargo/env" ]; then
    source "$HOME/.cargo/env"
fi

# Check if cargo is available
if command -v cargo &> /dev/null; then
    # Check Rust code
    echo "Checking Rust code..."
    cargo check
else
    echo "WARNING: Cargo not found, skipping Rust code checks."
    echo "Please run the setup.sh script first or install Rust manually."
fi

# Run check-manifest
echo "Running check-manifest..."
check-manifest -v

# Run basic tests (faster subset for precommit)
echo "Running basic tests..."
# Run only the simple tests and limit verbosity for speed
pytest -xvs tests/test_simple_public.py
