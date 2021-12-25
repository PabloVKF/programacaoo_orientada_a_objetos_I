from tkinter import messagebox

from application import Appplication


def on_closing():
    if messagebox.askyesno("Sair", "Você deseja sair?"):
        raise SystemExit


if __name__ == "__main__":
    app = Appplication()
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
