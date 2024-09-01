# Dungeons & Dragons Game 🐉⚔️🏰

Welcome to the Dungeons & Dragons project, a Django Rest Framework application designed to manage your D&D campaigns, characters, and game sessions. This project provides a backend system for creating and managing users, characters, game structures, and entire games with integrated gameplay mechanics like dice rolling and difficulty calculations.🧙🏻‍♂️


## Features 🛡️

- **User Authentication & Management**: Register and authenticate users, ensuring only verified users can access certain features🧛.
- **Character Creation & Management**: Create and manage characters with attributes like race, class, hit points, power, wisdom, and dexterity🧜🏽‍♂️🧝🏼‍♀️.
- **Game Session Management**: Create game sessions, assign characters, and manage in-game structures🏹, NPCs🧞‍♀️, and enemies🧟.
- **Automated Structure Setup**: Automatically assign structures (dungeons, palaces, etc.) to a game based on the desired difficulty class (DC)📜.
- **Dice Rolling Utilities**: Built-in utilities for rolling various types of dice🎲, essential for game mechanics💰.


## Installation 🧙🏼

To get started with the D&D Game API, you'll need to clone the repository and install the necessary dependencies.

```
git clone https://github.com/MahsaRah99/Dungeons-Dragons.git
cd Dungeons-Dragons
pip install -r requirements.txt
```
Next, set up your database and run migrations:
```
python manage.py makemigrations
python manage.py migrate
```
Finally, start the development server:
```
python manage.py runserver
```
