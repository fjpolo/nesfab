import os

keywords = ["frame_counter"]

path = "analysis/ram_variables.txt"
try:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line_num, line in enumerate(f, 1):
            for kw in keywords:
                if kw in line:
                    print(f"{line_num}: {line.strip()}")
except Exception as e:
    print(e)
