#ifndef GAMEDATA_H
#define GAMEDATA_H

#include "PlayerGames.h"

class GameData {
  public:
    GameData();

    bool inputData(int game, int acs, int kills, int deaths, 
                   int assists, int roundswon, int roundslost);

    bool printPlayerData(Players p);

    bool printLeaderboard();

    int calculateRating(Players p);



  private:
    int m_game;
    int m_acs;
    int m_kills;
    int m_deaths;
    int m_assists;
    int m_roundswon;
    int m_roundslost;

};

#endif