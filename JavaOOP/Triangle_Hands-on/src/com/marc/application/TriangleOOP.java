package com.marc.application;

import java.util.Locale;
import java.util.Scanner;

import com.marc.triangle.Triangle;

/**
 * The Herons' Triangle area is defined by the formula:
 *      area = sqrt(p (p - a) (p - b) (p - c)) -> where "p" stands for Perimeter
 *      and Perimeter -> p = ((a + b + c) / 2)
 */

public class TriangleOOP {

    public static void main(final String[] args) {
        Locale.setDefault(Locale.CANADA);
        final Scanner sides = new Scanner(System.in);
        // For triangles X and Y
        Triangle x;
        Triangle y;
        x = new Triangle();
        y = new Triangle();

        System.out.println("Enter the measures of the triangle X: ");

        x.sA = sides.nextDouble();
        x.sB = sides.nextDouble();
        x.sC = sides.nextDouble();

        System.out.println("Enter the measures of the triangle Y: ");

        y.sA = sides.nextDouble();
        y.sB = sides.nextDouble();
        y.sC = sides.nextDouble();

        // For the perimeter of the triangle X
        final double pX = (x.sA + x.sB + x.sC) / 2.0;

        // For the area of the triangle X
        final double areaX = Math.sqrt(pX * (pX - x.sA) * (pX - x.sB) * (pX - x.sC));

        // For the perimeter of the triangle Y
        final double pY = (y.sA + y.sB + y.sC) / 2.0;

        // For the area of the triangle Y
        final double areaY = Math.sqrt(pY * (pY - y.sA) * (pY - y.sB) * (pY - y.sC));

        /**sides.close();*/

        /** System.out.printf("Triangle X area: %.8f%n", areaX); */
        System.out.println("Triangle X area: " + areaX);

        /** System.out.printf("Triangle Y area: %.8f%n", areaY); */
        System.out.println("Triangle Y area: " + areaY);

        // Which of the areas is larger
        try {
            if (areaX > areaY) {
                System.out.println("The triange X has the larger area.");
            }
            if (areaX < areaY) {
                System.out.println("The triangle Y has the larger area.");
            }
            if (areaX == areaY) {
                System.out.println("Both triangles, X and Y has the same area.");
            }
        } catch (final Exception exc)
        {
            System.out.println("Invalid input -> " + exc);
        }

        sides.close();

    }
}