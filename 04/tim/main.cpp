#include <iostream>
#include <fstream>
#include <string>

int main (int argc, char* argv[]) {
  std::ifstream inputFile (argv[1]);
  std::string line;
  int result01 = 0;
  int result02 = 0;
  while (std::getline(inputFile, line)) {
    int posComma = line.find(",");
    int posFirstHyphen = line.find("-");
    int posSecondHyphen = line.rfind("-");
    int firstElveBegin = std::stoi(line.substr(0, posFirstHyphen));
    int firstElveEnd = std::stoi(line.substr(posFirstHyphen + 1, posComma));
    int secondElveBegin = std::stoi(line.substr(posComma + 1, posSecondHyphen));
    int secondElveEnd = std::stoi(line.substr(posSecondHyphen + 1, line.size()));
    if (((firstElveBegin <= secondElveBegin) && (firstElveEnd >= secondElveEnd)) ||
      ((secondElveBegin <= firstElveBegin) && (secondElveEnd >= firstElveEnd))) result01++;
    if (!((firstElveEnd < secondElveBegin) || (secondElveEnd < firstElveBegin))) result02++;
  }

  std::cout << "Result for task 01: " << result01 << std::endl;
  std::cout << "Result for task 02: " << result02 << std::endl;

  return 0;
}