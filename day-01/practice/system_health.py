import psutil

def check_system_health():
    
    cpu_threshold = int(input("Enter CPU threshold: "))
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > cpu_threshold:
        print("CPU Alert Email Sent...")
    else:
        print("CPU In Safe State.")

    memory_threshold = int(input("Enter Memory threshold: "))
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > memory_threshold:
        print("High Memory Usage Alert Email Sent...")
    else:
        print("Sufficient Memory Available.")
    
    disk_threshold = int(input("Enter Disk threshold: "))
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > disk_threshold:
        print("Low Disk Space Alert Email Sent...")
    else:
        print("Disk Space Available.")
 
check_system_health()