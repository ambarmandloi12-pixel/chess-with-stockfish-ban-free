# Installation Guide

Detailed setup instructions for the Chess with Stockfish educational analysis tool.

## 📋 Prerequisites

- **Python 3.7 or higher**
- **pip** (Python package installer)
- **Stockfish** (chess engine)
- ~50MB free disk space

## 🔍 Check Python Installation

```bash
python --version
# or
python3 --version
```

Should show Python 3.7 or higher.

## 🌍 Operating System Specific Instructions

### 🐧 Linux (Ubuntu/Debian)

**1. Install Stockfish:**
```bash
sudo apt-get update
sudo apt-get install stockfish
```

Verify installation:
```bash
stockfish --version
```

**2. Install Python packages:**
```bash
pip install -r requirements.txt
```

### 🍎 macOS

**1. Install Homebrew (if not installed):**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**2. Install Stockfish:**
```bash
brew install stockfish
```

Verify installation:
```bash
stockfish --version
```

**3. Install Python packages:**
```bash
pip install -r requirements.txt
```

### 🪟 Windows

**1. Install Stockfish:**

- Download from [Stockfish Official Website](https://stockfishchess.org/download/)
- Extract to a known location (e.g., `C:\Program Files\stockfish`)
- Add to PATH or note the installation path

**2. Install Python packages:**
```bash
pip install -r requirements.txt
```

**3. Configure Stockfish path (if needed):**

Edit your configuration or code to point to Stockfish:
```python
# Example
STOCKFISH_PATH = "C:\\Program Files\\stockfish\\stockfish.exe"
```

## 📦 Virtual Environment Setup (Recommended)

**1. Create virtual environment:**
```bash
python -m venv venv
```

**2. Activate it:**

Linux/macOS:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🚀 Running the Program

**1. Navigate to project directory:**
```bash
cd chess-with-stockfish-ban-free
```

**2. Run the program:**
```bash
python main.py
```

## ✅ Verification

After installation, verify everything works:

```bash
# Test Python
python -c "import chess; print('python-chess OK')"

# Test Stockfish installation
stockfish --version

# Try running the program
python main.py
```

## 🐛 Troubleshooting

### Issue: `stockfish command not found`

**Solution:** 
- Ensure Stockfish is installed and in your PATH
- On Windows, use full path: `C:\Program Files\stockfish\stockfish.exe`
- On macOS/Linux, try: `which stockfish`

### Issue: `ModuleNotFoundError: No module named 'chess'`

**Solution:**
```bash
pip install python-chess==1.10.0
```

### Issue: Python version too old

**Solution:**
- Update Python to 3.7 or higher
- Ubuntu: `sudo apt-get install python3.9`
- macOS: `brew install python@3.9`
- Windows: Download from [python.org](https://www.python.org/downloads/)

### Issue: Permission denied (Linux/macOS)

**Solution:**
```bash
chmod +x main.py
./main.py
```

### Issue: Virtual environment not activating

**Solution - Windows:**
```bash
# If you get an execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

## 📚 Next Steps

Once installed:
1. Read [README.md](README.md) for overview
2. Check project structure
3. Review source code
4. Start analyzing chess positions!

## 🆘 Still Having Issues?

1. Check your Python version: `python --version`
2. Verify Stockfish: `stockfish --version`
3. Check installed packages: `pip list`
4. Open a GitHub issue with:
   - Your OS and version
   - Python version
   - Error message
   - Steps to reproduce

---

Happy learning! ♟️
