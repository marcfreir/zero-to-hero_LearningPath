package com.company;

class Employee
{
    private String name;
    protected double salary;

    public void setSalary(double salary)
    {
        this.salary = salary;
    }

    public double getBonus()
    {
        return this.salary * 0.2;
    }
}

//Applying inheritance from the class Employee to Manager
class Manager extends Employee
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
}

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

class BonusTotal
{
    private double total = 0;

    public void add(Employee emp)
    {
        total += emp.getBonus();
    }

    public double getTotal()
    {
        return this.total;
    }
}

class TestEmployee
{
    public static void main(String[] args)
    {
        //Creating a new Employee
        Employee john = new Employee();
        john.setSalary(5000.00);

        System.out.println("The bonus of John is:  " + john.getBonus());

        //Creating a new Manager
        Manager linda = new Manager();
        linda.setSalary(8000.00);
        linda.chargeDelivery();

        System.out.println("The bonus of Linda is: " + linda.getBonus());

        //Creating/Instantiating a new Developer
        Developer timmy = new Developer();
        timmy.setSalary(7000.00);

        System.out.println("The bonus of Timmy is: " + timmy.getBonus());

        //Creating/Instantiating a new BonusTotal
        BonusTotal total = new BonusTotal();
        total.add(john);
        total.add(linda);

        System.out.println(total.getTotal());
    }
}
