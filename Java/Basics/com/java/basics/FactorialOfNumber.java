package com.java.basics;

import java.util.Scanner;

/**
 * Factorial Of A Number
 * [Algorithm]
 * Step 1: Start
 * Step 2: Declare variables number, factorial and index (to iterate)
 * Step 3: Initialize variables
 *          factorial <- 1
 *          index <- 1
 * Step 4: Read value of number
 * Step 5: Repeat the steps until index = number
 *      5.1: factorial <- factorial * index
 *      5.2: index <- index + 1
 * Step 6: Display factorial
 * Step 7: Stop
 */
public class FactorialOfNumber
{
    public static void main(String[] args)
    {
        try {
            Scanner num = new Scanner(System.in);
            System.out.println("Enter a integer: ");
            int number = num.nextInt();

            int factorial = 1;
            int index;

            num.close();

            for (index = 1; index <= number; index++)
            {
                factorial = factorial * index;
            }
            System.out.println(number + "! is: " + factorial);


        } catch (Exception exc) {
            System.out.println("You should type a integer! >> " + exc);
        }
    }
}