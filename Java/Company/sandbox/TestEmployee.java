//package com.company;

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