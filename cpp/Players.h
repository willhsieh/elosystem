#ifndef PLAYERS_H
#define PLAYERS_H

#include "GameData.h"
#include <string>

const int MAX_PLAYERS = 20;

class Players {
  public:
    Players();

    bool addPlayer(string username);

    bool removePlayer(string username);

    void printAllPlayers();


  private:
    string *plist;
    int numPlayers;

};



#endif