#include <iostream>
#include <fstream>

#define SCORE_DEFEAT 0
#define SCORE_DRAW 3
#define SCORE_WIN 6

enum RockPaperScissors {
  rock = 1,
  paper = 2,
  scissors = 3
};

enum Outcome {
  defeat,
  draw,
  win
};

int getRockPaperScissorsScore (RockPaperScissors opponentsChoice, RockPaperScissors myChoice) {
  int result = 0;
  if (opponentsChoice == myChoice) result += SCORE_DRAW;
  else if (opponentsChoice == rock) {
    if (myChoice == paper) result += SCORE_WIN;
    else result += SCORE_DEFEAT;
  }
  else if (opponentsChoice == paper) {
    if (myChoice == rock) result += SCORE_DEFEAT;
    else result += SCORE_WIN;
  }
  else {
    if (myChoice == rock) result += SCORE_WIN;
    else result += SCORE_DEFEAT;
  }
  result += myChoice;
  return result;
}

RockPaperScissors getMyChoice (RockPaperScissors opponentsChoice, Outcome outcome) {
  if (outcome == defeat) {
    if (opponentsChoice == rock) return scissors;
    else if (opponentsChoice == paper) return rock;
    else return paper;
  }
  else if (outcome == win) {
    if (opponentsChoice == rock) return paper;
    else if (opponentsChoice == paper) return scissors;
    else return rock;
  }
  else return opponentsChoice;
}

int main (int argc, char* argv[]) {
  std::ifstream inputFile(argv[1]);
  char chOpponentsChoice, chMyChoice;
  RockPaperScissors opponentsChoice, myChoice;
  Outcome outcome;
  int totalScore01 = 0;
  int totalScore02 = 0;

  while (inputFile >> chOpponentsChoice >> chMyChoice) {
    if (chOpponentsChoice == 'A') opponentsChoice = rock;
    else if (chOpponentsChoice == 'B') opponentsChoice = paper;
    else opponentsChoice = scissors;
    if (chMyChoice == 'X') { myChoice = rock; outcome = defeat; }
    else if (chMyChoice == 'Y') { myChoice = paper; outcome = draw; }
    else { myChoice = scissors; outcome = win; }
    totalScore01 += getRockPaperScissorsScore(opponentsChoice, myChoice);
    totalScore02 += getRockPaperScissorsScore(opponentsChoice, getMyChoice(opponentsChoice, outcome));
  }

  std::cout << "Result for task 1: " << totalScore01 << std::endl;
  std::cout << "Result for task 2: " << totalScore02 << std::endl;

  return 0;
}