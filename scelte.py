import streamlit as st

st.set_page_config(
    page_title="Quiz Logica Condizionale",
    page_icon="💻",
    layout="centered"
)

st.title("💻 Che tipo di esploratore digitale sei?")
st.write(
    "Rispondi alle domande e scopri il tuo profilo attraverso la logica condizionale."
)

st.divider()

r1 = st.radio(
    "1. Quando devi risolvere un problema, preferisci:",
    ["Provare subito una soluzione", "Ragionare prima con calma"]
)

r2 = st.radio(
    "2. Davanti a un errore nel programma, cosa fai prima?",
    ["Modifico qualcosa e riprovo", "Leggo con attenzione il messaggio di errore"]
)

r3 = st.radio(
    "3. Preferisci lavorare:",
    ["Da solo", "In gruppo"]
)

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

if st.button("Scopri il risultato"):
    percorso = ""

    if r1 == "Provare subito una soluzione":
        percorso += "1"
    else:
        percorso += "2"

    if r2 == "Modifico qualcosa e riprovo":
        percorso += "1"
    else:
        percorso += "2"

    if r3 == "Da solo":
        percorso += "1"
    else:
        percorso += "2"

    titolo, descrizione = profili[percorso]

    st.success(f"Il tuo profilo è: {titolo}")
    st.write(descrizione)

    st.info(f"Percorso decisionale generato: `{percorso}`")

    st.caption(
        "Ogni cifra del percorso rappresenta una risposta. "
        "Il programma usa condizioni if/else per determinare l'output finale."
    )
