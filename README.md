# idalib-example

Simple example project for [idalib](https://docs.hex-rays.com/user-guide/idalib) and the [IDA Domain API](https://github.com/HexRaysSA/ida-domain).

## Prerequisites

- [uv](https://github.com/astral-sh/uv)
- IDA Pro 9.0 or newer

## Setup

1. Create the virtual environment and install this project's dependencies:

   ```bash
   uv sync
   ```

2. Activate `idalib` once globally:

   ```bash
   # windows
   uv run "C:\Program Files\IDA Professional 9.3\idalib\python\py-activate-idalib.py"
   # macos
   uv run "/Applications/IDA Professional 9.3.app/Contents/MacOS/idalib/python/py-activate-idalib.py"
   ```

   **NOTE**: If you use [`hcli`](https://github.com/HexRaysSA/ida-hcli) to manage your IDA installation this is not necessary.

You can also use a regular Python virtual environment:

```bash
python -m venv .venv
.venv/bin/activate
pip install -e .
```

## Running the examples

This repository contains two small examples:

- `idalib_example.py` — uses `idapro` + standard IDAPython modules
- `domain_example.py` — uses the [IDA Domain API](https://github.com/HexRaysSA/ida-domain)

### Run examples

```bash
uv run idalib_example.py crackme03.elf
uv run domain_example.py crackme03.elf
```

## What the scripts do

Both scripts:

- open the input file with idalib
- run auto-analysis
- print the discovered functions

## Agents

Coding agents are pretty good at using the IDA Domain API. You can look at [ida-plugin-development/skills](https://github.com/HexRaysSA/ida-claude-plugins/tree/main/plugins/ida-plugin-development/skills) as a starting point.

## Files

- `idalib_example.py`
- `domain_example.py`
- `crackme03.elf` — sample input file
