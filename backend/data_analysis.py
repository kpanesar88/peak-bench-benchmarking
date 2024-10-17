# backend/data_analysis.py

def analyze_data(data):
    # Initialize analysis dictionary
    analysis = {}

    # Extract and analyze CPU info
    cpu_info = data.get("CPU Info", {})
    analysis["CPU Usage"] = f"{cpu_info.get('CPU', 'N/A')}%"
    analysis["Cores"] = cpu_info.get('Cores', 'N/A')
    analysis["Max Frequency"] = f"{cpu_info.get('Max Frequency', 'N/A')} MHz"
    analysis["Current Frequency"] = f"{cpu_info.get('Current Frequency', 'N/A')} MHz"

    # Extract and analyze GPU info
    gpu_info = data.get("GPU Info", [])
    if gpu_info:
        analysis["GPU Name"] = gpu_info[0].get("GPU", "No GPU")
        analysis["GPU Load"] = f"{gpu_info[0].get('Load', 'N/A')}%"
        analysis["GPU Temperature"] = f"{gpu_info[0].get('Temperature', 'N/A')}°C"
    else:
        analysis["GPU Usage"] = "No GPU"

    # Extract and analyze RAM info
    ram_info = data.get("RAM Info", {})
    analysis["Total RAM"] = f"{ram_info.get('Total RAM', 'N/A')} GB"
    analysis["Used RAM"] = f"{ram_info.get('Used RAM', 'N/A')} GB"
    analysis["Available RAM"] = f"{ram_info.get('Available RAM', 'N/A')} GB"
    analysis["RAM Usage"] = f"{ram_info.get('RAM Usage', 'N/A')}%"

    # Extract and analyze storage info
    storage_info = data.get("Storage Info", [])
    for storage in storage_info:
        device = storage.get("Device", "N/A")
        analysis[f"{device} Total Size"] = f"{storage.get('Total Size', 'N/A')} GB"
        analysis[f"{device} Used"] = f"{storage.get('Used', 'N/A')} GB"
        analysis[f"{device} Free"] = f"{storage.get('Free', 'N/A')} GB"
        analysis[f"{device} Usage"] = f"{storage.get('Usage', 'N/A')}%"

    return analysis
