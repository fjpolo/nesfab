#!/bin/bash
clear && python3 scratch/mapfab_to_json.py && python3 scratch/split_maps.py && ../../nesfab BlasNESmous.cfg && python3 scratch/analyze_metasprites.py && python3 scratch/analyze_prg_banks.py && python3 scratch/verify_physics.py
