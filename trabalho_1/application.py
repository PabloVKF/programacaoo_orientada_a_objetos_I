import ttkbootstrap as ttk
from data_maneger import DataManeger


class Appplication(ttk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.datamaneger = DataManeger()
        self.title('Controle residencial')

        self.height_window = 720
        self.width_window = 1280
        self.position_right = int(self.winfo_screenwidth() / 2 - self.width_window / 2)
        self.position_down = int(self.winfo_screenheight() / 2 - self.height_window / 2)
        self.geometry(f"{self.width_window}x{self.height_window}+{self.position_right}+{self.position_down}")
