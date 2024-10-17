import psutil
import GPUtil

def get_cpu_info():
    cpu_info = {
        "CPU": psutil.cpu_percent(interval=1),
        "Cores": psutil.cpu_count(logical=True),
        "Max Frequency": psutil.cpu_freq().max,
        "Current Frequency": psutil.cpu_freq().current
    }
    return cpu_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            "GPU": gpu.name,
            "Load": gpu.load * 100,
            "Temperature": gpu.temperature,
            "Memory Total": gpu.memoryTotal,
            "Memory Free": gpu.memoryFree,
            "Memory Used": gpu.memoryUsed,
        })
    return gpu_info

def get_ram_info():
    ram_info = {
        "Total RAM": round(psutil.virtual_memory().total / (1024 ** 3), 2),  # Convert bytes to GB
        "Available RAM": round(psutil.virtual_memory().available / (1024 ** 3), 2),
        "Used RAM": round(psutil.virtual_memory().used / (1024 ** 3), 2),
        "RAM Usage": psutil.virtual_memory().percent
    }
    return ram_info

def get_storage_info():
    storage_info = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        partition_usage = psutil.disk_usage(partition.mountpoint)
        storage_info.append({
            "Device": partition.device,
            "Mountpoint": partition.mountpoint,
            "Total Size": round(partition_usage.total / (1024 ** 3), 2),
            "Used": round(partition_usage.used / (1024 ** 3), 2),
            "Free": round(partition_usage.free / (1024 ** 3), 2),
            "Usage": partition_usage.percent
        })
    return storage_info

def run_benchmarks():
    print("Benchmarking System Resources...\n")
    
    cpu_info = get_cpu_info()
    gpu_info = get_gpu_info()
    ram_info = get_ram_info()
    storage_info = get_storage_info()
    
    print("CPU Info:", cpu_info)
    print("GPU Info:", gpu_info)
    print("RAM Info:", ram_info)
    print("Storage Info:", storage_info)

if __name__ == "__main__":
     run_benchmarks()
