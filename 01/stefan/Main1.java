package day1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.logging.Logger;

public class Main1 {
    public static void main(String[] args) {
        System.setProperty("java.util.logging.SimpleFormatter.format", "[%1$tT.%1$tL] %5$s %n");
        Logger log = Logger.getGlobal();
        List<String> lines;
        try {
            lines = Files.lines(Path.of("inputs/input1.txt")).toList();
        } catch (IOException e) {
            log.severe("yo wat");
            return;
        }
        int currentMax = 0;
        int currentValue = 0;
        List<Integer> all = new ArrayList<>();
        for (String line : lines) {
            if (line.isEmpty()) {
                if (currentValue > currentMax) currentMax = currentValue;
                all.add(currentValue);
                currentValue = 0;
                continue;
            }
            try {
                int value = Integer.parseInt(line);
                currentValue += value;
            } catch (NumberFormatException e) {

            }
        }
        log.info(currentMax + "");

        all.sort(Comparator.comparingInt(a -> -a));
        int total = all.get(0) + all.get(1) + all.get(2);
        log.info("total: " + total);
    }
}
