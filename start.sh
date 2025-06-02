#!/bin/bash

echo "🔧 Installing Python dependencies..."
pip install -r requirements.txt

echo "📦 Installing Node.js dependencies..."
npm install

echo "🚀 Starting Node.js server..."
node index.js
