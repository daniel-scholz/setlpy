import subprocess
import time

file_name = f"result{int(time.time())}"
with open(f"measures/{file_name}", "w+") as f:
    subprocess.call(f"python  -m cProfile -s time __main__.py",
                    stdout=f)
