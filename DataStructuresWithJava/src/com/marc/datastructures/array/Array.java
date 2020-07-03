package com.marc.datastructures.array;

public class Array
{
    private String[] elements;

    public Array(int capacity)
    {
        this.elements = new String[capacity];
    }

    public void addElement(String element)
    {
        for (int index = 0; index < this.elements.length; index++)
        {
            if (this.elements[index] == null)
            {
                this.elements[index] = element;
            }
        }
    }
}