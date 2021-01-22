#include "PlayerGames.h"
#include "GameData.h"
#include <iostream>
using namespace std;

GameData::GameData() {
    m_acs = 0;
    m_kills = 0;
    m_deaths = 0;
    m_assists = 0;
    m_roundswon = 0;
    m_roundslost = 0;
}

bool GameData::inputData(int game, int acs, int kills, int deaths, 
                         int assists, int roundswon, int roundslost) {
    m_game = game;
    m_acs = acs;
    m_kills = kills;
    m_deaths = deaths;
    m_assists = assists;
    m_roundswon = roundswon;
    m_roundslost = roundslost;
}

bool GameData::printPlayerData(Players p) {
    
}

bool GameData::printLeaderboard() {

}

int GameData::calculateRating(Players p) {

}