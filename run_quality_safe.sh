#!/bin/bash
echo "Running safe code quality improvements..."

# Format all Python files
echo "Formatting with Black..."
black OWN_PACKAGE/

# Organize imports
echo "Organizing imports with Isort..."
isort OWN_PACKAGE/

# Run linting
echo "Running Flake8 linting..."
flake8 OWN_PACKAGE/ --count --statistics

echo "Quality improvements completed!"
