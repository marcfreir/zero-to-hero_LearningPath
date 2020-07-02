package com.java.basics;

import java.util.Scanner;

/**
 * Roots of a Quadratic Equation
 * [Algorithm]
 * Step 1: Start
 * Step 2: Declare variables a, b, c, D, x1, x2, rp and ip; //rp stands fo Real Part and ip stands for Imaginary Part
 * Step 3: Calculate Discriminant
 *          D <- b^2 - 4ac
 * Step 4: If D >= 0
 *                 x1 <- (-b+√D)/2a
 *                 x2 <- (-b-√D)/2a
 *                 Display x1 and x2 as roots.
 *         Else
 *                 Calculate real part and imaginary part
 *                 rp <- b/2a
 *                 ip <- √(-D)/2a
 *                 Display rp+j(ip) and rp-j(ip) as roots
 * Step 5: Stop
 */

public class RootsOfAQuadraticEquation
{
    public static void main (String[] args)
    {
        double d;
        double x1;
        double x2;
        double rp;
        double ip;

        Scanner numA = new Scanner(System.in);
        System.out.println("Enter a number for a: ");
        double a = numA.nextDouble();

        Scanner numB = new Scanner(System.in);
        System.out.println("Enter a number for b: ");
        double b = numB.nextDouble();
        
        Scanner numC = new Scanner(System.in);
        System.out.println("Enter a number for c: ");
        double c = numC.nextDouble();

        double base = b;
        int exponent = 2;

        d = Math.pow(base, exponent) - (4 * a * c);

        if (d >= 0)
        {
            x1 = ((-b + Math.sqrt(d)) / 2 * a);
            x2 = ((-b - Math.sqrt(d)) / 2 * a);

            System.out.println("The x1 root is: " + x1);
            System.out.println("The x2 root is: " + x2);
        }
        else
        {
            rp = b / (2 * a);
            ip = (Math.sqrt(-d)) / (2 * a);

            System.out.println("The roots for the real part and imaginary part are: ");
            System.out.println(rp + " + j " + ip);
            System.out.println(rp + " - j " + ip);
        }
    }
    
}