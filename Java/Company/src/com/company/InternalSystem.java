package com.company;

public class InternalSystem
{
    public void authenticate(Authenticable authEmp)
    {
        int password = 1234;

        if (authEmp.authenticate(password) == true)
        {
            System.out.println("Welcome!");
        }
        else
        {
            System.out.println("Incorrect Password!");
        }
    }
    
}