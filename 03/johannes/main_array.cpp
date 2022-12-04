#include <iostream>
#include <fstream>
#include <string>

int priority(char a){
    uint64_t one = 1;
    int priority ;
    if (islower(a)) {
        priority = a - 'a' + 1;
    } else {
        priority = a - 'A' + 27;
    }
    return priority;
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

    bool firsthalf [53];
    bool secondhalf [53];
    for (int i=0;i<53;i++){
        firsthalf[i] = false;
        secondhalf[i] = false;
    }

    for (int i = 0;i< line.length()/2 ;i++) {
        firsthalf [priority(line.at(i))] = true;
        secondhalf[priority(line.at(i+line.length()/2))] = true;
    }
    for (int i=0;i<53;i++){
        if(firsthalf[i] && secondhalf[i]){
            score1 += i;            
        }
    }

    if (count_to_2 == 0){
        line1 = line;
    }
    if (count_to_2 == 1){
        line2 = line;
    }
    

    count_to_2++;

    if (count_to_2 == 3){
        count_to_2 = 0;

        bool mask1 [53];
        bool mask2 [53];
        bool mask3 [53];
        for (int i=0;i<53;i++){
            mask1[i] = false;
            mask2[i] = false;
            mask3[i] = false;
        }

        for (int i = 0;i< line1.length() ;i++) {
            mask1[priority(line1.at(i))] = true;
        }
        for (int i = 0;i< line2.length() ;i++) {
            mask2[priority(line2.at(i))] = true;
        }
        for (int i = 0;i< line.length() ;i++) {
            mask3[priority(line.at(i))] = true;
        }

        for (int i=0;i<53;i++){
            if(mask1[i] && mask2[i] && mask3[i]){
                score2 += i;            
            }
        }
    }
  }

  std::cout<<score1 << std::endl;
  std::cout<<score2 << std::endl;
  return 0;
}