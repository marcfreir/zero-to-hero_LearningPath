package com.company;

abstract class Employee
{
    private String name;
    protected double salary;

    public void setSalary(double salary)
    {
        this.salary = salary;
    }

    public abstract double getBonus();

    public String getName()
    {
        return name;
    }
}