// STACK IMPLEMENTATION USING JAVA
// stack: static array
// size: size of static array
// top: index of top element, initially -1

import java.lang.Exception;

public class Stack {
    private int[] stack;
    private int size;
    private int top;

    public Stack(int size) {
        if (size <= 0) {
            System.out.println("Stack must have size greater than 0");
            throw new IllegalArgumentException("Stack size must be greater than 0");
        }

        this.size = size;
        this.stack = new int[size];
        this.top = -1;
    }

    public boolean isEmpty() {
        return (top == -1);
    }

    public boolean isFull() {
        return (top == (size - 1));
    }

    public void push(int val) {
        if (isFull()) {
            System.out.println("Stack Overflow");
        } else {
            top++;
            stack[top] = val;
        }
    }

    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack Empty, cannot pop");
            throw new RuntimeException("Stack Empty, cannot pop");
        } else {
            int val = stack[top];
            top--;
            return val;
        }
    }

    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack Empty, cannot peek");
            throw new RuntimeException("Stack Empty, cannot peek");
        } else {
            return stack[top];
        }
    }

    public void clear() {
        top = -1;
        stack = new int[size];
    }
};