#include <iostream>
#include <fstream>
#include <cctype>
#include <string>
#include <vector>
#include <bitset>

int getLookUpVectorPosition (char character) {
  if (std::isupper(character)) return int(character) - 65 + 26;
  else return int(character) - 97;
}

int main (int argc, char* argv[]) {
  std::ifstream inputFile (argv[1]);
  std::string line;
  int resultTask01 = 0;
  int resultTask02 = 0;
  std::bitset<52> lookUpVectorTask01;
  std::vector<std::bitset<52>> lookUpVectorsTask02 (3);
  int elfCount = 0;

  while (std::getline(inputFile, line)) {
    for (auto posPointer = line.begin(); posPointer != line.begin() + line.size() / 2; posPointer++) {
      int lookUpVectorPosition = getLookUpVectorPosition(*posPointer);
      lookUpVectorTask01[lookUpVectorPosition] = 1;
      lookUpVectorsTask02.at(elfCount)[lookUpVectorPosition] = 1;
    }
    for (auto posPointer = line.begin() + line.size() / 2; posPointer != line.end(); posPointer++) {
      int lookUpVectorPosition = getLookUpVectorPosition(*posPointer);
      if (lookUpVectorTask01[lookUpVectorPosition] == 1) resultTask01 += lookUpVectorPosition + 1;
      lookUpVectorsTask02.at(elfCount)[lookUpVectorPosition] = 1;
    }
    lookUpVectorTask01.reset();
    if (elfCount == 2) {
      for (int pos = 0; pos < lookUpVectorsTask02.at(0).size(); pos++) {
        if ((lookUpVectorsTask02.at(0)[pos] == 1) && 
          (lookUpVectorsTask02.at(1)[pos] == 1) && 
          (lookUpVectorsTask02.at(2)[pos] == 1)) {
          resultTask02 += pos + 1;
          break;
        }
      }
      elfCount = 0;
      lookUpVectorsTask02.at(0).reset();
      lookUpVectorsTask02.at(1).reset();
      lookUpVectorsTask02.at(2).reset();
    }
    else elfCount++;
  }

  std::cout << "Result for task 01: " << resultTask01 << std::endl;
  std::cout << "Result for task 02: " << resultTask02 << std::endl;

  return 0;
}