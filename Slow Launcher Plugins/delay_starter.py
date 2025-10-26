# plugins/delay_starter.py
import time

def run(ctx):
    delay = int(ctx.config.get("delay_ms", 5000))
    ctx.logger(f"delay_starter: waiting {delay} ms before launch...")
    time.sleep(delay / 1000)
    ctx.logger("delay_starter: launch delay finished.")
