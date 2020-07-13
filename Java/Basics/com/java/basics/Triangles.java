package com.java.basics;

import java.util.Locale;
import java.util.Scanner;

/**
 * The triangle area is defined by the formula:
 *      area = sqrt(p (p - a) (p - b) (p - c)) -> where "p" stands for Perimeter
 *      and Perimeter -> p = ((a + b + c) / 2)
 */

public class Triangles {

    public static void main(String[] args)
    {
        Locale.setDefault(Locale.CANADA);
        Scanner sides = new Scanner(System.in);
        //For triangle X
        double xA;
        double xB;
        double xC;

        //For triangle Y
        double yA;
        double yB;
        double yC;

        System.out.println("Enter the measures of the triangle X: ");

        xA = sides.nextDouble();
        xB = sides.nextDouble();
        xC = sides.nextDouble();

        System.out.println("Enter the measures of the triangle Y: ");

        yA = sides.nextDouble();
        yB = sides.nextDouble();
        yC = sides.nextDouble();

        //For the perimeter of the triangle X
        double pX = (xA + xB + xC) / 2.0;

        //For the area of the triangle X
        double areaX = Math.sqrt(pX * (pX - xA) * (pX - xB) * (pX - xC));

        //For the perimeter of the triangle Y
        double pY = (yA + yB + yC) / 2.0;

        //For the area of the triangle Y
        double areaY = Math.sqrt(pY * (pY - yA) * (pY - yB) * (pY - yC));

        System.out.printf("Triangle X area: %.4f%n", areaX);

        System.out.printf("Triangle Y area: %.4f%n", areaY);

        //Which of the areas is larger
        if (areaX > areaY)
        {
            System.out.println("The triange X has the larger area.");
        }
        if (areaX < areaY)
        {
            System.out.println("The triangle Y has the larger area.");
        }
        else
        {
            System.out.println("Both triangles, X and Y has the same area.");
        }

        sides.close();

    }
}