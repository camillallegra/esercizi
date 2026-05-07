import streamlit as st

st.set_page_config(
    page_title="Quiz Logica Condizionale",
    page_icon="💻",
    layout="centered"
)

# ----------------------------
# DATI
# ----------------------------

domande = [
    {
        "testo": "Quando devi risolvere un problema, preferisci:",
        "opzioni": [
            ("Provare subito una soluzione", "1"),
            ("Ragionare prima con calma", "2")
        ]
    },
    {
        "testo": "Davanti a un errore nel programma, cosa fai prima?",
        "opzioni": [
            ("Modifico qualcosa e riprovo", "1"),
            ("Leggo con attenzione il messaggio di errore", "2")
        ]
    },
    {
        "testo": "Preferisci lavorare:",
        "opzioni": [
            ("Da solo", "1"),
            ("In gruppo", "2")
        ]
    }
]

profili = {
    "111": ("Creatore Istintivo", "Ti butti subito e impari facendo. Sei veloce, creativo e ami sperimentare, ma a volte rischi di saltare qualche passaggio."),
    "112": ("Creatore Collaborativo", "Ti piace provare soluzioni concrete e confrontarti con gli altri. Sei molto utile nei lavori pratici di gruppo."),
    "121": ("Sperimentatore Analitico", "Provi soluzioni nuove, ma sai anche osservare gli errori. Hai un buon equilibrio tra azione e controllo."),
    "122": ("Analista Collaborativo", "Analizzi i problemi e lavori bene con gli altri. Sei adatto a risolvere situazioni complesse in gruppo."),
    "211": ("Riflessivo Indipendente", "Preferisci pensare con calma e lavorare da solo. Hai un approccio profondo, personale e ordinato."),
    "212": ("Stratega di Gruppo", "Rifletti prima di agire e poi ti confronti con gli altri. Sei molto utile quando bisogna prendere decisioni condivise."),
    "221": ("Analista Preciso", "Sei metodico, attento agli errori e preciso. Hai un approccio ideale per il debugging."),
    "222": ("Problem Solver Completo", "Rifletti, analizzi e collabori. Hai un approccio completo, equilibrato e molto efficace.")
}

# ----------------------------
# SESSIONE
# ----------------------------

if "step" not in st.session_state:
    st.session_state.step = 0

if "percorso" not in st.session_state:
    st.session_state.percorso = ""

# ----------------------------
# FUNZIONI
# ----------------------------

def scegli_risposta(valore):
    st.session_state.percorso += valore
    st.session_state.step += 1

def ricomincia():
    st.session_state.step = 0
    st.session_state.percorso = ""

# ----------------------------
# INTERFACCIA
# ----------------------------

st.title("💻 Che tipo di esploratore digitale sei?")
st.write("Rispondi alle domande e scopri il tuo profilo attraverso la logica condizionale.")

st.divider()

totale_domande = len(domande)

if st.session_state.step < totale_domande:
    domanda_corrente = domande[st.session_state.step]

    st.progress(st.session_state.step / totale_domande)

    st.subheader(f"Domanda {st.session_state.step + 1} di {totale_domande}")
    st.write(domanda_corrente["testo"])

    for testo_opzione, valore in domanda_corrente["opzioni"]:
        st.button(
            testo_opzione,
            on_click=scegli_risposta,
            args=(valore,),
            use_container_width=True
        )

else:
    st.progress(1.0)

    percorso = st.session_state.percorso
    titolo, descrizione = profili[percorso]

    st.success(f"Il tuo profilo è: {titolo}")
    st.write(descrizione)

    st.info(f"Percorso decisionale generato: `{percorso}`")

    st.caption(
        "Ogni cifra del percorso rappresenta una risposta. "
        "Il programma usa condizioni if/else per determinare l'output finale."
    )

    st.button("Ricomincia", on_click=ricomincia)
