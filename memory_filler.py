# plugins/memory_filler.py
import time

def run(ctx):
    size_mb = int(ctx.config.get("max_mb", 200))
    step_mb = int(ctx.config.get("step_mb", 20))
    delay = int(ctx.config.get("delay_ms", 1000))

    ctx.logger(f"memory_filler: allocating up to {size_mb} MB in {step_mb} MB steps.")
    memory = []
    try:
        for i in range(0, size_mb, step_mb):
            memory.append(bytearray(step_mb * 1024 * 1024))
            ctx.logger(f"memory_filler: allocated {i + step_mb}/{size_mb} MB")
            time.sleep(delay / 1000)
        ctx.logger("memory_filler: done allocating memory.")
    except MemoryError:
        ctx.logger("memory_filler: system out of memory!")
    except Exception as e:
        ctx.logger(f"memory_filler: error: {e}")
    ctx.logger("memory_filler finished.")
