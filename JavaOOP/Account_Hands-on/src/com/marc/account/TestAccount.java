package com.marc.account;

public class TestAccount
{
    public static void main(String[] args)
    {
        //Some random data for Timmy
        Account timmy = new Account();
        timmy.deposit(50.0);
        try
        {
            timmy.withdraw(100.00);
        }
        catch (InsufficientFundsException exc)
        {
            System.out.println("Funds are Insufficient: " + exc.getCurrentBalance());
        }
        catch (RuntimeException exc)
        {
            System.out.println("Any other error!");
        }

        System.out.println("Balance: " + timmy.getAccountBalance());
    }
}
