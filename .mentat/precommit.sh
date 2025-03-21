#!/bin/bash
# This script runs checks before committing changes to tiktoken.
# It checks that the Rust code compiles, that the manifest is correct,
# and that the tests pass.

set -e  # Exit on error

# Check Rust code
echo "Checking Rust code..."
cargo check

# Run check-manifest
echo "Running check-manifest..."
check-manifest -v

# Run tests
echo "Running tests..."
pytest -xvs tests
