package com.java.basics;

public class IncrementAndDecrementOperator
{
    public static void main(String[] args)
    {
        double number = 8.2;

        System.out.println("The number base is: " + number);
        System.out.println("The increment will occur after: " + number++);
        System.out.println("... now: " + number);
        System.out.println("The increment will occur before: " + ++number);
        System.out.println("The decrement will occur after: : " + number--);
        System.out.println("... now: " + number);
        System.out.println("The decrement will occur before: " + --number);
    }
}