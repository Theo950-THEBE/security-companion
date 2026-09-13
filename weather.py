import tkinter as tk
import random
import math

# ============================================================
# ANIME WALKER → CARTOON EXPLOSION → WEATHER REPORT
# No external packages required.
# ============================================================

WIDTH = 900
HEIGHT = 550

root = tk.Tk()
root.title("Weather Report")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
root.configure(bg="#101522")

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#8ed6ff",
    highlightthickness=0
)
canvas.pack()

# ------------------------------------------------------------
# State
# ------------------------------------------------------------

girl_x = -100
girl_y = 390
walking = True
exploding = False
weather = False

frame = 0
explosion_frame = 0
particles = []


# ------------------------------------------------------------
# Background
# ------------------------------------------------------------

def draw_background():
    canvas.delete("background")

    # Sky
    canvas.create_rectangle(
        0, 0, WIDTH, HEIGHT,
        fill="#8ed6ff",
        outline="",
        tags="background"
    )

    # Clouds
    for x, y in [(150, 100), (500, 70), (760, 130)]:
        canvas.create_oval(
            x - 45, y - 20,
            x + 45, y + 25,
            fill="white",
            outline="",
            tags="background"
        )
        canvas.create_oval(
            x - 15, y - 40,
            x + 45, y + 25,
            fill="white",
            outline="",
            tags="background"
        )

    # Ground
    canvas.create_rectangle(
        0, 430, WIDTH, HEIGHT,
        fill="#78b84b",
        outline="",
        tags="background"
    )

    canvas.create_line(
        0, 430, WIDTH, 430,
        fill="#4d8c36",
        width=4,
        tags="background"
    )


# ------------------------------------------------------------
# Anime-style cartoon girl
# ------------------------------------------------------------

def draw_girl(x, y, walk_frame):
    canvas.delete("girl")

    # Hair
    canvas.create_oval(
        x - 25, y - 105,
        x + 35, y - 40,
        fill="#35205f",
        outline="#21143d",
        width=3,
        tags="girl"
    )

    # Face
    canvas.create_oval(
        x - 18, y - 90,
        x + 25, y - 45,
        fill="#ffd8bd",
        outline="#9d684e",
        width=2,
        tags="girl"
    )

    # Hair fringe
    canvas.create_polygon(
        x - 20, y - 75,
        x - 5, y - 95,
        x + 5, y - 70,
        x + 15, y - 95,
        x + 28, y - 72,
        fill="#35205f",
        outline="",
        tags="girl"
    )

    # Eyes
    canvas.create_oval(
        x - 9, y - 67,
        x - 3, y - 59,
        fill="black",
        tags="girl"
    )

    canvas.create_oval(
        x + 10, y - 67,
        x + 16, y - 59,
        fill="black",
        tags="girl"
    )

    # Body / shirt
    canvas.create_rectangle(
        x - 25, y - 40,
        x + 30, y + 45,
        fill="#ff77a8",
        outline="#a52e61",
        width=3,
        tags="girl"
    )

    # Arms — alternate while walking
    arm_offset = 12 if walk_frame % 2 == 0 else -12

    canvas.create_line(
        x - 20, y - 25,
        x - 48, y + arm_offset,
        fill="#ffd8bd",
        width=12,
        capstyle="round",
        tags="girl"
    )

    canvas.create_line(
        x + 25, y - 25,
        x + 50, y - arm_offset,
        fill="#ffd8bd",
        width=12,
        capstyle="round",
        tags="girl"
    )

    # Skirt
    canvas.create_polygon(
        x - 32, y + 40,
        x + 38, y + 40,
        x + 48, y + 75,
        x - 45, y + 75,
        fill="#5d6ee8",
        outline="#303c99",
        width=3,
        tags="girl"
    )

    # Legs
    leg_offset = 14 if walk_frame % 2 == 0 else -14

    canvas.create_line(
        x - 15, y + 72,
        x - 15 + leg_offset, y + 125,
        fill="#ffd8bd",
        width=13,
        capstyle="round",
        tags="girl"
    )

    canvas.create_line(
        x + 20, y + 72,
        x + 20 - leg_offset, y + 125,
        fill="#ffd8bd",
        width=13,
        capstyle="round",
        tags="girl"
    )

    # Shoes
    canvas.create_oval(
        x - 35 + leg_offset,
        y + 115,
        x - 2 + leg_offset,
        y + 130,
        fill="#222222",
        tags="girl"
    )

    canvas.create_oval(
        x + 3 - leg_offset,
        y + 115,
        x + 35 - leg_offset,
        y + 130,
        fill="#222222",
        tags="girl"
    )


# ------------------------------------------------------------
# Explosion
# ------------------------------------------------------------

def create_explosion(x, y):
    global particles

    canvas.delete("girl")

    # Big cartoon explosion
    points = []

    for i in range(24):
        angle = (math.pi * 2 / 24) * i
        radius = random.choice([50, 70, 95])

        px = x + math.cos(angle) * radius
        py = y + math.sin(angle) * radius

        points.extend([px, py])

    canvas.create_polygon(
        points,
        fill="#ffb300",
        outline="#ff5a00",
        width=5,
        tags="explosion"
    )

    canvas.create_text(
        x,
        y,
        text="POOF!",
        font=("Arial", 38, "bold"),
        fill="white",
        tags="explosion"
    )

    # Cartoon particles
    particles = []

    for _ in range(35):
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(3, 9)

        particles.append({
            "x": x,
            "y": y,
            "dx": math.cos(angle) * speed,
            "dy": math.sin(angle) * speed,
            "life": random.randint(15, 35)
        })


def animate_explosion():
    global explosion_frame, weather

    canvas.delete("explosion")

    # Recreate explosion at center
    create_explosion(girl_x, girl_y - 20)

    explosion_frame += 1

    if explosion_frame > 12:
        canvas.delete("explosion")
        show_weather()
    else:
        root.after(80, animate_explosion)


# ------------------------------------------------------------
# Weather report
# ------------------------------------------------------------

def show_weather():
    global weather

    weather = True
    canvas.delete("all")

    # News-style background
    canvas.create_rectangle(
        0, 0, WIDTH, HEIGHT,
        fill="#18243a"
    )

    canvas.create_rectangle(
        0, 0, WIDTH, 80,
        fill="#d71920"
    )

    canvas.create_text(
        WIDTH // 2,
        40,
        text="BREAKING WEATHER REPORT",
        fill="white",
        font=("Arial", 30, "bold")
    )

    canvas.create_text(
        WIDTH // 2,
        150,
        text="🌤️  TODAY'S FORECAST",
        fill="white",
        font=("Arial", 32, "bold")
    )

    canvas.create_text(
        WIDTH // 2,
        230,
        text="Sunny with a 100% chance of confusion.",
        fill="#ffe66d",
        font=("Arial", 24, "bold")
    )

    canvas.create_text(
        WIDTH // 2,
        285,
        text="Temperature: 27°C",
        fill="white",
        font=("Arial", 22)
    )

    canvas.create_text(
        WIDTH // 2,
        330,
        text="Wind: 14 km/h",
        fill="white",
        font=("Arial", 22)
    )

    canvas.create_text(
        WIDTH // 2,
        375,
        text="Humidity: Surprisingly normal.",
        fill="white",
        font=("Arial", 22)
    )

    canvas.create_text(
        WIDTH // 2,
        450,
        text="☁️  Reporter status: pretending nothing happened.",
        fill="#b8c7e0",
        font=("Arial", 18, "italic")
    )

    canvas.create_text(
        WIDTH // 2,
        510,
        text="GOODNIGHT.",
        fill="white",
        font=("Arial", 28, "bold")
    )


# ------------------------------------------------------------
# Walking animation
# ------------------------------------------------------------

def walk():
    global girl_x, frame, exploding

    if exploding:
        return

    draw_background()
    draw_girl(girl_x, girl_y, frame)

    girl_x += 5
    frame += 1

    # When she reaches the middle...
    if girl_x >= WIDTH // 2:
        exploding = True
        canvas.delete("girl")
        root.after(300, animate_explosion)
        return

    root.after(45, walk)


# ------------------------------------------------------------
# Start
# ------------------------------------------------------------

draw_background()

canvas.create_text(
    WIDTH // 2,
    30,
    text="LIVE",
    fill="red",
    font=("Arial", 18, "bold")
)

root.after(500, walk)

root.mainloop()