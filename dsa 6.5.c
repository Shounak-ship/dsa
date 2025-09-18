#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX_SIZE 100


int stack[MAX_SIZE];
int top = -1;

void push(int item) {
    if (top >= MAX_SIZE - 1) {
        printf("Stack Overflow\n");
        return;
    }
    stack[++top] = item;
}

int pop() {
    if (top < 0) {
        printf("Stack Underflow\n");
        return -1;
    }
    return stack[top--];
}

int main() {
    char exp[MAX_SIZE];
    int op1, op2, result,i;
    
    printf("Enter a postfix expression: ");
    scanf("%s", exp);

    for (i = 0; i < strlen(exp); i++) {
        char ch = exp[i];

        if (isdigit(ch)) {
            push(ch - '0'); 
        } else {
            op2 = pop();
            op1 = pop();
            
            switch (ch) {
                case '+':
                    result = op1 + op2;
                    break;
                case '-':
                    result = op1 - op2;
                    break;
                case '*':
                    result = op1 * op2;
                    break;
                case '/':
                    result = op1 / op2;
                    break;
                default:
                    printf("Invalid operator: %c\n", ch);
                    return 1;
            }
            push(result);
        }
    }

    if (top == 0) {
        printf("Result: %d\n", pop());
    } else {
        printf("Invalid expression\n");
    }

    return 0;
}
