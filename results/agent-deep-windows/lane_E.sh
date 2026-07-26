#!/bin/bash
# Lane E — L=5.00 triple completion, then 5.50 middle point.
cd "$(dirname "$0")"
python3 run_window.py 5.00 160 90 80 stretch     > logs/L5.00_m160.log 2>&1
python3 run_window.py 5.50 168 100 90 addendum   > logs/L5.50_m168.log 2>&1
echo LANE_E_DONE
