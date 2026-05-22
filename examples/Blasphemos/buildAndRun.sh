#!/bin/bash
clear && python3 scratch/mapfab_to_json.py && python3 scratch/split_maps.py && python3 update_version.py && ../../nesfab BlasNESmous.cfg
python3 analyzeROM.py
python3 scratch/analyze_metasprites.py
~/Downloads/Mesen/Mesen.app/Contents/MacOS/Mesen BlasNESmous.nes &
