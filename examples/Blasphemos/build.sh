#!/bin/bash
clear && python3 scripts/mapfab_to_json.py && python3 scripts/split_maps.py && python3 scripts/update_version.py && ../../nesfab BlasNESmous.cfg && python3 scripts/analyzeROM.py && python3 scripts/analyzeCHR.py && python3 scripts/analyze_metasprites.py && python3 scripts/analyze_prg_banks.py && python3 scripts/verify_physics.py
