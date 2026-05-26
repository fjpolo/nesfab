#!/bin/bash
clear

echo "Starting Quick Build Pipeline (Dev Version)..."

python3 scripts/mapfab_to_json.py || exit $?
python3 scripts/split_maps.py || exit $?
python3 scripts/update_version.py || exit $?

echo "Building Dev version..."
python3 scripts/set_build_flag.py dev || exit $?
../../nesfab BlasNESmous.cfg || exit $?

# Rename the output
cp BlasNESmous.nes BlasNESmous_dev.nes
cp BlasNESmous.mlb BlasNESmous_dev.mlb

echo "Launching Mesen..."
~/Downloads/Mesen/Mesen.app/Contents/MacOS/Mesen BlasNESmous_dev.nes &
