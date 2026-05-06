#!/bin/bash
clear && python3 update_version.py && ../../nesfab BlasNESmous.cfg
python3 analyzeROM.py
~/Downloads/Mesen/Mesen.app/Contents/MacOS/Mesen BlasNESmous.nes &
