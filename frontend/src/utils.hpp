#ifndef UTILS_HPP
#define UTILS_HPP

#include <string>

std::string getCPUInfo();
std::string getGPUInfo();
std::string getRAMInfo();
std::string getStorageInfo();
std::string getTemperatureInfo();

std::string executePythonScript(const std::string& scriptPath, const std::string& arg);

#endif // UTILS_HPP
