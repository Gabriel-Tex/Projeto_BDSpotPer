import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from app.GUI.gui_playlists import criar_playlists
from app.GUI.gui_albuns import criar_albuns
from app.GUI.gui_consultas import criar_consultas
from app.GUI.gui_faixas import criar_faixas
from app.GUI.gui_compositor import criar_obras_compositor

class BDSpotPerApp(ttk.Window):
    def __init__(self):
        super().__init__(
            title="BDSpotPer",
            themename="darkly",
            size=(1000, 650),
            resizable=(False, False)
        )
        self._criar_layout()

    def _criar_layout(self):
        container = ttk.Frame(self)
        container.pack(expand=True, fill=BOTH)

        sidebar = ttk.Frame(container, width=200)
        sidebar.pack(side=LEFT, fill=Y)

        ttk.Label(
            sidebar,
            text="BDSpotPer",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(20, 5))

        ttk.Label(
            sidebar,
            text="Gerenciador Musical",
            font=("Segoe UI", 10),
            foreground="#AAAAAA"
        ).pack(pady=(0, 20))

        ttk.Separator(sidebar).pack(fill=X, padx=10, pady=10)

        content = ttk.Frame(container)
        content.pack(side=RIGHT, expand=True, fill=BOTH, padx=10, pady=10)

        tabs = ttk.Notebook(content, bootstyle="dark")
        tabs.pack(expand=True, fill=BOTH)

        criar_playlists(tabs)
        criar_consultas(tabs)
        criar_albuns(tabs)
        criar_faixas(tabs)
        criar_obras_compositor(tabs)