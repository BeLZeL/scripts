// https://connect.ed-diamond.com/GNU-Linux-Magazine/glmf-153/c-11-et-gcc
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class personne {
public:
    string Nom;
    string Prenom;
};

bool TriPersonneParNom_CPP98(const personne &G,const personne &D)
{
    return G.Nom<D.Nom;
}

int main()
{
    // sort + C++98
    {
        vector<personne> VP = {{"Stroustrup", "Bjarne"},
                               {"Torvalds",   "Linus"},
                               {"Navarro",    "Laurent"}};
        sort(VP.begin(), VP.end(), TriPersonneParNom_CPP98);
        for ( auto it=VP.begin(); it!=VP.end(); ++it )
            std::cout << "[C++98] " << it->Nom << " : " << it->Prenom << std::endl;
        // [C++98] Navarro : Laurent
        // [C++98] Stroustrup : Bjarne
        // [C++98] Torvalds : Linus
    }

    // sort + lambda C++11
    // https://en.cppreference.com/w/cpp/algorithm/sort
    {
        vector<personne> VP = {{"Stroustrup", "Bjarne"},
                               {"Torvalds",   "Linus"},
                               {"Navarro",    "Laurent"}};
        sort(VP.begin(), VP.end(),[](const personne &G,const personne &D){return G.Nom<D.Nom; });
        for ( const auto& it: VP)
            std::cout << "[C++11] " << it.Nom << " : " << it.Prenom << std::endl;
        // [C++11] Navarro : Laurent
        // [C++11] Stroustrup : Bjarne
        // [C++11] Torvalds : Linus
    }

    // count_if + lambda C++11
    // https://en.cppreference.com/w/cpp/algorithm/count
    {
        vector<personne> VP = {{"Stroustrup", "Bjarne"},
                               {"Torvalds",   "Linus"},
                               {"Navarro",    "Laurent"}};
        cout << "count_if : length(prenom) < length(nom) = " << count_if(VP.begin(), VP.end(),[](const personne &P){return P.Prenom.length()<P.Nom.length(); }) << endl;
        // count_if : length(prenom) < length(nom) = 2

        int x=6;
        cout << "count_if : length(prenom) < " << x << " = " << count_if(VP.begin(), VP.end(),[x](const personne &P){return P.Prenom.length()<x; }) << endl;
        // count_if : length(prenom) < 6 = 1
    }

    return 0;
}
