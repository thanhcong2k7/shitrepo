import os
import sys
import threading
import subprocess
import pathlib
import time
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    import psutil
except (ImportError, ModuleNotFoundError):
    print("Missing psutil, installing....")
    os.system("{} -m pip install psutil".format(sys.executable))

import psutil

if os.name == 'nt':
    s = "\\"
    os.system("cls")
else:
    s = "/"
    os.system("clear")


version = "{major}.{minor}".format(major = sys.version_info.major, minor = sys.version_info.minor)

physical_cores = psutil.cpu_count(logical=False)
logical_cores = psutil.cpu_count(logical=True)
total_ram_gb = round(psutil.virtual_memory().total / (1024 ** 2))

python_executable = sys.executable
executable = "main.py"
executable_path = pathlib.Path("lib{s}{version}{s}{executable}".format(version = version, s = s, executable = executable)).resolve()
pwd_path = ""
threads = []
all_files = {}
isFolder = None

mode = -1
is_module = -1
addDauricum = -1

def set_terminal_title(title):
    if os.name == 'nt':  
        os.system(f"title {title}")
    elif os.name == 'posix':  
        sys.stdout.write(f"\033]0;{title}\007")
        sys.stdout.flush()

def run(id, file, semaphore):
    with semaphore:
        print("\n\\ Process {} starting...".format(id), flush=True)
        cmd = "cd \"{pwd_path}\" && \"{python_executable}\" \"{executable_path}\" \"{python_file}\" mode={mode} is_module={is_module} addDauricum={addDauricum}".format(pwd_path = pwd_path, python_executable = python_executable, executable_path = executable_path, python_file = file, mode = mode, is_module = is_module, addDauricum = addDauricum)
        code = os.system(cmd)
        if (code == 0):
            print("\n/ Process {} completed\n".format(id), flush=True)
            globals()["all_files"][file] = 1
        else:
            print("\n! Process {} failed with [{}]\n".format(id, file), flush=True)
            globals()["all_files"][file] = 0
            
    return

if (__name__ == '__main__'):
    set_terminal_title("SCRIPT AUTO OBF BY KHANHNGUYEN9872")
    
    print()
    print("  SCRIPT AUTO OBF BY KHANHNGUYEN9872")
    print("  Python: {}".format(version))
    print("  Python executable: [{}]".format(python_executable))
    print("  CPU: {} cores / {} threads".format(physical_cores, logical_cores))
    print("  RAM: {} MB".format(total_ram_gb))
    print()

    if not (pathlib.Path(executable_path).is_file()):
        print("! Unsupported current python, lib is not found")
        sys.exit(1)

    file_or_path = input("> Path file (a <.py> / a folder contain <.py> file): ")
    if not file_or_path:
        print("! Need a path for a file or a folder")
    
    if ('"' in file_or_path or "'" in file_or_path):
        file_or_path = eval("r" + file_or_path)

    file_or_path = file_or_path.replace("\\", "/")

    if (pathlib.Path(file_or_path).is_file()):
        pwd_path = s.join("/".join(file_or_path.split("\\")).split("/")[:-1])
        if (pathlib.Path(file_or_path).suffix == ".py"):
            file_path = pathlib.Path(file_or_path).resolve()
            all_files[file_path] = -1
            isFolder = False
        else:
            print("! File extension must be <.py>")
            sys.exit(1)
    elif (pathlib.Path(file_or_path).is_dir()):
        pwd_path = file_or_path
        py_files = pathlib.Path(file_or_path).glob("*.py")
        for file in py_files:
            all_files[file] = -1
        isFolder = True
    else:
        print("! Wrong path")
        sys.exit(1)

    is_module = input(">> Type File: [0-Main, 1-Import, 2-Exec]: ")
    if (is_module not in ["0", "1", "2"]):
        print("! Wrong Type file")
        sys.exit(1)

    mode = input(">> Mode ENC [2-Medium]: ")
    if (mode not in ["2"]):
        print("! Wrong Mode ENC")
        sys.exit(1)

    addDauricum = input(">> Add dauricum?: [0-No, 1-Yes]: ")
    if (addDauricum not in ["0", "1"]):
        print("! Wrong Add dauricum")
        sys.exit(1)

    if (isFolder):
        print()
        print("For maximum performance when obf multiple file, choose thread")
        cores = input(">> Using core or thread to process? [0-Core, 1-Thread]: ")
        if (cores not in ["0", "1"]):
            print("! Wrong choose")
            sys.exit(1)

        if (cores == "0"):
            cores = physical_cores
        elif (cores == "1"):
            cores = logical_cores
    else:
        cores = 1

    semaphore = threading.Semaphore(cores)
    for _ in range(0, len(all_files)):
        threads.append(threading.Thread(target=run, args=(_ + 1, list(all_files)[_], semaphore, )))

    time_start = time.time()

    # start

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # end

    time_stop = time.time()
    elapsed_time = time_stop - time_start

    time.sleep(1)

    total = len(all_files)
    completed = 0
    failed = 0
    not_running = 0

    for i in all_files:
        if (all_files[i] == 0):
            failed += 1
        elif (all_files[i] == 1):
            completed += 1
        else:
            not_running += 1

    print()
    print(">> Total: {} script".format(total))
    print(">> Not running: {} script".format(not_running))
    print(">> Completed: {} script".format(completed))
    print(">> Failed: {} script".format(failed))
    print(">> Total time: {} seconds".format(round(elapsed_time, 0)))
    print()

