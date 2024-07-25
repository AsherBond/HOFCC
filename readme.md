# CognitiveCompiler

CognitiveCompiler is a Python application that acts as a higher-order function (HOF) cognitive generator of code in various programming and spoken languages. By leveraging state-of-the-art pre-trained language models, CognitiveCompiler can autonomously generate "Hello, World!" code snippets in different programming languages and translate them into multiple spoken languages. This demonstrates the potential of cognitive computing in automating and enhancing software development tasks.

## Features

- **Code Generation**: Generates "Hello, World!" code snippets in various programming languages using DistilGPT-2.
- **Translation**: Translates generated code snippets into multiple spoken languages using MarianMT models.
- **Customizable**: Allows specification of the number of programming and spoken languages to use.

## What is a Cognitive Compiler?

A cognitive compiler is an advanced AI system that combines the capabilities of natural language processing (NLP) and machine learning to generate and manipulate code. It leverages pre-trained models to understand and produce human-like code snippets in multiple programming languages. The cognitive compiler can be seen as a higher-order function (HOF) because it operates on other functions (code generation and translation) to produce a more complex output.

### Higher-Order Function (HOF)

In programming, a higher-order function is a function that does at least one of the following:
1. Takes one or more functions as arguments.
2. Returns a function as its result.

CognitiveCompiler exemplifies HOF by using language models to dynamically generate code and translate it, thus automating tasks typically performed by human developers.

## Requirements

- Python 3.8 or later
- PyTorch
- Transformers
- SentencePiece
- Sacremoses

## Installation

1. **Clone the repository:**

   ```sh
   git clone git@github.com:Distillative-AI/HOFCC.git
   cd CognitiveCompiler
   ```

2. **Set up a virtual environment:**

   ```sh
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Hello World script:**

   ```sh
   python hello_world.py
   ```

2. **Check the output directory:**

   The generated code snippets and translations will be saved in the `output` directory.

## Example

The following example demonstrates how to use the CognitiveCompiler to generate "Hello, World!" code snippets and their translations:

### `hofcc.py`

This file contains the generic functionality of the CognitiveCompiler class.


### `hello_world.py`

This file demonstrates generating "Hello, World!" in 5 programming languages and 5 spoken languages, taking the number of languages as parameters.


### `requirements.txt`

Ensure you have all the required libraries listed:



