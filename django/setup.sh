#!/bin/bash

# Setup script for Minicom Django application

echo "Setting up Minicom..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run migrations
echo "Running migrations..."
python manage.py makemigrations minicom
python manage.py migrate

echo "Setup complete!"
echo ""
echo "To start the server:"
echo "  source venv/bin/activate"
echo "  daphne -b 0.0.0.0 -p 8000 minicom.asgi:application"
echo ""
echo "Then open in browser:"
echo "  http://localhost:8000/chat/customer1/"
echo "  http://localhost:8000/chat/customer2/"
