#include "utils.hpp"
#include <iostream>
#include <array>
#include <string>
#include <stdexcept>
#include <cstdio>
#include <memory>

// Function to get CPU information by calling Python backend
std::string getCPUInfo() {
    return executePythonScript("backend/benchmark.py", "cpu");
}

// Function to get GPU information by calling Python backend
std::string getGPUInfo() {
    return executePythonScript("backend/benchmark.py", "gpu");
}

// Function to get RAM information by calling Python backend
std::string getRAMInfo() {
    return executePythonScript("backend/benchmark.py", "ram");
}

// Function to get Storage information by calling Python backend
std::string getStorageInfo() {
    return executePythonScript("backend/benchmark.py", "storage");
}

// Function to get Temperature information by calling Python backend
std::string getTemperatureInfo() {
    return executePythonScript("backend/benchmark.py", "temperature");
}

// Utility function to execute a Python script and capture its output
std::string executePythonScript(const std::string& scriptPath, const std::string& arg) {
    std::string command = "python " + scriptPath + " " + arg;
    std::array<char, 128> buffer;
    std::string result;
    FILE* pipe = _popen(command.c_str(), "r");
    if (!pipe) throw std::runtime_error("popen() failed!");
    while (fgets(buffer.data(), buffer.size(), pipe) != nullptr) {
        result += buffer.data();
    }
    _pclose(pipe);
    return result;
}
