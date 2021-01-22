#include "Players.h"
#include "GameData.h"
#include <iostream>
using namespace std;

Players::Players() {
    plist = new string[SIZE];
    numPlayers = 0;
}

bool Players::addPlayer(string username) {
    if (numPlayers == MAX_PLAYERS) {
        return false;
    }
    plist[numPlayers] = username;
    GameData username;
    numPlayers++;
    return true;
}

bool Players::removePlayer(string username) {
    if (numPlayers == 0) {
        return false;
    }
    numPlayers--;
    return true;
}

void Players::printAllPlayers() {
    cout << "Players:" << endl;
    for (int i = 0; i < numPlayers; i++) {
        cout << plist[i] << endl;
    }
}