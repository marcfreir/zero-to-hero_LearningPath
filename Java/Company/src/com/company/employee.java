package com.company;

class employee
{
    private String name;
    private double salary;
    int position;
    //1 = assistant; 2 = manager, 3 = ...
    public void setSalary(double salary)
    {
        this.salary = salary;
    }

    public double getBonus()
    {
        if (position == 1)
        {
            return this.salary * 0.2;
        }
        else if ()
    }
}

class testEmployee
{
    public static void main(String[] args)
    {
        employee john = new employee();
        john.setSalary(5000.00);

        System.out.println(john.getBonus());
    }
}
