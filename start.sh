#!/bin/bash

echo "🔧 Installing Python dependencies..."
pip install -r requirements.txt

echo "🚀 Starting Node.js server..."
node index.js
