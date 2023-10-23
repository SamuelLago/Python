import time
for numero in range(600, -1, -1):
    mino = numero // 60
    seg = numero % 60
    print(f"{mino}:{seg}")
    time.sleep(1)

import time

print("10:00")
for m in range(9,-1,-1):
    for s in range(59, -1,-1):
        print(f"{m}:{s}")
        time.sleep(1)