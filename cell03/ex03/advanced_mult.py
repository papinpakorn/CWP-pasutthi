#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:
        j = 0
        results = []
        while j <= 10:
            results.append(str(i * j))
            j += 1
        print(f"Table de {i}: " + " ".join(results))
        i += 1