// https://connect.ed-diamond.com/GNU-Linux-Magazine/glmf-153/c-11-et-gcc#index_h4_313

#include <condition_variable>
#include <iostream>
#include <thread>
#include <unistd.h>
using namespace std;

mutex Mcv;
condition_variable MyCV;
char MyData='?';

void Consommateur(int id)
{
    unique_lock<mutex> LG(Mcv);
    while(1)
    {
        MyCV.wait(LG);
        cout << id << " => " << MyData << endl;
    }
}

void Producteur()
{
    thread T1(Consommateur, 1);
    thread T2(Consommateur, 2);
    sleep(1);// On laisse les thread se lancer et se mettre en attente sur la condition
    {
        lock_guard<mutex> LG(Mcv);
        MyData='A';
        cout << "notify_one " << MyData << endl;
        MyCV.notify_one();
    }
    sleep(1);
    {
        lock_guard<mutex> LG(Mcv);
        MyData='B';
        cout << "notify_one " << MyData << endl;
        MyCV.notify_one();
    }
    sleep(1);
    {
        lock_guard<mutex> LG(Mcv);
        MyData='C';
        cout << "notify_all " << MyData << endl;
        MyCV.notify_all();
    }
    sleep(1);
    T1.detach();
    T2.detach();
}

int main()
{
    Producteur();
    //notify_one A
    //1=>A
    //notify_one B
    //2=>B
    //notify_all C
    //1=>C
    //2=>C
    return 0;
}