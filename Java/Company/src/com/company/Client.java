package com.company;

public class Client implements Authenticable
{
    
    private String name;
    private String address;

    @Override
    public boolean authenticate(int password) {
        // Implemented authentication rule
        return false;
    }
}