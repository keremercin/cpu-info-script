import os
import psutil

def get_cpu_info():
    # Get the number of logical (virtual) cores
    logical_cores = os.cpu_count()

    # Get the number of physical cores
    physical_cores = psutil.cpu_count(logical=False)

    return logical_cores, physical_cores

if __name__ == "__main__":
    logical_cores, physical_cores = get_cpu_info()
    print(f"Total logical (virtual) cores: {logical_cores}")
    print(f"Total physical cores: {physical_cores}")
