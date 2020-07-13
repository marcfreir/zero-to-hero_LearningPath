# Triangle OOP

The Herons' Triangle area is defined by the formula:
>     area = √(p (p - a) (p - b) (p - c)) -> where "p" stands for Perimeter

>     and Perimeter -> p = (a + b + c) / 2

#### preview Triangle.java
```java
public class Triangle
{
    //Sides of the triangle
    public double sA;
    public double sB;
    public double sC;
}
```
where e new Triangle is instantiated, getting the attibutes from the class Triangle

>     x = new Triangle()
>     x has sA (side A)
>     x has sB (side B)
>     x has sC (side C)

>     The Perimeter of X is:
>     pX = (x.sA + x.sB + x.sC) / 2

>     The Area of X is:
>     areaX = Math.sqrt(pX * (pX - x.sA) * (pX - x.sB) * (pX - x.sC))


##### Improvements and suggestion are welcome £:D