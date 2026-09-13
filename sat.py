import tkinter as tk
from tkinter import ttk
import random
import time
import math

# ============================================================
# MISSION CONTROL v0.1
# Local aerospace/cybersecurity simulation
# ============================================================

root = tk.Tk()
root.title("MISSION CONTROL // ORBITAL SYSTEM")
root.geometry("1100x700")
root.configure(bg="#07100d")

# ------------------------------------------------------------
# COLORS
# ------------------------------------------------------------

BG = "#07100d"
PANEL = "#0c1914"
GREEN = "#00ff88"
DIM_GREEN = "#3c9f72"
RED = "#ff4444"
YELLOW = "#ffd166"
WHITE = "#d8fff0"
GRAY = "#719084"

# ------------------------------------------------------------
# SIMULATED SATELLITE STATE
# ------------------------------------------------------------

satellite = {
    "name": "ORBITAL-01",
    "altitude": 408.2,
    "speed": 7.66,
    "temperature": 21.4,
    "battery": 94.0,
    "signal": 98.0,
    "latitude": 24.7136,
    "longitude": 46.6753,
    "status": "NOMINAL",
}

security_events = [
    "Telemetry packet received",
    "Ground station heartbeat OK",
    "Authentication service online",
    "Encryption channel verified",
]

# ------------------------------------------------------------
# MAIN FRAME
# ------------------------------------------------------------

main = tk.Frame(root, bg=BG)
main.pack(fill="both", expand=True)

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------

header = tk.Frame(main, bg=PANEL, height=70)
header.pack(fill="x")

tk.Label(
    header,
    text="MISSION CONTROL",
    fg=GREEN,
    bg=PANEL,
    font=("Consolas", 24, "bold")
).pack(side="left", padx=25, pady=18)

tk.Label(
    header,
    text="ORBITAL SYSTEM // LOCAL SIMULATION",
    fg=GRAY,
    bg=PANEL,
    font=("Consolas", 11)
).pack(side="right", padx=25)


# ------------------------------------------------------------
# LEFT SIDEBAR
# ------------------------------------------------------------

sidebar = tk.Frame(main, bg=PANEL, width=210)
sidebar.pack(side="left", fill="y")

tk.Label(
    sidebar,
    text="SYSTEMS",
    fg=GRAY,
    bg=PANEL,
    font=("Consolas", 11, "bold")
).pack(pady=(25, 10))

systems = [
    "SATELLITE",
    "TELEMETRY",
    "GROUND STATION",
    "SECURITY",
    "MISSION LOG",
]

for system in systems:
    tk.Label(
        sidebar,
        text="●  " + system,
        fg=GREEN,
        bg=PANEL,
        anchor="w",
        font=("Consolas", 11)
    ).pack(fill="x", padx=20, pady=8)


# ------------------------------------------------------------
# CONTENT AREA
# ------------------------------------------------------------

content = tk.Frame(main, bg=BG)
content.pack(side="left", fill="both", expand=True)


# ------------------------------------------------------------
# STATUS BAR
# ------------------------------------------------------------

status_frame = tk.Frame(content, bg=BG)
status_frame.pack(fill="x", padx=20, pady=15)

tk.Label(
    status_frame,
    text="SYSTEM STATUS",
    fg=GRAY,
    bg=BG,
    font=("Consolas", 10)
).pack(side="left")

status_label = tk.Label(
    status_frame,
    text="● NOMINAL",
    fg=GREEN,
    bg=BG,
    font=("Consolas", 11, "bold")
)

status_label.pack(side="left", padx=15)


# ------------------------------------------------------------
# TELEMETRY PANEL
# ------------------------------------------------------------

telemetry = tk.LabelFrame(
    content,
    text="  LIVE TELEMETRY  ",
    fg=GREEN,
    bg=BG,
    bd=1,
    relief="solid",
    font=("Consolas", 11, "bold")
)

telemetry.pack(
    fill="x",
    padx=20,
    pady=10
)

telemetry_labels = {}

telemetry_items = [
    ("ALTITUDE", "altitude", "km"),
    ("VELOCITY", "speed", "km/s"),
    ("TEMPERATURE", "temperature", "°C"),
    ("BATTERY", "battery", "%"),
    ("SIGNAL", "signal", "%"),
    ("LATITUDE", "latitude", "°"),
    ("LONGITUDE", "longitude", "°"),
]

for i, (label, key, unit) in enumerate(telemetry_items):

    box = tk.Frame(
        telemetry,
        bg=PANEL,
        padx=15,
        pady=10
    )

    box.grid(
        row=i // 4,
        column=i % 4,
        padx=8,
        pady=8,
        sticky="ew"
    )

    tk.Label(
        box,
        text=label,
        fg=GRAY,
        bg=PANEL,
        font=("Consolas", 9)
    ).pack()

    value = tk.Label(
        box,
        text="--",
        fg=GREEN,
        bg=PANEL,
        font=("Consolas", 16, "bold")
    )

    value.pack()

    telemetry_labels[key] = (value, unit)

for i in range(4):
    telemetry.columnconfigure(i, weight=1)


# ------------------------------------------------------------
# LOWER PANELS
# ------------------------------------------------------------

lower = tk.Frame(content, bg=BG)
lower.pack(fill="both", expand=True, padx=20, pady=10)

# ------------------------------------------------------------
# SECURITY PANEL
# ------------------------------------------------------------

security = tk.LabelFrame(
    lower,
    text="  SECURITY MONITOR  ",
    fg=GREEN,
    bg=BG,
    font=("Consolas", 11, "bold")
)

security.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 10)
)

security_text = tk.Text(
    security,
    bg="#030806",
    fg=GREEN,
    insertbackground=GREEN,
    font=("Consolas", 10),
    bd=0,
    height=15
)

security_text.pack(
    fill="both",
    expand=True,
    padx=8,
    pady=8
)

security_text.insert(
    "end",
    "[SECURITY] Monitoring started...\n"
)


# ------------------------------------------------------------
# MISSION LOG
# ------------------------------------------------------------

mission = tk.LabelFrame(
    lower,
    text="  MISSION LOG  ",
    fg=GREEN,
    bg=BG,
    font=("Consolas", 11, "bold")
)

mission.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(10, 0)
)

mission_text = tk.Text(
    mission,
    bg="#030806",
    fg=WHITE,
    font=("Consolas", 10),
    bd=0,
    height=15
)

mission_text.pack(
    fill="both",
    expand=True,
    padx=8,
    pady=8
)


# ------------------------------------------------------------
# LOGGING
# ------------------------------------------------------------

def log_security(message):

    timestamp = time.strftime("%H:%M:%S")

    security_text.insert(
        "end",
        f"[{timestamp}] {message}\n"
    )

    security_text.see("end")


def log_mission(message):

    timestamp = time.strftime("%H:%M:%S")

    mission_text.insert(
        "end",
        f"[{timestamp}] {message}\n"
    )

    mission_text.see("end")


# ------------------------------------------------------------
# TELEMETRY SIMULATION
# ------------------------------------------------------------

def update_telemetry():

    # Small realistic changes
    satellite["altitude"] += random.uniform(-0.08, 0.08)

    satellite["speed"] += random.uniform(-0.01, 0.01)

    satellite["temperature"] += random.uniform(-0.2, 0.2)

    satellite["battery"] -= random.uniform(0.005, 0.03)

    satellite["signal"] += random.uniform(-0.3, 0.3)

    satellite["signal"] = max(
        80,
        min(100, satellite["signal"])
    )

    # Update UI
    for key, (label, unit) in telemetry_labels.items():

        value = satellite[key]

        if isinstance(value, float):
            display = f"{value:.2f} {unit}"
        else:
            display = f"{value} {unit}"

        label.config(text=display)

    root.after(1000, update_telemetry)


# ------------------------------------------------------------
# SECURITY EVENTS
# ------------------------------------------------------------

def security_loop():

    event = random.choice(security_events)

    log_security(event)

    root.after(
        random.randint(2000, 5000),
        security_loop
    )


# ------------------------------------------------------------
# MISSION EVENTS
# ------------------------------------------------------------

def mission_loop():

    events = [
        "Orbital position calculated",
        "Telemetry synchronization complete",
        "Ground station connection stable",
        "Navigation solution updated",
        "Satellite clock synchronized",
        "Environmental sensors responding",
    ]

    log_mission(random.choice(events))

    root.after(
        random.randint(3000, 6000),
        mission_loop
    )


# ------------------------------------------------------------
# STARTUP
# ------------------------------------------------------------

log_mission("MISSION CONTROL INITIALIZED")
log_mission("Loading ORBITAL-01...")
log_mission("Telemetry channel established")
log_mission("System operating in simulation mode")

update_telemetry()
security_loop()
mission_loop()

root.mainloop()