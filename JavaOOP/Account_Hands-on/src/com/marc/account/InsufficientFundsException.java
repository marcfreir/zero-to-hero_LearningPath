package com.marc.account;

public class InsufficientFundsException extends RuntimeException
{
    private final double currentBalance;

    public InsufficientFundsException(double currentBalance)
    {
        super("Insufficient Funds: " + currentBalance);
        this.currentBalance = currentBalance;
    }

    public double getCurrentBalance()
    {
        return currentBalance;
    }
}