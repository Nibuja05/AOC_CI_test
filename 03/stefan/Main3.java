package day3;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

public class Main3 {
    public static void main(String[] args) {
        System.setProperty("java.util.logging.SimpleFormatter.format", "[%1$tT.%1$tL] %5$s %n");
        Logger log = Logger.getGlobal();
        log.info("start");
        List<String> lines;
        try {
            lines = Files.lines(Path.of("inputs/input3.txt")).toList();
        } catch (IOException e) {
            log.severe("yo wat");
            return;
        }
        int sumPriority = 0;
        for (String line : lines) {
            String[] compartments = {line.substring(0, line.length() / 2), line.substring(line.length() / 2)};
            for (int i = 0; i < compartments[0].length(); i++) {
                boolean found = false;
                for (int j = 0; j < compartments[1].length(); j++) {
                    if (compartments[0].charAt(i) == (compartments[1].charAt(j))) {
                        sumPriority += getValueOfChar(compartments[0].charAt(i));
                        found = true;
                        break;
                    }
                }
                if (found) break;
            }
        }
        log.info("sum: " + sumPriority);

        int counter = 0;
        sumPriority = 0;
        List<String> currentGroup = new ArrayList<>();
        for (String line : lines) {
            currentGroup.add(line);
            if (counter <= 1) {
                counter++;
            } else {
                boolean found = false;
                for (int i = 0; i < currentGroup.get(0).length() && !found; i++) {
                    for (int j = 0; j < currentGroup.get(1).length() && !found; j++) {
                        for (int k = 0; k < currentGroup.get(2).length() && !found; k++) {
                            if (currentGroup.get(0).charAt(i) == currentGroup.get(1).charAt(j) && currentGroup.get(1).charAt(j) == currentGroup.get(2).charAt(k)) {
                                sumPriority += getValueOfChar(currentGroup.get(0).charAt(i));
                                found = true;
                            }
                        }
                    }
                }

                counter = 0;
                currentGroup = new ArrayList<>();
            }
        }
        log.info("sum: " + sumPriority);
    }

    private static int getValueOfChar(char c) {
        int value = Character.getNumericValue(c) - 9;
        if (Character.isUpperCase(c)) value += 26;
        return value;
    }
}