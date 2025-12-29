# config.py

from pathlib import Path

BASE_DIR = Path().cwd()
DATA_DIR = BASE_DIR / "data"

dirs = [BASE_DIR, DATA_DIR]


if __name__ == '__main__': 
    for dir in dirs: 
        print(dir, dir.exists(), dir.is_dir())