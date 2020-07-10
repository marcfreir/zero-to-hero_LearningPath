package com.marc.account;

public class TestException
{

    public static void main(String[] args)
    {
        System.out.println("Starting main...");
        main_1();
        System.out.println("Finishing main...");
    }
    private static void main_1()
    {
        System.out.println("Starting main_1...");
        main_2();
        System.out.println("Finishing main_1...");
    }
    private static void main_2()
    {
        System.out.println("Starting main_2...");
        
        int[] numbers = new int[5];
        for (int index = 0; index < 5; index++)
        {
            numbers[index] = index * 2;
            System.out.println(numbers[index]);
        }
        System.out.println("Finishing main_2...");
    }
}