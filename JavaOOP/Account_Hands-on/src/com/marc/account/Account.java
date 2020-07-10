package com.marc.account;

public class Account
{
    private double accountBalance;
    private String holder;
    private int branchCode;
    private int number;
    
    public void withdraw(double value)
    {
        if (accountBalance >= value)
        {
            this.accountBalance -= value;
        }
        else
        {
            throw new InsufficientFundsException(accountBalance);
            //Comment the line above before uncommenting the line below
            /** throw new RuntimeException(); */
        }
    }

    public void deposit(double value)
    {
        this.accountBalance += value;
    }

    //Getters and setters
    public String getHolder()
    {
        return holder;
    }

    public void setHolder(String holder)
    {
        this.holder = holder;
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
        System.out.println(holder);
        System.out.println(branchCode);
        System.out.println(accountBalance);
    }
}
