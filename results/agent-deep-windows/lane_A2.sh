#!/bin/bash
# Restart lane A' — analysis-critical ladder points, then depth.
cd "$(dirname "$0")"
python3 run_window.py 4.75 144 75 65 rung-restart   > logs/L4.75_m144.log 2>&1
python3 run_window.py 4.25 144 75 65 ladder-extra   > logs/L4.25_m144.log 2>&1
python3 run_window.py 5.00 144 90 80 stretch        > logs/L5.00_m144.log 2>&1
python3 run_window.py 5.50 152 100 90 addendum      > logs/L5.50_m152.log 2>&1
echo LANE_A2_DONE
