package com.marc.account;

public class Account
{
    private double accountBalance;
    private String name;
    private int branchCode;

    //Constructor 
    public Account(String name, int branchCode, double accountBalance)
    {
        this.name = name;
        this.branchCode = branchCode;
        this.accountBalance = accountBalance;
    }

    //Getters and setters
    public String getName()
    {
        return name;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public int getBranchCode()
    {
        return branchCode;
    }

    public void setBranchCode(int branchCode)
    {
        this.branchCode = branchCode;
    }

    public double getAccountBalance()
    {
        return accountBalance;
    }
    
    //Print data
    public void print()
    {
        System.out.println(name);
        System.out.println(branchCode);
        System.out.println(accountBalance);
    }
}
