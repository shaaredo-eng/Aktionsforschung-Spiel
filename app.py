import streamlit as st

# Seitensetup
st.set_page_config(page_title="Action Research Navigator", page_icon="⛵", layout="wide")

# Spielzustände (Session State)
if "current_scenario" not in st.state_defaults:
    if "current_scenario" not in st.session_state:
        st.session_state.current_scenario = 0
        st.session_state.resilience = 50
        st.session_state.methods = 50
        st.session_state.autonomy = 50
        st.session_state.completed = False
        st.session_state.history = []

# Szenarien-Datenbank
scenarios = [
    {
        "title": "Szenario 1: Wortschatzvermittlung im DaF-Unterricht",
        "situation": "Die Schüler*innen lernen neue Nomen, vergessen die Artikel aber bereits am nächsten Tag wieder. Sie sind unschlüssig, wie Sie den Unterricht anpassen sollen.",
        "options": [
            {
                "text": "Option A: Für eine eintägige Fortbildung in zwei Monaten anmelden.",
                "type": "classic",
                "feedback": "„Klassische Ein-Tages-Workshops verändern wenig – echte Entwicklung passiert mitten im Schulalltag.“",
                "resilience": -5, "methods": 0, "autonomy": 0
            },
            {
                "text": "Option B: Forschungsfrage formulieren: „Inwiefern verbessert der gezielte Einsatz von Farbcodierungen und Bildkarten das Behalten von Genuszuordnungen?“ und direkt erproben.",
                "type": "action_research",
                "feedback": "„Unsicherheiten werden nicht zum Problem, sondern zur spannenden Forschungsfrage.“ & „Wissenschaftliche Theorien sind keine starren Regeln, sondern Hypothesen zum eigenen Erproben.“",
                "resilience": 15, "methods": 20, "autonomy": 10
            },
            {
                "text": "Option C: Den Schüler*innen doppelt so viele Vokabellisten als Hausaufgabe aufgeben.",
                "type": "avoidance",
                "feedback": "Überforderung steigt bei Lehrkraft und Lernenden. Das eigentliche Problem bleibt ungelöst.",
                "resilience": -10, "methods": -5, "autonomy": -5
            }
        ]
    },
    {
        "title": "Szenario 2: Komplexe Grammatikstrukturen & Redemittel",
        "situation": "Trotz mehrfacher Grammatikübungen zu Nebensätzen mit „weil“ und „dass“ nutzen die Lernenden in freien Gesprächsphasen weiterhin nur einfache Hauptsätze.",
        "options": [
            {
                "text": "Option A: 5 Minuten Unterrichtsinteraktion aufnehmen, transkribieren und prüfen, an welchen Stellen Scaffolding gefehlt hat.",
                "type": "action_research",
                "feedback": "„Wer Probleme im Unterricht systematisch erforscht, schützt sich langfristig vor Überforderung.“",
                "resilience": 15, "methods": 20, "autonomy": 20
            },
            {
                "text": "Option B: Vorgefertigte Übungsblätter aus dem Internet herunterladen und noch mehr Lückentexte ausfüllen lassen.",
                "type": "classic",
                "feedback": "Mehr desselben führt selten zu echter Sprachhandlungskompetenz im freien Sprechen.",
                "resilience": -5, "methods": 0, "autonomy": 0
            },
            {
                "text": "Option C: Das Thema abbrechen und davon ausgehen, dass die Gruppe noch nicht bereit ist.",
                "type": "avoidance",
                "feedback": "Frustration stellt sich ein. Die Passung von Lernangebot und Lernstand wird nicht reflektiert.",
                "resilience": -10, "methods": -5, "autonomy": -5
            }
        ]
    },
    {
        "title": "Szenario 3: Feedback und Lernerautonomie",
        "situation": "Nach einer schriftlichen Aufgabe korrigieren Sie stundenlang Fehler mit roter Farbe, merken aber, dass die Schüler*innen die Korrekturen kaum anschauen.",
        "options": [
            {
                "text": "Option A: Am Wochenende ein Web-Seminar zum Thema „Effiziente Korrekturtechniken“ besuchen.",
                "type": "classic",
                "feedback": "Externe Inputs geben Ideen, lösen aber nicht die konkrete Interaktionsdynamik in Ihrer Klasse.",
                "resilience": 0, "methods": 5, "autonomy": 0
            },
            {
                "text": "Option B: Das Korrigieren komplett einstellen und nur noch Noten ohne Feedback vergeben.",
                "type": "avoidance",
                "feedback": "Verlust von Diagnosemöglichkeiten und Begleitung der Lernenden.",
                "resilience": -10, "methods": -10, "autonomy": -10
            },
            {
                "text": "Option C: Methode des „Lauten Denkens“ mit zwei Lernenden nutzen und Mini-Interviews zur Feedback-Verarbeitung führen.",
                "type": "action_research",
                "feedback": "„Klassische Ein-Tages-Workshops verändern wenig – echte Entwicklung passiert mitten im Schulalltag.“",
                "resilience": 15, "methods": 20, "autonomy": 20
            }
        ]
    },
    {
        "title": "Szenario 4: Einsatz digitaler Medien im Unterricht",
        "situation": "Sie möchten eine Lern-App zur Grammatikwiederholung einbauen, sind sich aber unsicher, ob der Einsatz den Lernerfolg wirklich steigert oder nur ablenkt.",
        "options": [
            {
                "text": "Option A: Vor und nach einer zweiwöchigen Testphase einen C-Test sowie einen Beobachtungsbogen einsetzen.",
                "type": "action_research",
                "feedback": "„Wissenschaftliche Theorien sind keine starren Regeln, sondern Hypothesen zum eigenen Erproben.“",
                "resilience": 10, "methods": 20, "autonomy": 20
            },
            {
                "text": "Option B: Die App unverändert übernehmen, weil sie im Fachmagazin als „best practice“ empfohlen wurde.",
                "type": "classic",
                "feedback": "Ohne kriteriengeleitete Evaluation bleibt unklar, ob das Medium für Ihren konkreten Lernkontext passt.",
                "resilience": 0, "methods": 0, "autonomy": 0
            },
            {
                "text": "Option C: Komplett auf digitale Medien verzichten, um Unruhe im Unterricht zu vermeiden.",
                "type": "avoidance",
                "feedback": "Vermeidung von Innovationen aus Unsicherheit.",
                "resilience": -5, "methods": -5, "autonomy": -5
            }
        ]
    },
    {
        "title": "Szenario 5: Binnendifferenzierung bei unterschiedlichem Sprachniveau",
        "situation": "In Ihrer DaF-Klasse klafft die Sprachkompetenz stark auseinander. Ein Drittel ist unterfordert, während ein anderes Drittel dem Unterricht kaum folgen kann.",
        "options": [
            {
                "text": "Option A: Im Frontalunterricht weiter auf mittlerem Niveau unterrichten und hoffen, dass sich die Schwächeren anpassen.",
                "type": "avoidance",
                "feedback": "Erhöht Überforderungsgefühle bei Lernenden und Lehrkraft langfristig.",
                "resilience": -15, "methods": -5, "autonomy": -5
            },
            {
                "text": "Option B: Verwandlung in eine Forschungsfrage: „Welche Form gestufter Lernhilfen ermöglicht allen Niveaustufen aktive Teilnahme?“ und Erfassung mit GER-Raster.",
                "type": "action_research",
                "feedback": "„Unsicherheiten werden nicht zum Problem, sondern zur spannenden Forschungsfrage.“ & „Wer Probleme im Unterricht systematisch erforscht, schützt sich langfristig vor Überforderung.“",
                "resilience": 25, "methods": 15, "autonomy": 15
            },
            {
                "text": "Option C: Auf das nächste ganztägige Pädagogische Seminar im kommenden Schuljahr warten.",
                "type": "classic",
                "feedback": "Passives Warten verändert die aktuelle Unterrichtssituation im Alltag nicht.",
                "resilience": -5, "methods": 0, "autonomy": 0
            }
        ]
    }
]

# Header & Titel
st.title("⛵ Der Action Research Navigator")
st.caption("Interaktives Simulations-Dashboard für angehende DaF/DaZ-Lehrkräfte")

# Sidebar / Dashboard-Status
with st.sidebar:
    st.header("📊 Forschungs-Profil")
    st.write("Ihre Entwicklung als *Reflective Practitioner*:")
    
    st.subheader("🛡️ Resilienz (Burnout-Schutz)")
    st.progress(min(max(st.session_state.resilience, 0), 100))
    st.caption(f"Wert: {st.session_state.resilience} / 100")
    
    st.subheader("🔬 Methodenkompetenz")
    st.progress(min(max(st.session_state.methods, 0), 100))
    st.caption(f"Wert: {st.session_state.methods} / 100")
    
    st.subheader("🎯 Handlungsautonomie")
    st.progress(min(max(st.session_state.autonomy, 0), 100))
    st.caption(f"Wert: {st.session_state.autonomy} / 100")
    
    st.divider()
    if st.button("🔄 Spiel zurücksetzen"):
        st.session_state.current_scenario = 0
        st.session_state.resilience = 50
        st.session_state.methods = 50
        st.session_state.autonomy = 50
        st.session_state.completed = False
        st.session_state.history = []
        st.rerun()

# Hauptbereich: Szenario oder Auswertung
if not st.session_state.completed:
    idx = st.session_state.current_scenario
    scenario = scenarios[idx]
    
    st.subheader(f"Szenario {idx + 1} von {len(scenarios)}")
    st.progress((idx) / len(scenarios))
    
    st.info(f"**{scenario['title']}**\n\n{scenario['situation']}")
    
    st.write("### Wie entscheiden Sie sich?")
    
    for i, opt in enumerate(scenario["options"]):
        if st.button(opt["text"], key=f"opt_{idx}_{i}"):
            # Stats anpassen
            st.session_state.resilience += opt["resilience"]
            st.session_state.methods += opt["methods"]
            st.session_state.autonomy += opt["autonomy"]
            
            # Verlauf speichern
            st.session_state.history.append({
                "scenario": scenario["title"],
                "option": opt["text"],
                "feedback": opt["feedback"],
                "type": opt["type"]
            })
            
            # Weiter zum nächsten Szenario
            if st.session_state.current_scenario + 1 < len(scenarios):
                st.session_state.current_scenario += 1
            else:
                st.session_state.completed = True
            st.rerun()

else:
    st.balloons()
    st.success("🎉 **Glückwunsch! Sie haben alle Szenarien durchgespielt.**")
    st.subheader("Ihr Ergebnis als Reflective Practitioner:")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Resilienz", f"{st.session_state.resilience} Points")
    col2.metric("Methodenkompetenz", f"{st.session_state.methods} Points")
    col3.metric("Handlungsautonomie", f"{st.session_state.autonomy} Points")
    
    st.divider()
    st.write("### Zusammenfassung Ihrer Entscheidungen:")
    for h in st.session_state.history:
        with st.expander(f"📌 {h['scenario']}"):
            st.write(f"**Ihre Wahl:** {h['option']}")
            st.info(f"**Erkenntnis:** {h['feedback']}")
