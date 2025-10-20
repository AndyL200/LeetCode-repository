#include <vector>
#include <unordered_set>
using namespace std;

class Solution {

private:
template <typename T>
class Deque
{  
private:
    int front;
    int end;
    vector<T> container;
    int size;
    int capacity;
public:
    Deque(int cap = 10) : front(0), end(0), size(0), capacity(cap) {
        container.resize(capacity);
    }
    Deque(T item) : front(0), end(0), size(0), capacity(10) {
        container.resize(10);
        push_back(item);
    }
    void push(T item)
    {
        if(size == capacity)
        {
            resize();
        }
        //keep the front positive
        front = (front - 1 + capacity) % capacity;
        container[front] = item;
        size++;
    }
    void push_back(T item)
    {
        if(size == capacity)
        {
            resize();
        }
        container[end] = item;
        end = (end+1) % capacity;
        size++;
    }

    T popleft()
    {
        if(size == 0)
        {
            throw runtime_error("Deque empty");
        }
        T item = container[front];
        front = (front + 1) % capacity;
        size--;
        return item;
    }
    T pop()
    {
        if(size == 0)
        {
            throw runtime_error("Deque empty");
        }
        end = (end-1+capacity)%capacity;
        T item = container[end];  
        size--;
        return item;
    }
    bool empty(){
        return size == 0;
    }
    private:
        void resize()
        {
            //new array printed front to back
            vector<T> newContainer = vector<T>(container.size() * 2);
            for(int i = 0; i < size; i++)
            {
                newContainer[i] = container[(front + i) % capacity];
            }
            container = newContainer;
            front = 0;
            end = size;
            capacity *= 2;
        }
};
public:
    string lexicoComp(string s1, string s2){
       return s1 < s2 ? s1 : s2;
    }
    string findLexSmallestString(string s, int a, int b) {
        //bfs
        unordered_set<string> u;
        Deque<string> q(s);
        string smallest = s;

        while(!q.empty()){
            string curr = q.popleft();
            if(u.find(curr) != u.end())
            {
                continue;
            }
            u.insert(curr);

            smallest = lexicoComp(curr, smallest);

            //op1
            string t = curr;
            for(int i = 1; i < curr.size(); i+=2){
                t[i] = ((curr[i] - '0' + a) % 10) + '0'; 
            }
            q.push_back(t);
            //op2
            string t2 = curr.substr(b) + curr.substr(0, b);
            q.push_back(t2);
            
        }


        return smallest;
    }
};