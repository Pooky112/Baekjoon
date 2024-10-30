#include <stdio.h>
#include <string.h>

#define MAX 10000

typedef struct {
    int data[MAX];
    int top;
} Stack;

void init(Stack* stack){
    stack->top = -1;
}

void push(Stack* stack, int x){
    if (stack->top < MAX - 1){
        stack -> data[++(stack->top)] = x;
    }
}

int pop(Stack* stack){
    if (stack->top == -1) return -1;
    return stack->data[(stack->top)--];
}

int size(Stack* stack){
    return stack->top + 1;
}

int empty(Stack* stack){
    return stack->top == -1 ? 1 : 0;
}

int top(Stack* stack){
    if (stack->top == - 1) return -1;
    return stack->data[stack->top];
}

int main(void)
{
    int n;
    scanf("%d", &n);

    Stack stack;
    init(&stack);

    char command[10];
    int x;
    for(int i =0; i < n; i++) {
        scanf("%s", command);

        if (strcmp(command, "push") == 0) {
            scanf("%d", &x);
            push(&stack, x);
        } else if (strcmp(command, "pop") == 0) {
            printf("%d\n", pop(&stack));
        } else if (strcmp(command, "size") == 0) {
            printf("%d\n", size(&stack));
        } else if (strcmp(command, "empty") == 0) {
            printf("%d\n",empty(&stack));
        } else if (strcmp(command, "top") == 0) {
            printf("%d\n",top(&stack));
        }
    }
    return 0;
}
