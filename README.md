# Lulu Mall Review Assistant

A simple question-answering system that uses LangChain and Ollama to answer questions about Lulu Mall based on customer reviews.

## Features

- Uses local LLM (Llama 3.2) through Ollama
- Vector search for relevant reviews using FAISS
- Interactive command-line interface for asking questions

## Requirements

- Python 3.9+
- Ollama with llama3.2 and mxbai-embed-large models installed

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Ensure Ollama is running with the required models:
   ```
   ollama run llama3.2
   ollama run mxbai-embed-large
   ```

3. Run the application:
   ```
   python main.py
   ```

## Usage

Simply enter your questions about Lulu Mall when prompted, and the system will retrieve relevant reviews and provide answers based on those reviews. 