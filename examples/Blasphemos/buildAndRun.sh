#!/bin/bash
clear && python3 update_version.py && ../../nesfab BlasNESmous.cfg
python3 analyzeROM.py
open -a ~/Downloads/Mesen/Mesen.app BlasNESmous.nes
