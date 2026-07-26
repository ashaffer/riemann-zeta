#!/bin/bash
# Lane F — the 5.50 discriminator ladder, outer points.
cd "$(dirname "$0")"
python3 run_window.py 5.50 152 100 90 addendum   > logs/L5.50_m152.log 2>&1
python3 run_window.py 5.50 184 100 90 addendum   > logs/L5.50_m184.log 2>&1
echo LANE_F_DONE
