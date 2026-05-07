import tkinter as tk
from tkinter import messagebox

# ----------------------------
# FUNZIONE PRINCIPALE
# ----------------------------

def calcola_risultato():
    risposta1 = var1.get()
    risposta2 = var2.get()
    risposta3 = var3.get()

    if risposta1 == "" or risposta2 == "" or risposta3 == "":
        messagebox.showwarning("Attenzione", "Rispondi a tutte le domande prima di continuare.")
        return

    percorso = risposta1 + risposta2 + risposta3

    profili = {
        "111": (
            "Creatore Istintivo",
            "Ti butti subito e impari facendo. Sei veloce, creativo e ami sperimentare, "
            "ma a volte rischi di saltare qualche passaggio."
        ),
        "112": (
            "Creatore Collaborativo",
            "Ti piace provare soluzioni concrete e confrontarti con gli altri. "
            "Sei molto utile nei lavori pratici di gruppo."
        ),
        "121": (
            "Sperimentatore Analitico",
            "Provi soluzioni nuove, ma sai anche osservare gli errori. "
            "Hai un buon equilibrio tra azione e controllo."
        ),
        "122": (
            "Analista Collaborativo",
            "Analizzi i problemi e lavori bene con gli altri. "
            "Sei adatto a risolvere situazioni complesse in gruppo."
        ),
        "211": (
            "Riflessivo Indipendente",
            "Preferisci pensare con calma e lavorare da solo. "
            "Hai un approccio profondo, personale e ordinato."
        ),
        "212": (
            "Stratega di Gruppo",
            "Rifletti prima di agire e poi ti confronti con gli altri. "
            "Sei molto utile quando bisogna prendere decisioni condivise."
        ),
        "221": (
            "Analista Preciso",
            "Sei metodico, attento agli errori e preciso. "
            "Hai un approccio ideale per il debugging e per il controllo del codice."
        ),
        "222": (
            "Problem Solver Completo",
            "Rifletti, analizzi e collabori. "
            "Hai un approccio completo, equilibrato e molto efficace."
        )
    }

    titolo, descrizione = profili[percorso]

    risultato_titolo.config(text=titolo)
    risultato_descrizione.config(text=descrizione)
    codice_percorso.config(text=f"Percorso decisionale: {percorso}")


def reset_quiz():
    var1.set("")
    var2.set("")
    var3.set("")
    risultato_titolo.config(text="")
    risultato_descrizione.config(text="")
    codice_percorso.config(text="")


# ----------------------------
# FINESTRA PRINCIPALE
# ----------------------------

root = tk.Tk()
root.title("Quiz - Logica Condizionale")
root.geometry("720x680")
root.configure(bg="#F4F1EC")
root.resizable(False, False)

# ----------------------------
# STILI
# ----------------------------

FONT_TITOLO = ("Arial", 22, "bold")
FONT_SOTTOTITOLO = ("Arial", 12)
FONT_DOMANDA = ("Arial", 13, "bold")
FONT_TESTO = ("Arial", 11)
FONT_BOTTONE = ("Arial", 11, "bold")
FONT_RISULTATO = ("Arial", 18, "bold")

COLORE_SFONDO = "#F4F1EC"
COLORE_CARD = "#FFFFFF"
COLORE_ACCENTO = "#4F6F52"
COLORE_TESTO = "#2B2B2B"
COLORE_SECONDARIO = "#6B6B6B"

# ----------------------------
# CONTENITORE PRINCIPALE
# ----------------------------

frame = tk.Frame(root, bg=COLORE_SFONDO)
frame.pack(padx=35, pady=25, fill="both", expand=True)

# ----------------------------
# INTESTAZIONE
# ----------------------------

titolo = tk.Label(
    frame,
    text="Che tipo di esploratore digitale sei?",
    font=FONT_TITOLO,
    fg=COLORE_TESTO,
    bg=COLORE_SFONDO
)
titolo.pack(pady=(5, 5))

sottotitolo = tk.Label(
    frame,
    text="Rispondi alle domande e scopri il tuo profilo attraverso la logica condizionale.",
    font=FONT_SOTTOTITOLO,
    fg=COLORE_SECONDARIO,
    bg=COLORE_SFONDO,
    wraplength=600,
    justify="center"
)
sottotitolo.pack(pady=(0, 20))

# ----------------------------
# VARIABILI RISPOSTE
# ----------------------------

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()

# ----------------------------
# FUNZIONE PER CREARE LE DOMANDE
# ----------------------------

def crea_domanda(parent, numero, testo, opzione1, opzione2, variabile):
    card = tk.Frame(parent, bg=COLORE_CARD, padx=18, pady=14)
    card.pack(fill="x", pady=8)

    domanda = tk.Label(
        card,
        text=f"{numero}. {testo}",
        font=FONT_DOMANDA,
        fg=COLORE_TESTO,
        bg=COLORE_CARD,
        anchor="w"
    )
    domanda.pack(anchor="w", pady=(0, 8))

    radio1 = tk.Radiobutton(
        card,
        text=opzione1,
        variable=variabile,
        value="1",
        font=FONT_TESTO,
        fg=COLORE_TESTO,
        bg=COLORE_CARD,
        activebackground=COLORE_CARD,
        selectcolor=COLORE_SFONDO
    )
    radio1.pack(anchor="w")

    radio2 = tk.Radiobutton(
        card,
        text=opzione2,
        variable=variabile,
        value="2",
        font=FONT_TESTO,
        fg=COLORE_TESTO,
        bg=COLORE_CARD,
        activebackground=COLORE_CARD,
        selectcolor=COLORE_SFONDO
    )
    radio2.pack(anchor="w")

# ----------------------------
# DOMANDE
# ----------------------------

crea_domanda(
    frame,
    1,
    "Quando devi risolvere un problema, preferisci:",
    "Provare subito una soluzione",
    "Ragionare prima con calma",
    var1
)

crea_domanda(
    frame,
    2,
    "Davanti a un errore nel programma, cosa fai prima?",
    "Modifico qualcosa e riprovo",
    "Leggo con attenzione il messaggio di errore",
    var2
)

crea_domanda(
    frame,
    3,
    "Preferisci lavorare:",
    "Da solo",
    "In gruppo",
    var3
)

# ----------------------------
# BOTTONI
# ----------------------------

frame_bottoni = tk.Frame(frame, bg=COLORE_SFONDO)
frame_bottoni.pack(pady=18)

bottone_risultato = tk.Button(
    frame_bottoni,
    text="Scopri il risultato",
    command=calcola_risultato,
    font=FONT_BOTTONE,
    bg=COLORE_ACCENTO,
    fg="white",
    activebackground="#3F5A42",
    activeforeground="white",
    padx=22,
    pady=8,
    relief="flat",
    cursor="hand2"
)
bottone_risultato.grid(row=0, column=0, padx=8)

bottone_reset = tk.Button(
    frame_bottoni,
    text="Ricomincia",
    command=reset_quiz,
    font=FONT_BOTTONE,
    bg="#D9D4CC",
    fg=COLORE_TESTO,
    activebackground="#C9C2B8",
    activeforeground=COLORE_TESTO,
    padx=22,
    pady=8,
    relief="flat",
    cursor="hand2"
)
bottone_reset.grid(row=0, column=1, padx=8)

# ----------------------------
# AREA RISULTATO
# ----------------------------

frame_risultato = tk.Frame(frame, bg=COLORE_CARD, padx=20, pady=18)
frame_risultato.pack(fill="x", pady=(5, 0))

risultato_titolo = tk.Label(
    frame_risultato,
    text="",
    font=FONT_RISULTATO,
    fg=COLORE_ACCENTO,
    bg=COLORE_CARD
)
risultato_titolo.pack(pady=(0, 6))

risultato_descrizione = tk.Label(
    frame_risultato,
    text="",
    font=FONT_TESTO,
    fg=COLORE_TESTO,
    bg=COLORE_CARD,
    wraplength=600,
    justify="center"
)
risultato_descrizione.pack()

codice_percorso = tk.Label(
    frame_risultato,
    text="",
    font=("Arial", 10, "italic"),
    fg=COLORE_SECONDARIO,
    bg=COLORE_CARD
)
codice_percorso.pack(pady=(10, 0))

# ----------------------------
# AVVIO PROGRAMMA
# ----------------------------

root.mainloop()
