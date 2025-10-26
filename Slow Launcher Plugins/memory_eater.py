import time

def run(target_pid=None):
    print("memory_eater: slowly consuming memory...")
    data = []
    try:
        for i in range(50):
            data.append(" " * 10**6)  # 1 MB per loop
            print(f"memory_eater: {len(data)} MB allocated")
            time.sleep(1)
    except MemoryError:
        print("memory_eater: ran out of memory!")
    finally:
        print("memory_eater finished.")
