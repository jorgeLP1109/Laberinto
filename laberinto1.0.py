from colorama import init, Fore, Back, Style
import os

def draw_maze(maze, player_x, player_y):
    os.system("cls" if os.name == "nt" else "clear")  # Limpia la pantalla

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if x == player_x and y == player_y:
                print(Back.YELLOW + "P", end="")
            elif cell == "#":
                print(Back.WHITE + " ", end="")
            elif cell == ".":
                print(Back.GREEN + " ", end="")
        print(Style.RESET_ALL)  # Restablece los colores al final de cada fila

def main():
    init(autoreset=True)  # Inicializa Colorama

    player_name = input("Ingresa tu nombre: ")
    print(f"Bienvenido, {player_name}!")

    maze = [
        "#########",
        "#P......#",
        "#..######",
        "#..#....#",
        "######..#",
        "#......P#",
        "#########",
    ]

    player_x, player_y = 1, 1

    while True:
        draw_maze(maze, player_x, player_y)
        print("Use las teclas ↑ ↓ ← → para mover el personaje.")

        key = input("Presione 'q' para salir: ")

        if key == "q":
            break
        elif key == "\x1b[A" and maze[player_y - 1][player_x] != "#":
            player_y -= 1
        elif key == "\x1b[B" and maze[player_y + 1][player_x] != "#":
            player_y += 1
        elif key == "\x1b[C" and maze[player_y][player_x + 1] != "#":
            player_x += 1
        elif key == "\x1b[D" and maze[player_y][player_x - 1] != "#":
            player_x -= 1

if __name__ == "__main__":
    main()