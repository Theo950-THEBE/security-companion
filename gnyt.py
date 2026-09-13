import tkinter as tk
import random
import threading
import time

try:
    import winsound
except ImportError:
    winsound = None


# ============================================================
# GOODNIGHT // PRANK
# ============================================================

BG = "#050505"
WHITE = "#f2f2f2"
RED = "#ff3344"
GREEN = "#55ff88"


class Prank:
    def __init__(self, root):
        self.root = root
        self.root.title("System Update")
        self.root.geometry("800x450")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.percent = 0

        self.build_screen()

        self.root.after(1000, self.start_loading)

    # --------------------------------------------------------
    # UI
    # --------------------------------------------------------

    def build_screen(self):

        self.title = tk.Label(
            self.root,
            text="INITIALIZING...",
            bg=BG,
            fg=WHITE,
            font=("Consolas", 25, "bold")
        )
        self.title.pack(pady=(90, 20))

        self.status = tk.Label(
            self.root,
            text="Preparing system...",
            bg=BG,
            fg="#777777",
            font=("Consolas", 11)
        )
        self.status.pack(pady=5)

        self.progress_bg = tk.Frame(
            self.root,
            bg="#202020",
            width=600,
            height=20
        )
        self.progress_bg.pack(pady=30)

        self.progress_bg.pack_propagate(False)

        self.progress = tk.Frame(
            self.progress_bg,
            bg=GREEN,
            width=0,
            height=20
        )
        self.progress.pack(
            side="left"
        )

        self.percent_label = tk.Label(
            self.root,
            text="0%",
            bg=BG,
            fg=WHITE,
            font=("Consolas", 18, "bold")
        )
        self.percent_label.pack()

        self.footer = tk.Label(
            self.root,
            text="DO NOT TURN OFF YOUR COMPUTER",
            bg=BG,
            fg="#444444",
            font=("Consolas", 9)
        )
        self.footer.pack(
            side="bottom",
            pady=25
        )

    # --------------------------------------------------------
    # LOADING
    # --------------------------------------------------------

    def start_loading(self):
        self.loading()

    def loading(self):

        if self.percent >= 100:
            self.finish()
            return

        self.percent += 1

        # Make the loading speed accelerate.
        if self.percent < 20:
            delay = 0.35
        elif self.percent < 40:
            delay = 0.18
        elif self.percent < 65:
            delay = 0.09
        elif self.percent < 85:
            delay = 0.045
        else:
            delay = 0.015

        # Random fake system messages
        messages = [
            "Checking system integrity...",
            "Loading core modules...",
            "Initializing secure environment...",
            "Optimizing memory...",
            "Connecting to mainframe...",
            "Analyzing system...",
            "Finalizing installation...",
            "Almost there..."
        ]

        if self.percent % 5 == 0:
            self.status.config(
                text=random.choice(messages)
            )

        width = int(
            600 * self.percent / 100
        )

        self.progress.config(
            width=width
        )

        self.percent_label.config(
            text=f"{self.percent}%"
        )

        self.root.after(
            int(delay * 1000),
            self.loading
        )

    # --------------------------------------------------------
    # FINISH
    # --------------------------------------------------------

    def finish(self):

        self.title.config(
            text="COMPLETE",
            fg=GREEN
        )

        self.status.config(
            text="System initialization successful."
        )

        self.root.after(
            700,
            self.fake_error
        )

    # --------------------------------------------------------
    # FAKE ERROR
    # --------------------------------------------------------

    def fake_error(self):

        self.title.config(
            text="WAIT..."
        )

        self.status.config(
            text="Unexpected event detected.",
            fg=RED
        )

        self.root.after(
            900,
            self.scare
        )

    # --------------------------------------------------------
    # SCARE
    # --------------------------------------------------------

    def scare(self):

        # Clear screen
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(
            bg="#000000"
        )

        self.scare_text = tk.Label(
            self.root,
            text="",
            bg="#000000",
            fg=WHITE,
            font=("Segoe UI", 90, "bold")
        )

        self.scare_text.pack(
            expand=True
        )

        # Play the laugh in another thread
        threading.Thread(
            target=self.laugh,
            daemon=True
        ).start()

        self.root.after(
            200,
            lambda: self.show_middle_finger()
        )

    # --------------------------------------------------------
    # CREEPY LITTLE LAUGH
    # --------------------------------------------------------

    def laugh(self):

        if winsound is None:
            return

        # A deliberately simple creepy "ha-ha-ha"
        notes = [
            (280, 140),
            (230, 130),
            (310, 150),
            (190, 180),
            (260, 120),
            (160, 220)
        ]

        for frequency, duration in notes:

            try:
                winsound.Beep(
                    frequency,
                    duration
                )
            except Exception:
                break

    # --------------------------------------------------------
    # MIDDLE FINGER
    # --------------------------------------------------------

    def show_middle_finger(self):

        self.scare_text.config(
            text="🖕",
            fg=WHITE
        )

        self.root.after(
            1200,
            self.goodnight
        )

    # --------------------------------------------------------
    # GOODNIGHT
    # --------------------------------------------------------

    def goodnight(self):

        self.scare_text.config(
            text="GOODNIGHT.",
            font=("Consolas", 42, "bold"),
            fg=WHITE
        )

        self.root.after(
            2500,
            self.close
        )

    def close(self):
        self.root.destroy()


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = Prank(root)

    root.mainloop()