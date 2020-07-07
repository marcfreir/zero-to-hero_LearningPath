package com.company;

public class CEO extends Employee implements Authenticable
{
    public double getBonus()
    {
        return this.salary * 0.35;
    }

    public void requestReports()
    {
        System.out.println("I need the reports!");
    }

    @Override
    public boolean authenticate(int password) {
        // Implemented authentication rule
        return false;
    }
}