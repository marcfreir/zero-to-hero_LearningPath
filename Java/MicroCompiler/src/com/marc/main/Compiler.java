package com.marc.main;

import java.io.IOException;
import com.marc.exception.ParseException;

/**
 * Compiler
 */
public class Compiler {

    //Look ahead
    private static char lookAhead;

    public static void main(String[] args) throws IOException {
        lookAhead = (char) System.in.read();
        try {
            expression();
        } catch (ParseException exception) {
            /**exception.printStackTrace();*/
            System.err.println(exception.getMessage());
        }
    }

    private static void expression() throws IOException, ParseException {
        System.out.println("movl $" + getNumber() + ", %eax");
    }

    private static char getNumber() throws IOException, ParseException {
        if(!Character.isDigit(lookAhead)) {
            throw new ParseException("Character Expected");
        }
        
        return lookAhead;
        
    }
}