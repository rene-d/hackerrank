
///////////////////////////////////////////////////////////////////////////////
// common for linked list challenges
///////////////////////////////////////////////////////////////////////////////

#include <bits/stdc++.h>

struct Node
{
    int data;
    struct Node *next;
};

Node *init_nodes1(const std::initializer_list<int>&& data)
{
    Node *head = NULL, *prev = NULL;
    for (auto&& b : data)
    {
        Node *node = new Node;
        if (prev) prev->next = node; else head = node;
        prev = node;
        node->data = b;
    }
    if (prev) prev->next = NULL;
    return head;
}

template <typename... T>
Node *init_nodes(T&&... a)
{
    return init_nodes1({std::forward<T>(a)...});
}

Node *read_nodes()
{
    Node *head = NULL, *prev = NULL;
    int n;
    std::cin >> n;
    while (n--)
    {
        Node *node = new Node;
        if (prev) prev->next = node; else head = node;
        prev = node;
        std::cin >> node->data;
    }
    if (prev) prev->next = NULL;
    return head;
}

void free_nodes(Node *head)
{
    for (; head; )
    {
        Node *old = head;
        head = head->next;
        delete old;
    }
}

void print_nodes(Node *head, const char *sep = " ")
{
    for (; head; head = head->next)
    {
        std::cout << head->data << sep;
    }
    std::cout << std::endl;
}

std::string to_str_nodes(Node *head)
{
    std::stringstream ss;
    for (; head; head = head->next)
    {
        ss << head->data;
    }
    return ss.str();
}

std::vector<int>& operator<<(std::vector<int>& v, Node *head)
{
    v.clear();
    for (; head; head = head->next)
    {
        v.push_back(head->data);
    }
    return v;
}