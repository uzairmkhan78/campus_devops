import subprocess
import sys
import time

apps = [
    ("app1:app", 5000),
    ("app2:app", 5001),
    ("app3:app", 5003),
    ("app4:app", 5004),
]

processes = []

try:
    for app, port in apps:
        process = subprocess.Popen([
            sys.executable,
            "-m", "flask",
            "--app", app,
            "run",
            "--host=0.0.0.0",
            f"--port={port}"
        ])

        processes.append(process)
        print(f"Started {app} on port {port}", flush=True)

    while True:
        for process in processes:
            if process.poll() is not None:
                raise RuntimeError(
                    f"Application exited with code {process.returncode}"
                )

        time.sleep(2)

except KeyboardInterrupt:
    print("Stopping applications...")

finally:
    for process in processes:
        if process.poll() is None:
            process.terminate()

    for process in processes:
        process.wait()
