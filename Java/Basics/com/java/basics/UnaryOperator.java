package com.java.basics;

public class UnaryOperator
{
    public static void main(String[] args)
    {
        double number = 8.7;
        boolean flag = false;

        //Here the number will remain the same (because it is already positive)
        System.out.println("+number = " + +number);
        //Here the number will turn positive to negative
        System.out.println("-number = " + -number);
        //Here the number will increase by 1
        System.out.println("++number = " + ++number);
        //Here the number will nagate the negative number
        System.out.println("--number = " + --number);
        //Negate flag value
        System.out.println("!flag = " + !flag);
    }
}