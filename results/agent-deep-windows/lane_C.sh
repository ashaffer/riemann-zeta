#!/bin/bash
# Lane C — new-rung base points + old-window ladder extensions (cheap), serial.
cd "$(dirname "$0")"
python3 run_window.py 4.75 128 75 65 rung          > logs/L4.75_m128.log 2>&1
python3 run_window.py 4.60 128 75 65 ladder-extra  > logs/L4.60_m128.log 2>&1
python3 run_window.py 4.025 96 50 40 old-ladder    > logs/L4.025_m96.log 2>&1
python3 run_window.py 4.025 112 50 40 old-ladder   > logs/L4.025_m112.log 2>&1
python3 run_window.py 3.555 96 50 40 old-ladder    > logs/L3.555_m96.log 2>&1
python3 run_window.py 3.555 112 50 40 old-ladder   > logs/L3.555_m112.log 2>&1
python3 run_window.py 2.996 80 50 40 old-ladder    > logs/L2.996_m80.log 2>&1
python3 run_window.py 2.996 96 50 40 old-ladder    > logs/L2.996_m96.log 2>&1
python3 run_window.py 5.00 160 90 80 ladder-extra  > logs/L5.00_m160.log 2>&1
python3 run_window.py 4.75 176 75 65 ladder-extra  > logs/L4.75_m176.log 2>&1
echo LANE_C_DONE
