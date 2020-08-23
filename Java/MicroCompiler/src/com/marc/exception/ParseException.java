package com.marc.exception;

public class ParseException extends Exception {

    /**
     *
     */
    private static final long serialVersionUID = 1L;
    
    public ParseException(String reason) {
        super(reason);
    }
}