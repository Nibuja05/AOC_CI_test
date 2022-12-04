package day2;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

public class Main2 {
    public static void main(String[] args) {
        System.setProperty("java.util.logging.SimpleFormatter.format", "[%1$tT.%1$tL] %5$s %n");
        Logger log = Logger.getGlobal();
        log.info("start");
        List<String> lines;
        try {
            lines = Files.lines(Path.of("inputs/input2.txt")).toList();
        } catch (IOException e) {
            log.severe("yo wat");
            return;
        }
        List<String[]> games = new ArrayList<>();
        lines.forEach(s -> games.add(s.split(" ")));

        int myScore = 0;
        for (String[] game : games) {
            if (game[1].equals("X")) { //rock
                myScore++;
                switch (game[0]) {
                    case "A" -> myScore += 3;
                    case "C" -> myScore += 6;
                }
            } else if (game[1].equals("Y")) { //paper
                myScore += 2;
                switch (game[0]) {
                    case "A" -> myScore += 6;
                    case "B" -> myScore += 3;
                }
            } else if (game[1].equals("Z")) { //scissor
                myScore += 3;
                switch (game[0]) {
                    case "B" -> myScore += 6;
                    case "C" -> myScore += 3;
                }
            }
        }
        log.info("myScore: " + myScore);

        //round two
        myScore = 0;
        for (String[] game : games) {
            if (game[1].equals("X")) { //I loose
                switch (game[0]) {
                    case "A" -> myScore += 3;
                    case "B" -> myScore += 1;
                    case "C" -> myScore += 2;
                }
            } else if (game[1].equals("Y")) { //draw
                myScore += 3;
                switch (game[0]) {
                    case "A" -> myScore += 1;
                    case "B" -> myScore += 2;
                    case "C" -> myScore += 3;
                }
            } else if (game[1].equals("Z")) { //I win
                myScore += 6;
                switch (game[0]) {
                    case "A" -> myScore += 2;
                    case "B" -> myScore += 3;
                    case "C" -> myScore += 1;
                }
            }
        }
        log.info("myScore2: " + myScore);
    }

}
