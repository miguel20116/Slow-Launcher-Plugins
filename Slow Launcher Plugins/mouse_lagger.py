import time, random

def run(target_pid=None):
    print("mouse_lagger: simulating mouse lag...")
    for _ in range(20):
        delay = random.uniform(0.5, 3.0)
        print(f"mouse_lagger: freezing input for {delay:.1f}s")
        time.sleep(delay)
    print("mouse_lagger finished.")
