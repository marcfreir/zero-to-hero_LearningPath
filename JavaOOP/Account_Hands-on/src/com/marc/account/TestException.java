package com.marc.account;

public class TestException
{

    public static void main(String[] args)
    {
        System.out.println("Starting main...");
        main1();
        System.out.println("Finishing main...");
    }
    private static void main1()
    {
        System.out.println("Starting main1...");
        main2();
        System.out.println("Finishing main1...");
    }
    private static void main2()
    {
        System.out.println("Starting main2...");
        
        int[] numbers = new int[5];
        for (int index = 0; index < 5; index++)
        {
            numbers[index] = index * 2;
            System.out.println(numbers[index]);
        }
        System.out.println("Finishing main2...");
    }
}