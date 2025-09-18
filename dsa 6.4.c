#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_SIZE 100


char stack[MAX_SIZE];
int top = -1;

void push(char item) {
    if (top >= MAX_SIZE - 1) {
        printf("Stack Overflow\n");
        return;
    }
    stack[++top] = item;
}

char pop() {
    if (top < 0) {
        printf("Stack Underflow\n");
        return '\0';
    }
    return stack[top--];
}

char peek() {
    if (top < 0) {
        return '\0';
    }
    return stack[top];
}


int is_operator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^');
}


int precedence(char ch) {
    switch (ch) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;
    }
    return -1;
}


void infix_to_postfix(char infix[], char postfix[]) {
    int i, j;
    char next;
    
   
    j = 0;
    
    for (i = 0; i < strlen(infix); i++) {
        char ch = infix[i];
        
        if (isalnum(ch)) {
            postfix[j++] = ch;
        } else if (ch == '(') {
            push(ch);
        } else if (ch == ')') {
            while (peek() != '(') {
                postfix[j++] = pop();
            }
            pop(); 
        } else if (is_operator(ch)) {
            while (top != -1 && precedence(peek()) >= precedence(ch) && peek() != '(') {
                postfix[j++] = pop();
            }
            push(ch);
        }
    }
    
    
    while (top != -1) {
        postfix[j++] = pop();
    }
    
    postfix[j] = '\0';
}

int main() {
    char infix[MAX_SIZE], postfix[MAX_SIZE];
    
    printf("Enter an infix expression: ");
    scanf("%s", infix);
    
    infix_to_postfix(infix, postfix);
    
    printf("The postfix expression is: %s\n", postfix);
    
    return 0;
}
