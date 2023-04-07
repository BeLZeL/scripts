// https://connect.ed-diamond.com/GNU-Linux-Magazine/glmf-168/c-standard-library-stl-repartons-sur-de-bonnes-bases-suite

#include <iostream>
#include <map>
using namespace std;

int main() {
    multimap<string,string> Villes;

    Villes.insert(pair<string,string>("France","Paris"));
    Villes.insert(pair<string,string>("France","Toulouse"));

    Villes.insert(pair<string,string>("Espagne","Madrid"));
    Villes.insert(pair<string,string>("Espagne","Barcelonne"));

    Villes.insert(pair<string,string>("Italie","Rome"));
    Villes.insert(pair<string,string>("Italie","Naples"));

    //----------------------

    multimap<string,string>::iterator it;
    for (it=Villes.begin(); it!=Villes.end(); it++)
        cout << it->first << " : " << it->second << endl;
    // Espagne : Madrid
    // Espagne : Barcelonne
    // France : Paris
    // France : Toulouse
    // Italie : Rome
    // Italie : Naples

    //----------------------

    cout << "Il y a " << Villes.count("France") << " villes en France" << endl;
    // Il y a 2 villes en France

    //----------------------

    for (it=Villes.lower_bound("France"); it!=Villes.upper_bound("France"); it++)
        cout << "(bound)En France il y a " << it->second<< endl;
    // (bound)En France il y a Paris
    // (bound)En France il y a Toulouse

    //----------------------

    it=Villes.find("France");
    if (it!=Villes.end())
        for (; it!=Villes.upper_bound("France"); it++)
            cout << "(bound2)En France il y a " << it->second<< endl;
    // (bound2)En France il y a Paris
    // (bound2)En France il y a Toulouse

    //----------------------

    pair<multimap<string,string>::iterator,multimap<string,string>::iterator> R;
    R=Villes.equal_range("France");
    for (it=R.first; it!=R.second; it++)
        cout << "(equal) En France il y a " << it->second<< endl;
    // (equal) En France il y a Paris
    // (equal) En France il y a Toulouse

    return 0;
}
