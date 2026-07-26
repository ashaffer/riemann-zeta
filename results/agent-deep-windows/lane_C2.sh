#!/bin/bash
# Restart lane C' — old-window ladder completion (cheap), then depth.
cd "$(dirname "$0")"
python3 run_window.py 4.025 112 50 40 old-ladder    > logs/L4.025_m112.log 2>&1
python3 run_window.py 3.555 96 50 40 old-ladder     > logs/L3.555_m96.log 2>&1
python3 run_window.py 3.555 112 50 40 old-ladder    > logs/L3.555_m112.log 2>&1
python3 run_window.py 5.00 176 90 80 stretch        > logs/L5.00_m176.log 2>&1
python3 run_window.py 5.50 184 100 90 addendum      > logs/L5.50_m184.log 2>&1
echo LANE_C2_DONE
