package com.java.basics;

import java.util.Scanner;

/**
 * Check whether a number entered by the user is prime or not
 * Step 1: Start
 * Step 2: Declare variables number, index and flag.
 * Step 3: Initialize variables
 *          flag <- 1
 *          index <- 2
 * Step 4: Read number from the user.
 * Step 5: Repeat steps until index = (number / 2)
 *      5.1: If remainder of number / index = 0
 *              flag <- true
 *              Go to step 6
 *      5.2 index <- index + 1
 * Step 6: If flag = 0
 *          Display number is not prime
 *         Else
 *          Display number is prime
 * Step 7: Stop
 */
public class PrimeNumber
{

    public static void main(String[] args)
    {
        try
        {
            int index;
            int flag = 1;

            Scanner num = new Scanner(System.in);
            System.out.println("Enter a number to check if it is prime or not: ");
            int number = num.nextInt();

            num.close();

            for (index = 2; index <= (number / 2); index++)
            {
                if (number % index == 0)
                {
                    flag = 0;
                    break;
                }
            }
            if (flag == 0)
            {
                System.out.println(number + " is not prime.");
            }
            else
            {
                System.out.println( number + " is prime.");
            }
            
        }
        catch (Exception exc)
        {
            System.out.print("The input is not valid!" + exc);
        }
    }
}