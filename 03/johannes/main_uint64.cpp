#include <iostream>
#include <fstream>
#include <string>

uint64_t priority(char a){
    uint64_t one = 1;
    int priority ;
    if (islower(a)) {
        priority = a - 'a' + 1;
    } else {
        priority = a - 'A' + 27;
    }
    return one << priority;
}

int my_log2(uint64_t n){
    int i = -1;
    while( n > 0 ){
      n >>= 1;
      i++;
    }
    return i ;
}

int main (int argc, char* argv[]) {
  std::fstream inputFile(argv[1], std::ios_base::in);
  std::string line;
  int score1 = 0; 
  int score2 = 0; 
  std::string line1;
  std::string line2;

  int count_to_2 = 0;
  while (std::getline(inputFile, line))
  {

    uint64_t firsthalf =0;
    uint64_t secondhalf =0;
    std::string compartment1 = line.substr(0, line.length() / 2);
    std::string compartment2 = line.substr(line.length() / 2);
    for (int i = 0;i< line.length()/2 ;i++) {
        firsthalf |= priority(line.at(i));
        secondhalf|= priority(line.at(i+line.length()/2));
    }
    uint64_t mask = firsthalf & secondhalf;
    score1 += my_log2(mask);

    if (count_to_2 == 0){
        line1 = line;
    }
    if (count_to_2 == 1){
        line2 = line;
    }
    

    count_to_2++;

    if (count_to_2 == 3){
        count_to_2 = 0;
        uint64_t mask1 =0;
        uint64_t mask2 =0;
        uint64_t mask3 =0;
        for (int i = 0;i < line1.length();i++){
           mask1 |= priority(line1.at(i));
        }
        for (int i = 0;i < line2.length();i++){
           mask2 |= priority(line2.at(i));
        }
        for (int i = 0;i < line.length();i++){
           mask3 |= priority(line.at(i));
        }
        uint64_t mask = mask1 & mask2 & mask3;
        score2 += my_log2(mask);
    }
  }

  std::cout<<score1 << std::endl;
  std::cout<<score2 << std::endl;
  return 0;
}