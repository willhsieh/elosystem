#include "Elo.h"
#include <iostream>
#include <cassert>
using namespace std;


int main()
{
    Sequence s;

    s.insert(3);
    // s.insert(5);
    // s.insert(2);
    s.dump();

    cout << "Passed all tests" << endl;
}