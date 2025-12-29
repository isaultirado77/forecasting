# scripts/data.py

import requests
import zipfile
import subprocess

from config import BASE_DIR, DATA_DIR


def fpp_data():
    fpp_dir = DATA_DIR / "fpp"
    fpp_dir.mkdir(parents=True, exist_ok=True)
    fpp_zip = fpp_dir / "fpppy_data.zip"

    script = BASE_DIR / "scripts" / "download_fpp.sh"

    # Download data
    result = subprocess.run(
        [script], 
        capture_output=True, 
        text=True, 
        check=True, 
    )
    print('Script output:')
    print(result.stdout)

    with zipfile.ZipFile(fpp_zip) as zfile:
        zfile.extractall(fpp_dir)
        print(f'Datos extraidos en:', fpp_dir)

    fpp_zip.unlink()


if __name__ == '__main__': 
    # fpp data
    fpp_data()
