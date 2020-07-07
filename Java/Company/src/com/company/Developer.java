package com.company;

//Applying inheritance from the class Employee to Developer
class Developer extends Employee
{
    @Override
    public double getBonus()
    {
        //Here the method getBonus will override the original getBonus from Employee
        return this.salary * 0.25;
    }
}