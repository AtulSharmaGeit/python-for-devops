import psutil

def get_threshold(message):
    try:
        return int(input(message))
    except ValueError:
        print("Invalid input! Using default value of 80.")
        return 80
    
def check_cpu(cpu_threshold):
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > cpu_threshold:
        print("CPU Alert! Usage is high.")
    else:
        print("CPU is safe")

def check_memory(memory_threshold):
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > memory_threshold:
        print("Memory Alert! Usage is high.")
    else:
        print("Memory is safe.")

def check_disk(disk_threshold):
    try:
        disk_usage = psutil.disk_usage('/').percent
        if disk_usage > disk_threshold:
            print("Disk Alert! Space is low.")
        else:
            print("Disk space is available.")
    except Exception as e:
        print("Error checking disk: ",e)

def check_system_health():
    print("\n--- System Health Check ---")
    cpu_threshold = get_threshold("Enter CPU threshold (%): ")
    check_cpu(cpu_threshold)

    memory_threshold = get_threshold("Enter Memory threshold (%): ")
    check_memory(memory_threshold)

    disk_threshold = get_threshold("Enter Disk threshold (%): ")
    check_disk(disk_threshold)

check_system_health()