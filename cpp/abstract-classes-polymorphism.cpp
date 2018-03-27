#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

#pragma GCC diagnostic ignored "-Wreorder"
#pragma GCC diagnostic ignored "-Wsign-compare"


struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
   
   protected: 
   map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function

};

//---------------------------------------------------------------------------
#include <queue>

class LRUCache : protected Cache
{
    std::queue<Node *>  lru_;
public:
    LRUCache(int capacity)
    {
        cp = capacity;
    }

    virtual ~LRUCache()
    {
        mp.clear();
        while (! lru_.empty())
        {
            Node *node = lru_.front();
            delete node;
            lru_.pop();
        }
    }

    virtual void set(int key, int val) override
    {
        auto i = mp.find(key);
        if (i != mp.end())
        {
            i->second->value = val;
            return;
        }

        Node *node = new Node(key, val);

        if (lru_.size() >= cp)
        {
            Node *node = lru_.front();
            mp.erase(node->key);
            delete node;
            lru_.pop();
        }

        mp[key] = node;
        lru_.push(node);
    }

    virtual int get(int key) override
    {
        auto i = mp.find(key);
        if (i == mp.end()) return -1;
        return i->second->value;
    }
};

//---------------------------------------------------------------------------

int main() {
   int n, capacity,i;
   cin >> n >> capacity;
   LRUCache l(capacity);
   for(i=0;i<n;i++) {
      string command;
      cin >> command;
      if(command == "get") {
         int key;
         cin >> key;
         cout << l.get(key) << endl;
      } 
      else if(command == "set") {
         int key, value;
         cin >> key >> value;
         l.set(key,value);
      }
   }
   return 0;
}

