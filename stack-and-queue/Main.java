import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // get the stack size
        System.out.println("Enter the size of the stack: ");
        int stackSize = scanner.nextInt();

        // create a stack
        Stack newStack = new Stack(stackSize);

        // try to pop (peek is the same thing) on an empty stack
        int num;
        // num = newStack.pop();

        // boolean to add items on to stack
        boolean addFull = true;
        int loops;

        if (addFull == true) {
            loops = stackSize;
        } else {
            loops = stackSize + 1;
        }

        // loop to add items to stack
        for (int i = 0; i < loops; i++) {
            newStack.push(i);
            System.out.println("Pushed " + i + " to the stack");
        }

        // test to see which number is on top, should be size
        // int num1 = newStack.peek();
        // System.out.println(num1);

        // test clear, see if popping throws an exception
        newStack.clear();
        // num1 = newStack.pop();
    }
}
