#include <iostream>
#include <string>

// this is a stack push and pop problem

using namespace std;

class Stack
{

public:
    int top;
    // could possible use a vector to make this more dynamic
    int arr[1000000];

    Stack() { top = -1; }

    void push(int x)
    {
        if (top >= 999999)
        {
            cout << "Stack overflow" << endl;
            return;
        }
        // increment top before index used
        arr[++top] = x;
        cout << "Pushed " << x << " to stack\n";
    }

    int pop()
    {

        if (top < 0)
        {
            cout << "Stack underflow" << endl;
            return -1;
        }
        // decrement top after it is used
        return arr[top--];
    }

    int peek()
    {
        if (top < 0)
        {
            cout << "Stack is empty" << endl;
            return 0;
        }

        return arr[top];
    }

    bool isEmpty()
    {
        return (top < 0);
    }
};
string removeStars(string s)
{
    Stack t;
    string temp = "";

    for (char c : s)
    {
        if (c == '*')
        {
            t.pop();
        }
        else
        {
            t.push((int)c);
        }
    }

    for (int i = 0; i <= t.top; i++)
    {
        temp = temp + (char)t.arr[i];
    }

    return temp;
}
int main()
{
    cout << removeStars("leet**cod*e");
    return 1;
}