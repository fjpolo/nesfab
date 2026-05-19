#!/bin/bash
clear && python3 scratch/mapfab_to_json.py && python3 scratch/split_maps.py && ../../nesfab BlasNESmous.cfg
