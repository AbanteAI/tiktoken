#!/bin/bash
# This script sets up the development environment for tiktoken.
# It installs Rust if needed and installs Python dependencies.

# Setup rust
if ! command -v rustc &> /dev/null; then
    echo "Installing Rust..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    source "$HOME/.cargo/env"
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -e .[blobfile]
pip install pytest hypothesis check-manifest build setuptools-rust
