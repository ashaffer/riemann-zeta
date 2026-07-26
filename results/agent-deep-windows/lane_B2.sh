#!/bin/bash
# Restart lane B' — deep ladder completions, then depth.
cd "$(dirname "$0")"
python3 run_window.py 4.75 160 75 65 rung-restart   > logs/L4.75_m160.log 2>&1
python3 run_window.py 4.50 160 75 65 ladder-extra   > logs/L4.50_m160.log 2>&1
python3 run_window.py 5.00 160 90 80 stretch        > logs/L5.00_m160.log 2>&1
python3 run_window.py 5.50 168 100 90 addendum      > logs/L5.50_m168.log 2>&1
echo LANE_B2_DONE
