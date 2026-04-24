#include <stdio.h>
#include <math.h>

void printMenu() {
    printf("\nCalculator Menu:\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    printf("5. Power\n");
    printf("6. Square Root\n");
    printf("7. Factorial\n");
    printf("8. Modulus\n");
    printf("9. Exit\n");
}

long long factorial(int n) {
    if (n < 0) return -1;
    long long res = 1;
    for (int i = 1; i <= n; i++) res *= i;
    return res;
}

int main() {
    int choice;
    double num1, num2, result;
    int int1, int2;
    do {
        printMenu();
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input!\n");
            while (getchar() != '\n');
            continue;
        }
        switch (choice) {
            case 1:
                printf("Enter two numbers: ");
                scanf("%lf %lf", &num1, &num2);
                printf("Result: %.2lf\n", num1 + num2);
                break;
            case 2:
                printf("Enter two numbers: ");
                scanf("%lf %lf", &num1, &num2);
                printf("Result: %.2lf\n", num1 - num2);
                break;
            case 3:
                printf("Enter two numbers: ");
                scanf("%lf %lf", &num1, &num2);
                printf("Result: %.2lf\n", num1 * num2);
                break;
            case 4:
                printf("Enter two numbers: ");
                scanf("%lf %lf", &num1, &num2);
                if (num2 == 0) {
                    printf("Error: Division by zero!\n");
                } else {
                    printf("Result: %.2lf\n", num1 / num2);
                }
                break;
            case 5:
                printf("Enter base and exponent: ");
                scanf("%lf %lf", &num1, &num2);
                printf("Result: %.2lf\n", pow(num1, num2));
                break;
            case 6:
                printf("Enter a number: ");
                scanf("%lf", &num1);
                if (num1 < 0) {
                    printf("Error: Negative input for square root!\n");
                } else {
                    printf("Result: %.2lf\n", sqrt(num1));
                }
                break;
            case 7:
                printf("Enter an integer: ");
                scanf("%d", &int1);
                if (int1 < 0) {
                    printf("Error: Negative input for factorial!\n");
                } else {
                    printf("Result: %lld\n", factorial(int1));
                }
                break;
            case 8:
                printf("Enter two integers: ");
                scanf("%d %d", &int1, &int2);
                if (int2 == 0) {
                    printf("Error: Division by zero in modulus!\n");
                } else {
                    printf("Result: %d\n", int1 % int2);
                }
                break;
            case 9:
                printf("Exiting calculator. Goodbye!\n");
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    } while (choice != 9);
    return 0;
}