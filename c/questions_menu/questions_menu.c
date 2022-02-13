#include <stdio.h>
#include <math.h>

int main()
{
    char menu;

    printf("Type the option for the question (1, 2, 0, 3, 4 ou 5): \n");
    scanf("%c", &menu);

    switch(menu)
    {
        case '1':
            /*Q1 Start*/

            printf("Question 1 \n");

            double a, b, c, discriminant, root1, root2;
            printf("Enter the coeficient a \n");
            scanf("%lf", &a);
            printf("Enter the coeficient b \n");
            scanf("%lf", &b);
            printf("Enter the coeficient c \n");
            scanf("%lf", &c);

            discriminant = b*b - 4 * a * c;

            // condition for real and different roots
            if (discriminant > 0) {
                root1 = (-b + sqrt(discriminant)) / (2 * a);
                root2 = (-b - sqrt(discriminant)) / (2 * a);
                printf("Root 1 = %.2lf e Root 2 = %.2lf", root1, root2);
            }

            // condition for real and equal roots
            else if (discriminant == 0) {
                root1 = root2 = -b / (2 * a);
                printf("Root 1 = Root 2 = %.2lf;", root1);
            }

            // if the roots are not real
            else {
                printf("For the entered function there is no real roots!");
            }

            /*Q1 End*/
            break;
        case '2':
            /*Q2 Start*/

            printf("Question 2 \n");

            int year;

            printf("Enter a year: \n");
            scanf("%d", &year);

            if (((year % 4 == 0)&&(year % 100 != 0))||((year % 400 == 0)))
            {
                printf("%d is a leap year!", year);
                printf("\nThis year is even!");

            }
            else
            {
                printf("%d is not a leap year!", year);

                if (year % 2 == 0)
                {
                    printf("\nThis year is even!");
                }
                else
                {
                    printf("\nThis year is odd!");
                }
            }

            /*Q2 End*/
            break;
        case '0':
            /*Q0 Start*/

            printf("Question 0 \n");

            int num,revN = 0;
            printf("Enter a integer number: ");
            scanf("%d", &num);

            for (int reminder = num; num!=0; num = (num/10))
            {
                reminder = num % 10;
                revN = revN * 10 + reminder;
            }
            printf("Reversed number = %d", revN);

            /*Q0 End*/
            break;
        case '3':
            /*Q3 Start*/

            printf("Question 3 \n");

            float v, r;

            printf("This program calculate the volume of a sphere from a given radius value.\n");
            printf("\nEnter the radius value: ");
            scanf("%f", &r);

            v = ((4/3.0f)*M_PI*pow(r,3));
            printf("The volume of the sphere is %.4f \n", v);

            /*Q3 End*/
            break;
        case '4':
            /*Q4 Start*/

            printf("Question 4 \n");

            float dividend = (25+16-(115*3)+(sqrt(49))*(78+32)-52*(9-1));
            float divisor = 5;
            float operation = (dividend/divisor);

            printf("Result = %.2lf", operation);

            /*Q4 End*/
            break;
        case '5':
            /*Q5 Start*/

            printf("Question 5 \n");

            int number;
            printf("Type a integer number: ");
            scanf("%d", &number);

            /* num = 154, so 154 is modulus 10 = 4 */
            /* In other words, 154 / 10 = 15 and remainder 4 */
            int units = number % 10; /* Then the value of the variable units = 4 */
            int tens = (number/10) % 10;
            int hundreds = (number/100) % 10;

            printf("The unit for the number %d = %d \n", number, units);
            printf("The ten for the number %d = %d \n", number, tens);
            printf("The hundred for the number %d = %d \n", number, hundreds);

            /*Q5 End*/
            break;
        default:
            printf("Invalid option!");
    }

    return 0;
}
