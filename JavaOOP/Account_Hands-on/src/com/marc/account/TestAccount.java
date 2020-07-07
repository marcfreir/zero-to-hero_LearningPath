package com.marc.account;

public class TestAccount
{
    public static void main(String[] args)
    {
        Account account = new Account("Timmy", 123, 500.42);
        account.setName("Timmy");
        account.print();

        System.out.println("Account name: " + account.getName());
    }
}