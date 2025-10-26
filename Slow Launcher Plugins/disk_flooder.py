import os, time, tempfile

def run(target_pid=None):
    print("disk_flooder: writing temporary junk files...")
    tmpdir = tempfile.gettempdir()
    for i in range(10):
        filename = os.path.join(tmpdir, f"junk_{i}.bin")
        with open(filename, "wb") as f:
            f.write(os.urandom(1024 * 100))  # 100 KB
        print(f"disk_flooder: created {filename}")
        time.sleep(2)
        os.remove(filename)
        print(f"disk_flooder: deleted {filename}")
    print("disk_flooder finished.")
