// https://connect.ed-diamond.com/GNU-Linux-Magazine/glmf-168/c-standard-library-stl-repartons-sur-de-bonnes-bases-suite

#include <iostream>
#include <map>

using namespace std;

int main() {
    // Déclaration d’une map clé de type string,
    // valeur de type string
    map<string,string> Capitales;
    Capitales["France"]     = "Paris";
    Capitales["Belgique"]   = "Bruxelles";
    Capitales["Espagne"]    = "Madrid";
    Capitales["Angleterre"] = "Londres";

    string country;

    //----------------------

    country = "France";
    cout << "Capitale de la " << country << " = "<< Capitales[country] << endl;
    // Capitale de la France = Paris

    //----------------------

    country = "Allemagne";
    cout << "Capitale de l'" << country << " = "<< Capitales[country] << endl;
    // Capitale de l'Allemagne =

    //----------------------

    Capitales["Allemagne"] = "Unknown"; // Insère ou modifie
    Capitales.at("Allemagne")="Berlin"; // Modifie seulement
    cout << "Capitale de l'" << country << " = "<< Capitales[country] << endl;
    // Capitale de l'Allemagne = Berlin

    //----------------------

    if (Capitales.count("Belgique"))
        cout << "Belgique dans la liste" << endl;
    // Belgique dans la liste

    //----------------------

    {
        map<string, string> Capitales_C11{{"France",     "Paris"},
                                          {"Belgique",   "Bruxelles"},
                                          {"Angleterre", "Londres"},
                                          {"Espagne",    "Madrid"},
                                          {"Allemagne",  "Berlin"}};
        if (Capitales == Capitales_C11)
            cout << "Map are Equal" << endl;
    }
    // Map are Equal

    //----------------------

    for ( auto /*map<string,string>::iterator*/ it=Capitales.begin() ; it != Capitales.end() ; ++it )
        cout << "Iterator : " << it->first << " : " << it->second << endl;
    // Iterator : Allemagne : Berlin
    // Iterator : Angleterre : Londres
    // Iterator : Belgique : Bruxelles
    // Iterator : Espagne : Madrid
    // Iterator : France : Paris

    //----------------------

    for ( const auto &it: Capitales )
        cout << "Iterator2 : " << it.first << " : " << it.second << endl;
    // Iterator2 : Allemagne : Berlin
    // Iterator2 : Angleterre : Londres
    // Iterator2 : Belgique : Bruxelles
    // Iterator2 : Espagne : Madrid
    // Iterator2 : France : Paris

    //----------------------

    {
        Capitales.insert({"Italie", "Rome"});
        if (Capitales.count("Italie"))
            cout << "Italie dans la liste." << endl;
        // Italie dans la liste

        auto it = Capitales.find("Italie");
        if (it != Capitales.end()) {
            cout << "Italie dans la liste. Capitale : " << it->second << endl;
            Capitales.erase(it);
        }
        // Italie dans la liste. Capitale : Rome

        if (Capitales.find("Italie") == Capitales.end())
            cout << "Italie n'est plus dans la liste" << endl;
        // Italie n'est plus dans la liste
    }

    return 0;
}
