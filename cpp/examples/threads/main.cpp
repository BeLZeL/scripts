#include <iostream>
#include <thread>
#include <chrono>
#include <vector>
#include <mutex>

std::vector<std::mutex> mtx{2};

void fetch(std::string delay, int num_arg)
{
    try
    {
        const int delay_to_int = std::stoi(delay, nullptr);

        std::string space = ( num_arg % 2 == 0 ? "" : "        " );

        mtx[delay_to_int % 2].lock();
        std::cout << space << "[arg n°" << num_arg << "] >>> starts and needs " << delay << " second(s)." << std::endl;
        std::this_thread::sleep_for(std::chrono::duration<int,std::milli>(delay_to_int * 1000));
        std::cout << space << "[arg n°" << num_arg << "] <<< waited for " << delay << " second(s)." << std::endl;
        mtx[delay_to_int % 2].unlock();
    }
    catch(std::invalid_argument const& ex)
    {
        std::cout << "std::invalid_argument::what(): " << ex.what() << '\n';
    }
    catch(std::out_of_range const& ex)
    {
        std::cout << "std::out_of_range::what(): " << ex.what() << '\n';
    }

    return;
}

// Arguments : 4 2 5 1 3
int main(int argc, char **argv) {
    if (argc < 2) return 0;

    std::cout << "Start" << std::endl;

    std::vector<std::thread> threads;
    for (int i=1; i<argc; ++i) {
        threads.push_back(std::thread(fetch, argv[i], i));
    }
    for(std::size_t th = 0; th < threads.size(); ++th) {
        threads[th].join();
    }

    std::cout << "End" << std::endl;

    //Start
    //        [arg n°1] >>> starts and needs 4 second(s).
    //[arg n°4] >>> starts and needs 1 second(s).
    //[arg n°4] <<< waited for 1 second(s).
    //        [arg n°3] >>> starts and needs 5 second(s).
    //        [arg n°1] <<< waited for 4 second(s).
    //[arg n°2] >>> starts and needs 2 second(s).
    //[arg n°2] <<< waited for 2 second(s).
    //        [arg n°3] <<< waited for 5 second(s).
    //        [arg n°5] >>> starts and needs 3 second(s).
    //        [arg n°5] <<< waited for 3 second(s).
    //End

    return 0;
}
