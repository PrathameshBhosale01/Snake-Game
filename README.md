# Snake Game 🐍

A classic Snake Game implementation built with Python and the Turtle graphics library. This project demonstrates core programming concepts including object-oriented design, event-driven programming, and game development fundamentals.

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Overview

Navigate the snake across the screen to eat food and grow longer. Avoid hitting the walls or the snake's own body. The game tracks your current score and saves your high score for future sessions.

## Features

- **Intuitive Controls**: Smooth keyboard-based snake movement
- **Press Any Key to Start**: Simple game initialization
- **Dynamic Gameplay**: Snake grows as it consumes food
- **Collision Detection**: Automatic game over on wall or self-collision
- **Score Tracking**: Real-time score display with persistent high-score storage
- **Clean UI**: Minimalist interface using Turtle graphics

## Technologies Used

- **Python 3**: Core programming language
- **Turtle Graphics**: Built-in Python library for game rendering
- **Object-Oriented Programming**: Modular, reusable code architecture
- **File I/O**: Persistent high-score storage

## Installation

### Prerequisites

- Python 3.x installed on your system
- No additional dependencies required (Turtle comes with Python)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/PrathameshBhosale01/Snake-Game.git
   
   ```

2. **Navigate to the project directory**
   ```bash
   cd snake-game
   ```

3. **Run the game**
   ```bash
   python main.py
   ```

## How to Play

1. Launch the game by running `main.py`
2. Press any key to start
3. Use arrow keys to control the snake's direction
4. Eat the food (colored circle) to grow and earn points
5. Avoid hitting walls or the snake's own body
6. Try to beat your high score!

## Controls

| Key | Action |
|-----|--------|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |

## Project Structure

```
Snake-Game/
│
├── main.py              # Game initialization and main loop
├── snake.py             # Snake class (movement, growth, collision)
├── food.py              # Food class (positioning and rendering)
├── score_board.py       # Scoreboard class (display and persistence)
└── data.txt             # High score storage file
```

## Code Architecture

The project follows object-oriented design principles with clear separation of concerns:

- **main.py**: Orchestrates the game loop and coordinates between components
- **snake.py**: Manages snake behavior, movement mechanics, and body segments
- **food.py**: Handles food generation and random positioning
- **score_board.py**: Controls score display and high-score persistence
- **data.txt**: Stores the highest score achieved across sessions

## Learning Outcomes

This project provides hands-on experience with:

- **Game Development**: Implementing game loops, state management, and real-time updates
- **Event Handling**: Processing keyboard input and user interactions
- **Object-Oriented Programming**: Creating reusable classes with encapsulation
- **Turtle Graphics**: Building graphical applications with Python's built-in library
- **File Operations**: Reading from and writing to files for data persistence
- **Collision Detection**: Implementing boundary checking and self-collision logic

## Future Enhancements

Potential improvements for the project:

- [ ] Add difficulty levels (speed variations)
- [ ] Implement pause functionality
- [ ] Add sound effects
- [ ] Create a menu system
- [ ] Add obstacles and power-ups
- [ ] Implement multiplayer mode

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by the classic Nokia Snake game
- Built as a learning project to understand Python game development
- Thanks to the Python community for excellent documentation

---

**Enjoy the game and happy coding!** 🎮✨
