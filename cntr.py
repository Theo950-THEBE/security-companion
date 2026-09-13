import tkinter as tk
import random
import time
import math

# ============================================================
# PROJECT: ORBITAL SECURITY SIMULATION
# A cinematic fake-hacking prank.
#
# SAFE:
# - No internet
# - No NASA connection
# - No credential collection
# - No file access
# - No system modification
# ============================================================

root = tk.Tk()
root.title("ORBITAL SECURITY NETWORK")
root.attributes("-fullscreen", True)
root.configure(bg="black")

W = root.winfo_screenwidth()
H = root.winfo_screenheight()

canvas = tk.Canvas(
    root,
    width=W,
    height=H,
    bg="black",
    highlightthickness=0
)
canvas.pack()

# ------------------------------------------------------------
# Emergency exit
# ------------------------------------------------------------

root.bind("<Escape>", lambda e: root.destroy())


# ------------------------------------------------------------
# Utility
# ------------------------------------------------------------

def clear():
    canvas.delete("all")


def center_text(text, y, size=20, color="#00ff66", weight="normal"):
    canvas.create_text(
        W // 2,
        y,
        text=text,
        fill=color,
        font=("Consolas", size, weight)
    )


def beep():
    try:
        import winsound
        winsound.Beep(
            random.randint(500, 900),
            random.randint(40, 100)
        )
    except:
        pass


# ============================================================
# PHASE 1 — BOOT
# ============================================================

boot_lines = [
    "ORBITAL SECURITY NETWORK",
    "INITIALIZING SECURE TERMINAL...",
    "",
    "Loading cryptographic environment...",
    "Loading telemetry interface...",
    "Loading authorization engine...",
    "Loading orbital monitoring subsystem...",
    "",
    "SYSTEM TIME SYNCHRONIZATION ........ OK",
    "SECURE MEMORY INITIALIZATION ........ OK",
    "CRYPTOGRAPHIC MODULE ................ OK",
    "REMOTE TERMINAL ...................... READY",
]

boot_index = 0


def boot():
    global boot_index

    clear()

    canvas.create_text(
        30,
        25,
        text="ORBITAL SECURITY NETWORK // TERMINAL",
        anchor="nw",
        fill="#00ff66",
        font=("Consolas", 19, "bold")
    )

    y = 75

    for line in boot_lines[:boot_index]:
        canvas.create_text(
            30,
            y,
            text=line,
            anchor="nw",
            fill="#00dd55",
            font=("Consolas", 16)
        )
        y += 30

    boot_index += 1

    if boot_index <= len(boot_lines):
        beep()
        root.after(
            random.randint(250, 650),
            boot
        )
    else:
        root.after(1200, identity)


# ============================================================
# PHASE 2 — IDENTITY RECOGNITION
# ============================================================

identity_lines = [
    "IDENTITY RECOGNITION ENGINE",
    "",
    "Analyzing terminal signature...",
    "Generating device fingerprint...",
    "Cross-referencing authorization database...",
    "",
    "DEVICE SIGNATURE: ************",
    "SESSION SIGNATURE: ************",
    "",
    "Checking authorization level...",
    "Checking geographic authorization...",
    "Checking security clearance...",
]

identity_index = 0


def identity():
    global identity_index

    clear()

    center_text(
        "IDENTITY RECOGNITION ENGINE",
        80,
        30,
        "#00ff66",
        "bold"
    )

    y = 140

    for line in identity_lines[:identity_index]:
        canvas.create_text(
            70,
            y,
            text=line,
            anchor="nw",
            fill="#00dd55",
            font=("Consolas", 17)
        )
        y += 32

    identity_index += 1

    if identity_index <= len(identity_lines):
        root.after(
            random.randint(350, 700),
            identity
        )
    else:
        root.after(1000, verification)


# ============================================================
# PHASE 3 — SECURITY VERIFICATION
# ============================================================

verification_progress = 0


def verification():
    global verification_progress

    clear()

    center_text(
        "MULTI-LAYER SECURITY VERIFICATION",
        100,
        27,
        "#00ff66",
        "bold"
    )

    stages = [
        "DEVICE AUTHENTICATION",
        "SESSION AUTHENTICATION",
        "NETWORK AUTHENTICATION",
        "SECURITY CLEARANCE",
        "BIOMETRIC TOKEN",
    ]

    completed = min(
        len(stages),
        verification_progress // 20
    )

    for i, stage in enumerate(stages):

        y = 190 + i * 55

        status = "VERIFIED" if i < completed else "PROCESSING"

        color = "#00ff66" if i < completed else "#888888"

        canvas.create_text(
            150,
            y,
            text=stage,
            anchor="w",
            fill=color,
            font=("Consolas", 17)
        )

        canvas.create_text(
            W - 150,
            y,
            text=status,
            anchor="e",
            fill=color,
            font=("Consolas", 17)
        )

    verification_progress += random.randint(2, 5)

    if verification_progress >= 100:
        root.after(1500, satellite)
    else:
        root.after(150, verification)


# ============================================================
# PHASE 4 — SATELLITE TELEMETRY
# ============================================================

satellite_progress = 0


def satellite():
    global satellite_progress

    clear()

    center_text(
        "ORBITAL TELEMETRY CHANNEL",
        70,
        29,
        "#00ff66",
        "bold"
    )

    center_text(
        "RESTRICTED",
        105,
        15,
        "#ff3333",
        "bold"
    )

    # Fake radar circle
    cx = W // 2
    cy = H // 2 + 30

    canvas.create_oval(
        cx - 180,
        cy - 180,
        cx + 180,
        cy + 180,
        outline="#075f36",
        width=2
    )

    canvas.create_oval(
        cx - 120,
        cy - 120,
        cx + 120,
        cy + 120,
        outline="#075f36"
    )

    canvas.create_line(
        cx - 180,
        cy,
        cx + 180,
        cy,
        fill="#075f36"
    )

    canvas.create_line(
        cx,
        cy - 180,
        cx,
        cy + 180,
        fill="#075f36"
    )

    # Fake moving objects
    for _ in range(7):
        angle = random.random() * math.pi * 2
        radius = random.randint(30, 160)

        x = cx + math.cos(angle) * radius
        y = cy + math.sin(angle) * radius

        canvas.create_oval(
            x - 4,
            y - 4,
            x + 4,
            y + 4,
            fill="#00ff66",
            outline=""
        )

    center_text(
        f"TELEMETRY SYNCHRONIZATION {satellite_progress}%",
        H - 100,
        18,
        "#00ff66"
    )

    satellite_progress += random.randint(3, 7)

    if satellite_progress >= 100:
        root.after(1800, classified)
    else:
        root.after(180, satellite)


# ============================================================
# PHASE 5 — CLASSIFIED ACCESS
# ============================================================

classified_lines = [
    "CLASSIFIED SECURITY ENVIRONMENT",
    "",
    "ACCESS REQUEST RECEIVED",
    "",
    "Authorization token detected.",
    "Security clearance detected.",
    "Secondary verification required.",
    "",
    "Opening restricted environment...",
    "",
    "WARNING:",
    "This terminal is monitored.",
    "",
    "Proceeding...",
]

classified_index = 0


def classified():
    global classified_index

    clear()

    y = 70

    for i, line in enumerate(
        classified_lines[:classified_index]
    ):

        color = "#ff3333" if "WARNING" in line else "#00ff66"

        canvas.create_text(
            50,
            y,
            text=line,
            anchor="nw",
            fill=color,
            font=("Consolas", 19, "bold" if "WARNING" in line else "normal")
        )

        y += 34

    classified_index += 1

    if classified_index <= len(classified_lines):
        beep()
        root.after(
            random.randint(350, 800),
            classified
        )
    else:
        root.after(1800, final_access)


# ============================================================
# PHASE 6 — FINAL ACCESS
# ============================================================

access_progress = 0


def final_access():
    global access_progress

    clear()

    center_text(
        "PRIVATE SECURITY ENVIRONMENT",
        100,
        32,
        "#00ff66",
        "bold"
    )

    center_text(
        "FINAL AUTHORIZATION",
        145,
        18,
        "#888888"
    )

    bar_w = 700
    bar_h = 28

    x1 = W // 2 - bar_w // 2
    y1 = H // 2

    canvas.create_rectangle(
        x1,
        y1,
        x1 + bar_w,
        y1 + bar_h,
        outline="#00ff66",
        width=2
    )

    filled = int(
        bar_w * access_progress / 100
    )

    canvas.create_rectangle(
        x1,
        y1,
        x1 + filled,
        y1 + bar_h,
        fill="#00ff66",
        outline=""
    )

    center_text(
        f"ACCESSING... {access_progress}%",
        y1 + 65,
        18,
        "#00ff66"
    )

    access_progress += random.randint(1, 4)

    if access_progress >= 100:
        root.after(2500, reveal)
    else:
        root.after(170, final_access)


# ============================================================
# PHASE 7 — THE FACE
# ============================================================

def reveal():
    clear()

    canvas.configure(bg="#050505")

    center_text(
        "ACCESS GRANTED",
        75,
        30,
        "#00ff66",
        "bold"
    )

    center_text(
        "PRIVATE SECURITY ENVIRONMENT",
        115,
        15,
        "#666666"
    )

    cx = W // 2
    cy = H // 2

    # Weird face
    canvas.create_oval(
        cx - 190,
        cy - 190,
        cx + 190,
        cy + 190,
        fill="#d0d0d0",
        outline="#555555",
        width=5
    )

    # Eyes
    for ex in (-75, 75):
        canvas.create_oval(
            cx + ex - 35,
            cy - 55,
            cx + ex + 35,
            cy + 35,
            fill="black"
        )

        canvas.create_oval(
            cx + ex - 8,
            cy - 20,
            cx + ex + 8,
            cy - 4,
            fill="#ff2222"
        )

    # Nose
    canvas.create_polygon(
        cx,
        cy - 10,
        cx - 22,
        cy + 65,
        cx + 22,
        cy + 65,
        fill="#999999"
    )

    # Smile
    canvas.create_arc(
        cx - 110,
        cy + 30,
        cx + 110,
        cy + 145,
        start=200,
        extent=140,
        style=tk.ARC,
        outline="black",
        width=9
    )

    center_text(
        "YOU REALLY THOUGHT THIS WAS REAL?",
        cy + 250,
        22,
        "#ff3333",
        "bold"
    )

    root.after(3000, blackout)


# ============================================================
# PHASE 8 — BLACKOUT
# ============================================================

def blackout():
    clear()
    canvas.configure(bg="black")

    # Brief black screen
    root.after(1300, psych)


# ============================================================
# PHASE 9 — PSYCH
# ============================================================

def psych():
    canvas.configure(bg="#050505")

    center_text(
        "PSYCH 💀",
        H // 2 - 70,
        48,
        "#00ff66",
        "bold"
    )

    center_text(
        "THIS WAS A JOKE.",
        H // 2,
        28,
        "white",
        "bold"
    )

    center_text(
        "NO SYSTEM WAS ACCESSED.",
        H // 2 + 55,
        18,
        "#777777"
    )

    center_text(
        "You really thought bro hacked NASA 😭",
        H // 2 + 115,
        17,
        "#888888"
    )

    root.after(5000, root.destroy)


# ============================================================
# START
# ============================================================

root.after(700, boot)
root.mainloop()