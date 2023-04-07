// https://connect.ed-diamond.com/GNU-Linux-Magazine/glmf-153/c-11-et-gcc#index_h4_314

#include <iostream>
#include <future>
#include <unistd.h>
using namespace std;

int CalculMult(int valeur,unsigned multiplicateur)
{
    int r = valeur;
    cout << "Ajoute " << valeur << endl;
    while(--multiplicateur)
    {
        sleep(1);
        r += valeur;
        cout << "Ajoute " << valeur << endl;
    }
    return r;
}

int main()
{
    cout << "Je lance le calcul à partir du thread principal." << endl;
    future<int> Resultat = async(launch::async,CalculMult, 6,4 );
    sleep(1);
    cout << "Je fais un truc dans le thread principal." << endl;
    sleep(1);
    cout << "J'ai fini, j'attends le résultat du calcul." << endl;
    cout << "Le résultat est " << Resultat.get() << " !" << endl;
    return 0;

    //Je lance le calcul à partir du thread principal.
    //Ajoute 6
    //Ajoute Je fais un truc dans le thread principal.6
    //
    //Ajoute J'ai fini, j'attends le résultat du calcul.6
    //
    //Le résultat est Ajoute 6
    //24 !
}