#!/bin/bash
# This script sets up the development environment for tiktoken.
# It installs Rust if needed and installs Python dependencies.

# Setup rust
if ! command -v rustc &> /dev/null; then
    echo "Installing Rust..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    # Source the Rust environment
    if [ -f "$HOME/.cargo/env" ]; then
        source "$HOME/.cargo/env"
        echo "Rust environment sourced successfully."
    else
        echo "WARNING: Could not find Rust environment file. You may need to restart your shell."
        echo "If Rust commands fail, try running: export PATH=\"\$HOME/.cargo/bin:\$PATH\""
    fi
fi

# Verify Rust is properly installed and in PATH
if command -v rustc &> /dev/null; then
    echo "Rust is installed: $(rustc --version)"
else
    echo "WARNING: Rust installation may not be complete. Continuing anyway..."
    # Try to add Rust to PATH explicitly
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -e .[blobfile]
pip install pytest hypothesis check-manifest build setuptools-rust
