#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

int main (int argc, char* argv[]) {
  std::fstream inputFile(argv[1], std::ios_base::in);
  std::string line;
  std::vector<int> result;
  result.push_back(0);

  while (std::getline(inputFile, line))
  {
    if (line == "") result.push_back(0);
    else result.at(result.size() - 1) += std::stoi(line);
  }
  
  std::nth_element(result.begin(), result.begin() + 2, result.end(), std::greater<int>());
  std::cout << "Result for task 01: " << result.at(0) << std::endl;
  std::cout << "Result for task 02: " << result.at(0) + result.at(1) + result.at(2) << std::endl;

  return 0;
}