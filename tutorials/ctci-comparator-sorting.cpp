// Sorting: Comparator
// Write a Comparator for sorting elements in an array.
//
// https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

struct Player {
    string name;
    int score;
};
// (skeliton_head) ----------------------------------------------------------------------


vector<Player> comparator(vector<Player> players) {

    std::sort(players.begin(), players.end(),
              [](const Player& p1, const Player& p2) -> bool
              {
                  if (p1.score > p2.score) return true;
                  if (p1.score == p2.score) return p1.name < p2.name;
                  return false;
              }
             );

    return players;
}


// (skeliton_tail) ----------------------------------------------------------------------
int main() {

    int n;
    cin >> n;
    vector< Player > players;
    string name;
    int score;
    for(int i = 0; i < n; i++){
        cin >> name >> score;
        Player p1;
        p1.name = name, p1.score = score;
        players.push_back(p1);
    }

    vector<Player > answer = comparator(players);
    for(int i = 0; i < answer.size(); i++) {
        cout << answer[i].name << " " << answer[i].score << endl;
    }
    return 0;
}
