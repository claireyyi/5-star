# 5-star

The goal of this project is to implement a parser for Python language, using Context-free Grammar (CFG) or BNF with ANTLR . The parser reads an input file written in a simplified “FiveStar” language and produces both a parse tree and a token stream. The project also includes a Python driver (main.py) that handles file loading, lexing, parsing, error reporting, and printing the resulting tree.

## Group members
* Claire Yi
* Amwaj Sabri
* Enobong Offiong


## Setup Instructions

### Requirements
- Python 3.10+
- Java 
- ANTLR 4
- ANTLR Python runtime

### 1. Install ANTLR
macOS:
```bash
brew install antlr

pip install antlr4-python3-runtime

antlr4 -Dlanguage=Python3 FiveStar.g4

python3 main.py project_deliverable_3.py
