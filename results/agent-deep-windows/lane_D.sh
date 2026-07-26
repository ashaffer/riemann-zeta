#!/bin/bash
# Lane D — false-plateau repair points; waits for a free worker slot
# (max 3 concurrent run_window.py processes) before each run.
cd "$(dirname "$0")"
wait_slot () {
  while [ "$(pgrep -fc 'run_window.py')" -ge 3 ]; do sleep 20; done
}
wait_slot
python3 run_window.py 4.25 160 75 65 plateau-check > logs/L4.25_m160.log 2>&1
wait_slot
python3 run_window.py 4.60 160 75 65 plateau-check > logs/L4.60_m160.log 2>&1
echo LANE_D_DONE
