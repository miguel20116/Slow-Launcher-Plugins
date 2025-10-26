# plugins/window_freezer.py
import time, psutil

def run(ctx):
    pid = ctx.proc.pid
    p = psutil.Process(pid)
    ctx.logger(f"window_freezer: pid={pid}")
    try:
        while p.is_running():
            ctx.logger("window_freezer: freezing for 2s...")
            p.suspend()
            time.sleep(2)
            ctx.logger("window_freezer: unfreezing for 1s...")
            p.resume()
            time.sleep(1)
    except Exception as e:
        ctx.logger(f"window_freezer: error: {e}")
    ctx.logger("window_freezer finished.")
