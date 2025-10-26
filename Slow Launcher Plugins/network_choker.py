import time

def run(target_pid=None):
    print("network_choker: simulating 1 bps connection...")
    for i in range(20):
        print(f"network_choker: sending 1 byte ({i+1}/20)")
        time.sleep(8)  # roughly 1 byte per 8 seconds (1 bps)
    print("network_choker finished.")
