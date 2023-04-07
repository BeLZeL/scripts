
// https://connect.ed-diamond.com/GNU-Linux-Magazine/glmf-248/principes-de-l-oriente-objet-en-c-la-genericite

#include <iostream>

template <typename T> // Modèle basé sur le type paramétré T
T maximum (const T& kprNb1, const T& kprNb2) {

    // La fonction générique maximum utilise le paramètre T
    return kprNb1 > kprNb2 ? kprNb1 : kprNb2;
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    int16_t lvMax1 = maximum (5, 56);
    double lvMax2 = maximum (-5.0, 57.6);
    double lvMax3 = maximum<double> (-5, 57.6);
    std::cout << lvMax1 << std::endl;
    std::cout << lvMax2 << std::endl;
    std::cout << lvMax3 << std::endl;
    std::cout << maximum (-5, 56) << std::endl;
    std::cout << maximum<std::string> ("linux", "magazine") << std::endl;
    return 0;
}
