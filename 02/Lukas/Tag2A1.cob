	IDENTIFICATION DIVISION.
	PROGRAM-ID. AoC_Tag_1.

	ENVIRONMENT DIVISION.

	DATA DIVISION.
	WORKING-STORAGE SECTION.
	77 strategie PIC XXX.
	77 punktzahl PIC 999999.
	

	PROCEDURE DIVISION.
	    ACCEPT strategie
	
	    PERFORM WITH TEST BEFORE UNTIL           
              strategie = SPACE
      * Stein
              IF strategie(3:1) = "X" THEN
                ADD 1 TO punktzahl 
              	IF strategie(1:1) = "A" THEN
                  ADD 3 TO punktzahl 
                END-IF
                IF strategie(1:1) = "B" THEN
                  ADD 0 TO punktzahl 
                END-IF
                IF strategie(1:1) = "C" THEN
                  ADD 6 TO punktzahl 
                END-IF
              END-IF
      * Papier
              IF strategie(3:1) = "Y" THEN
                ADD 2 TO punktzahl 
                IF strategie(1:1) = "A" THEN
                  ADD 6 TO punktzahl 
                END-IF
                IF strategie(1:1) = "B" THEN
                  ADD 3 TO punktzahl 
                END-IF
                IF strategie(1:1) = "C" THEN
                  ADD 0 TO punktzahl 
                END-IF
              END-IF
      * Schere
              IF strategie(3:1) = "Z" THEN
                ADD 3 TO punktzahl 
                IF strategie(1:1) = "A" THEN
                  ADD 0 TO punktzahl 
                END-IF
                IF strategie(1:1) = "B" THEN
                  ADD 6 TO punktzahl 
                END-IF
                IF strategie(1:1) = "C" THEN
                  ADD 3 TO punktzahl 
                END-IF
              END-IF
              ACCEPT strategie
            END-PERFORM 
            display punktzahl
            STOP RUN.
