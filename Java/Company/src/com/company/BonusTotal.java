package com.company;

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