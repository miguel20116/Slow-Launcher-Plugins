import time, random, winsound

def run(target_pid=None):
    print("speaker_buzzer: making random beeps...")
    for _ in range(10):
        freq = random.randint(200, 2000)
        dur = random.randint(100, 500)
        print(f"speaker_buzzer: beep {freq}Hz for {dur}ms")
        winsound.Beep(freq, dur)
        time.sleep(1)
    print("speaker_buzzer finished.")
