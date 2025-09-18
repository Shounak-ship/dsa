#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int open_count = 0;
    int close_count = 0;
    
    printf("Enter a string with parentheses: ");
    scanf("%s", str);
    
   
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == '(') {
            open_count++;
        } else if (str[i] == ')') {
            close_count++;
        }
    }
    
   
    if (open_count == close_count) {
        printf("The number of opening and closing parentheses are equal.\n");
    } else {
        printf("The number of opening and closing parentheses are not equal.\n");
    }
    
    return 0;
}
