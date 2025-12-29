#!/usr/bin/env bash
set -e

URL="https://otexts.com/fpppy/data/fpppy_data.zip"
OUT="data/fpp/fpppy_data.zip"

curl -L \
  -H "User-Agent: Mozilla/5.0" \
  -o "$OUT" \
  "$URL"

echo "Descarga completada: $OUT"
