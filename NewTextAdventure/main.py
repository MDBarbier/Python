#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import sqlitefunctions as sqlitefunc
import classes
# ------ FUNCTIONS -------------


def CreatePlayer():
    conn = sqlitefunc.CreateSqliteConnection('test.db')

    if not conn:
        GracefulExit("Could not establish a db connection!")

    name = input("What is your name? ")    
    shortname = input("What is your short name? ")    
    password = input("Enter a password: ")
    player = (name, shortname, password)
    sqlitefunc.InsertPlayer(player)

def GracefulExit(message):
    print("There was a problem: %s" % message)
    print("Program will now exit")
    exit()

def Welcome():
    print("Welcome to the game!")
    prevGame = input("Do you want to load a previous game (y/n)? ")

    if (prevGame == "y"):
        print("loading game...")
        LogInUser()
    elif (prevGame == "n"):
        print("starting new game")
        CreatePlayer()
    else:
        GracefulExit("Unrecognised response!")

def LogInUser():
    usernameToCheck = input("Username: ")
    passwordToCheck = input("Password: ")
    response = sqlitefunc.CheckCredentialsAgainstDatabase(usernameToCheck, passwordToCheck)
    if response:
        print("user logged in OK")
        loggedInPlayer = classes.LoggedInPlayer()
        loggedInPlayer.name = usernameToCheck
        loggedInPlayer.password = passwordToCheck
        GameManager(loggedInPlayer)
    else:
        print("could not log user in, invalid credentials")
        Welcome()

def GameManager(player):
    print("Game manager loaded")
    print("Welcome to your game, {0}".format(player.name))
# ------ Main execution -------------

print("Loading... please wait...")
sqliteVersion = sqlitefunc.CheckSqliteVersion()
print("The sqlite databse version is %s" % sqliteVersion)
print("database connection successful...")

Welcome()

print("Execution finished.")
