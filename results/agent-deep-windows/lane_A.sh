#!/bin/bash
# Lane A — heaviest single runs, serial. One single-threaded python at a time.
cd "$(dirname "$0")"
python3 run_window.py 4.25 128 75 65 refine       > logs/L4.25_m128.log 2>&1
python3 run_window.py 4.50 144 75 65 refine       > logs/L4.50_m144.log 2>&1
python3 run_window.py 4.75 160 75 65 rung         > logs/L4.75_m160.log 2>&1
python3 run_window.py 5.00 176 90 80 stretch      > logs/L5.00_m176.log 2>&1
python3 run_window.py 4.25 144 75 65 ladder-extra > logs/L4.25_m144.log 2>&1
echo LANE_A_DONE
