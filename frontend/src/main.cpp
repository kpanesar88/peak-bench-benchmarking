#include <iostream>
#include "utils.hpp"

int main() {
    std::cout << "Welcome to Benchmark++" << std::endl;

    // Get system information by calling the functions from utils.cpp
    std::string cpu_info = getCPUInfo();
    std::string gpu_info = getGPUInfo();
    std::string ram_info = getRAMInfo();
    std::string storage_info = getStorageInfo();
    std::string temp_info = getTemperatureInfo();
    
    // Display the gathered system information
    std::cout << "CPU Info: " << cpu_info << std::endl;
    std::cout << "GPU Info: " << gpu_info << std::endl;
    std::cout << "RAM Info: " << ram_info << std::endl;
    std::cout << "Storage Info: " << storage_info << std::endl;
    std::cout << "Temperature Info: " << temp_info << std::endl;

    return 0;
}
