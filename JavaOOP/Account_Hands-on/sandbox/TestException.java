//package com.marc.account;

public class TestException
{

    public static void main(String[] args)
    {
        //Step 1
        System.out.println("Starting main...");
        //Step 2...
        main_1();
        //Step 7
        System.out.println("Finishing main...");
    }
    private static void main_1()
    {
        //...Step 2
        System.out.println("Starting main_1...");
        //Step 3...
        main_2();
        //Step 6
        System.out.println("Finishing main_1...");
    }
    private static void main_2()
    {
        //...Step 3
        System.out.println("Starting main_2...");
        //Step 4
        int[] numbers = new int[5];
        for (int index = 0; index < 5; index++)
        {
            numbers[index] = index * 2;
            System.out.println(numbers[index]);
        }
        //Step 5
        System.out.println("Finishing main_2...");
    }
}