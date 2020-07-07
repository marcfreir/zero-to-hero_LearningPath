package com.company;

//Applying inheritance from the class Employee to Manager
class Manager extends Employee implements Authenticable
{
    @Override
    public double getBonus()
    {
        //Here the method getBonus will override the original getBonus from Employee
        return this.salary * 0.3;
    }

    public void chargeDelivery()
    {
        System.out.println("Is ready?");
    }

    @Override
    public boolean authenticate(int password) {
        // Implemented authentication rule
        return false;
    }
}