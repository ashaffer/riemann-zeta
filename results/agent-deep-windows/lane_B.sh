#!/bin/bash
# Lane B — refinement + ladder intermediates, serial.
cd "$(dirname "$0")"
python3 run_window.py 4.50 128 75 65 refine       > logs/L4.50_m128.log 2>&1
python3 run_window.py 4.60 144 75 65 rung         > logs/L4.60_m144.log 2>&1
python3 run_window.py 4.75 144 75 65 ladder-extra > logs/L4.75_m144.log 2>&1
python3 run_window.py 5.00 144 90 80 stretch      > logs/L5.00_m144.log 2>&1
python3 run_window.py 4.50 160 75 65 ladder-extra > logs/L4.50_m160.log 2>&1
python3 run_window.py 4.60 160 75 65 ladder-extra > logs/L4.60_m160.log 2>&1
echo LANE_B_DONE
