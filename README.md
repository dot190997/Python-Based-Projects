# Python-Based-Projects
This repository contains a few personal python-based projects.

Tic-Tac-Toe:
This is a simple GUI-based Tic-Tac-Toe game that can be played versus computer or second player.
It offers a menu bar that allows game reset, new game etc. It can also keep a tab of scores in current session.

Finger Counter:
It uses openCV library.
Using the following, it counts the number of fingers shown to computer's web-cam.
This program uses computer's web camera an captures live image. It then uses the live feed to check the moving entities.
It then removes noise and converts the live feed into gray-scale for better processing. It counts crests and troughs.
Iftrough has an angle less than 105 degrees, it considers it a finger.

Web Crawler:
It uses Beautiful Soups library to fetch information from a webpage's source code. This simple web-crawler extracts links and Book Titles from a website called goodreads.com and stores them in a separate file, namely store2.txt. The web crawler can be modified according to the needs and its extension (commented out part) can also work on nested pages.
