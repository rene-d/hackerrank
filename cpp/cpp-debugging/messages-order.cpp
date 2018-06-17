// C++ > Debugging > Cpp messages order
// Implement a software layer over the top of a network, such that sent messages are printed by the recipient in the order they were sent.
//
// https://www.hackerrank.com/challenges/messages-order/problem
// challenge id: 67829
//

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
// (skeliton_head) ----------------------------------------------------------------------


class Message
{
    string text_;
    int seq_ = 0;

  public:
    Message() {}

    Message(const string& text, int seq = 0) : text_(text), seq_(seq)
    {
    }

    const string& get_text() const
    {
        return text_;
    }

    bool operator<(const Message& o) const
    {
        return seq_ < o.seq_;
    }
};

class MessageFactory
{
    int seq_ = 0;

  public:
    MessageFactory() {}

    Message create_message(const string& text)
    {
        return Message(text, seq_++);
    }
};


// (skeliton_tail) ----------------------------------------------------------------------
class Recipient {
public:
    Recipient() {}
    void receive(const Message& msg) {
        messages_.push_back(msg);
    }
    void print_messages() {
        fix_order();
        for (auto& msg : messages_) {
            cout << msg.get_text() << endl;
        }
        messages_.clear();
    }
private:
    void fix_order() {
        sort(messages_.begin(), messages_.end());
    }
    vector<Message> messages_;
};

class Network {
public:
    static void send_messages(vector<Message> messages, Recipient& recipient) {
    // simulates the unpredictable network, where sent messages might arrive in unspecified order
        random_shuffle(messages.begin(), messages.end());
        for (auto msg : messages) {
            recipient.receive(msg);
        }
    }
};



int main() {
    MessageFactory message_factory;
    Recipient recipient;
    vector<Message> messages;
    string text;
    while (getline(cin, text)) {
        messages.push_back(message_factory.create_message(text));
    }
    Network::send_messages(messages, recipient);
    recipient.print_messages();
}
