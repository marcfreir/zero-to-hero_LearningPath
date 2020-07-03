package com.java.basics;

import java.util.Scanner;

/**
 * Find the Fibonacci Series till term <= 1000
 * [Algorithm]
 * Step 1: Start
 * Step 2: Declare variables first_term, second_term, temp, maxLimit and the number.
 * Step 3: Initialize variables first_term <- 0, second_term <- 1 and limit <- 1000
 * Step 4: Display first_term
 * Step 5: Repeat the steps until second_term <= limit
 *      5.1: temp <- second_term
 *      5.2: second_term <- second_term + first_term
 *      5.3: first_term <- temp
 *      5.4: Display second_term - (second_term - first_term)
 * Step6: Stop
 */

public class FibonacciSeries
{
    public static void main(String[] args)
    {
        try
        {
            int temp;
            int firstTerm = 0;
            int secondTerm = 1;
            int limit = 1000;

            Scanner num = new Scanner(System.in);
            System.out.println("Enter a number up to 1000: ");
            int number = num.nextInt();

            num.close();

            System.out.println("\nThe sequence for the number " + number + " is:\n" + firstTerm);

            if (number <= limit)
            {
            
                do
                {
                    temp = secondTerm;
                    secondTerm = secondTerm + firstTerm;
                    firstTerm = temp;

                    System.out.println(secondTerm - (secondTerm - firstTerm));
                }
                while (secondTerm < number);
            }
            else
            {
                System.out.println("To avoid high memory usage the limit is up 1000!");
            }
        }
        catch (Exception exc)
        {
            System.out.println("The input is not valid >> " + exc);
        }
    }
}