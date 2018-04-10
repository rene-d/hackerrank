// https://www.hackerrank.com/challenges/magic-spells/problem

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Spell {
    private:
        string scrollName;
    public:
        Spell(): scrollName("") { }
        Spell(string name): scrollName(name) { }
        virtual ~Spell() { }
        string revealScrollName() {
            return scrollName;
        }
};

class Fireball : public Spell {
    private: int power;
    public:
        Fireball(int power): power(power) { }
        void revealFirepower(){
            cout << "Fireball: " << power << endl;
        }
};

class Frostbite : public Spell {
    private: int power;
    public:
        Frostbite(int power): power(power) { }
        void revealFrostpower(){
            cout << "Frostbite: " << power << endl;
        }
};

class Thunderstorm : public Spell {
    private: int power;
    public:
        Thunderstorm(int power): power(power) { }
        void revealThunderpower(){
            cout << "Thunderstorm: " << power << endl;
        }
};

class Waterbolt : public Spell {
    private: int power;
    public:
        Waterbolt(int power): power(power) { }
        void revealWaterpower(){
            cout << "Waterbolt: " << power << endl;
        }
};

class SpellJournal {
    public:
        static string journal;
        static string read() {
            return journal;
        }
};
string SpellJournal::journal = "";

void counterspell(Spell *spell) {
      /* Enter your code here */
    if (Fireball *s = dynamic_cast<Fireball *>(spell))
    {
        s->revealFirepower();
    }
    else if (Waterbolt *s = dynamic_cast<Waterbolt *>(spell))
    {
        s->revealWaterpower();
    }
    else if (Frostbite *s = dynamic_cast<Frostbite *>(spell))
    {
        s->revealFrostpower();
    }
    else if (Thunderstorm *s = dynamic_cast<Thunderstorm *>(spell))
    {
        s->revealThunderpower();
    }
    else
    {
        auto name = spell->revealScrollName();
        auto journal = SpellJournal::read();

        vector<vector<size_t> > data(name.size() + 1, vector<size_t>(journal.size() + 1, 0));
        for (size_t i = 0; i < name.size(); ++i) {
            for (size_t j = 0; j < journal.size(); ++j) {
                if (name[i] == journal[j])
                    data[i+1][j+1] = data[i][j] + 1;
                else
                    data[i+1][j+1] = max(data[i][j + 1], data[i + 1][j]);
            }
        }
        cout << data[name.size()][journal.size()] << endl;
    }

}

class Wizard {
    public:
        Spell *cast() {
            Spell *spell;
            string s; cin >> s;
            int power; cin >> power;
            if(s == "fire") {
                spell = new Fireball(power);
            }
            else if(s == "frost") {
                spell = new Frostbite(power);
            }
            else if(s == "water") {
                spell = new Waterbolt(power);
            }
            else if(s == "thunder") {
                spell = new Thunderstorm(power);
            }
            else {
                spell = new Spell(s);
                cin >> SpellJournal::journal;
            }
            return spell;
        }
};

int main() {
    int T;
    cin >> T;
    Wizard Arawn;
    while(T--) {
        Spell *spell = Arawn.cast();
        counterspell(spell);
    }
    return 0;
}