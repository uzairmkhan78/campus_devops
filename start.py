import subprocess
import sys
import time

apps = [
    ("app1:app", 5001),
    ("app2:app", 5002),
    ("app3:app", 5003),
    ("app4:app", 5004),
]

processes = []

try:
    for app, port in apps:
        process = subprocess.Popen([
            sys.executable,
            "-m",
            "gunicorn",
            "--bind",
            f"0.0.0.0:{port}",
            app
        ])
        processes.append(process)

    while True:
        for process in processes:
            if process.poll() is not None:
                raise RuntimeError("An application stopped unexpectedly")
        time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    for process in processes:
        process.terminate()
