import streamlit as st
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="HAMIDOUCHE REDJDAL | CV",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PHOTO
# ============================================================

PHOTO = Path("photo.jpg")


# ============================================================
# STYLE CSS
# ============================================================

st.markdown(
    """
<style>

.stApp {
    background-color: #f4f7fb;
}

.block-container {
    max-width: 1200px;
    padding-top: 25px;
    padding-bottom: 50px;
}

/* ==========================================================
   HEADER
   ========================================================== */

.cv-header {
    background: linear-gradient(135deg, #102a43, #1f5f8b);
    color: white;
    padding: 40px 45px;
    border-radius: 22px;
    margin-bottom: 30px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
    min-height: 260px;
}

.cv-name {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 12px;
}

.cv-title {
    font-size: 23px;
    font-weight: 600;
    margin-bottom: 18px;
}

.cv-subtitle {
    font-size: 16px;
    line-height: 1.8;
}

/* ==========================================================
   PHOTO
   ========================================================== */

.photo-container {
    text-align: center;
    padding-top: 10px;
}

.photo-title {
    color: white;
    font-size: 13px;
    margin-top: 10px;
}

/* ==========================================================
   TITRES
   ========================================================== */

.section-title {
    color: #102a43;
    font-size: 27px;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 3px solid #1f5f8b;
}

/* ==========================================================
   CARTES
   ========================================================== */

.card {
    background-color: white;
    border-radius: 17px;
    padding: 25px;
    margin-bottom: 18px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
}

.card-title {
    color: #102a43;
    font-size: 19px;
    font-weight: 800;
    margin-bottom: 10px;
}

.card-text {
    color: #52606d;
    font-size: 16px;
    line-height: 1.9;
}

/* ==========================================================
   EXPERIENCES
   ========================================================== */

.experience-card {
    background-color: white;
    border-left: 5px solid #1f5f8b;
    border-radius: 17px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
}

.experience-position {
    color: #102a43;
    font-size: 21px;
    font-weight: 800;
}

.experience-company {
    color: #1f5f8b;
    font-size: 16px;
    font-weight: 700;
    margin-top: 6px;
}

.experience-date {
    color: #829ab1;
    font-size: 14px;
    margin-top: 5px;
    margin-bottom: 18px;
}

.mission {
    color: #52606d;
    line-height: 1.7;
    margin-top: 9px;
}

/* ==========================================================
   FORMATIONS
   ========================================================== */

.education-card {
    background-color: white;
    border-radius: 17px;
    padding: 22px;
    margin-bottom: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
}

.year {
    display: inline-block;
    background-color: #102a43;
    color: white;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 10px;
}

.education-title {
    color: #102a43;
    font-size: 17px;
    font-weight: 800;
}

.education-school {
    color: #627d98;
    font-size: 14px;
    margin-top: 7px;
    line-height: 1.6;
}

/* ==========================================================
   COMPETENCES
   ========================================================== */

.skill-card {
    background-color: white;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    color: #334e68;
    line-height: 1.6;
}

/* ==========================================================
   TAGS
   ========================================================== */

.tag {
    display: inline-block;
    background-color: #e9f2f9;
    color: #102a43;
    padding: 9px 15px;
    margin: 4px;
    border-radius: 25px;
    font-size: 14px;
    font-weight: 600;
}

/* ==========================================================
   CONTACT
   ========================================================== */

.contact-card {
    background-color: white;
    border-radius: 17px;
    padding: 25px;
    text-align: center;
    min-height: 145px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
}

.contact-icon {
    font-size: 32px;
    margin-bottom: 8px;
}

.contact-title {
    color: #102a43;
    font-weight: 800;
    margin-bottom: 8px;
}

.contact-value {
    color: #52606d;
    font-size: 14px;
    line-height: 1.6;
}

/* ==========================================================
   SIDEBAR
   ========================================================== */

[data-testid="stSidebar"] {
    background-color: #102a43;
}

[data-testid="stSidebar"] * {
    color: white;
}

/* ==========================================================
   FOOTER
   ========================================================== */

.footer {
    text-align: center;
    color: #829ab1;
    font-size: 13px;
    margin-top: 50px;
    padding-top: 25px;
    border-top: 1px solid #d9e2ec;
}

/* ==========================================================
   MOBILE
   ========================================================== */

@media (max-width: 768px) {

    .cv-header {
        padding: 30px 25px;
    }

    .cv-name {
        font-size: 30px;
    }

    .cv-title {
        font-size: 18px;
    }

    .cv-subtitle {
        font-size: 14px;
    }

    .section-title {
        font-size: 23px;
    }

}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# INFORMATIONS PERSONNELLES
# ============================================================

nom = "HAMIDOUCHE REDJDAL"

fonction = "Planificateur et Superviseur Logistique"

telephone = "00213775 73 79 30"

email = "hamidoucheredjdal@yahoo.fr"

adresse = "Tazmalt 06039, wilaya de Bejaia"

nationalite = "Algérienne"

situation = "Marié"

service_national = "Dégagé"


# ============================================================
# PROFIL
# ============================================================

profil = (
    "Dynamique, sérieux et ayant de bonnes compétences relationnelles, "
    "avec 9 ans d'expérience dans le domaine de la logistique. "
    "Très à l'aise avec les outils informatiques, je souhaite mettre "
    "mes compétences et ma motivation au service d'une entreprise "
    "et relever de nouveaux défis professionnels."
)


# ============================================================
# EXPERIENCES PROFESSIONNELLES
# ============================================================

experiences = [

    {
        "poste": "Superviseur techno-commercial",
        "periode": "01/2024 - À ce jour",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Analyser les besoins des clients.",
            "Établir des reportings d'activité quotidiens, mensuels et annuels.",
            "Apporter des solutions pertinentes et adaptées.",
            "Suivre le bon déroulement de l'activité.",
            "Contrôler les flux entrants et sortants de la zone d'entreposage."
        ]
    },

    {
        "poste": "Superviseur exploitation",
        "periode": "06/2022 - 01/2024",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Piloter et superviser les opérations de transport.",
            "Suivre le bon déroulement de l'activité.",
            "Contrôler les flux entrants et sortants de la zone d'entreposage.",
            "Planifier, organiser et contrôler l'activité d'une équipe.",
            "Réceptionner les commandes des clients et veiller à leur satisfaction.",
            "Assurer la bonne réalisation du programme et le réadapter en fonction des imprévus."
        ]
    },

    {
        "poste": "Chargé de la planification",
        "periode": "02/2020 - 06/2022",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Préparer la disponibilité des ressources humaines et matérielles.",
            "Planifier les commandes de chaque client.",
            "Élaborer les reportings et les KPI liés à l'activité.",
            "Réceptionner et traiter les demandes du service commercial.",
            "Optimiser les ressources logistiques en termes de coûts et de délais.",
            "Administrer et générer les ordres de mission.",
            "Assurer la bonne réalisation du programme et le réadapter en fonction des imprévus."
        ]
    },

    {
        "poste": "Coordinateur logistique",
        "periode": "02/2019 - 02/2020",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Élaborer et maintenir une parfaite coordination avec les autres services.",
            "Élaborer et mettre en place des indicateurs de suivi de transport.",
            "Gérer les partenariats avec les prestataires de transport.",
            "Piloter et contrôler les performances des activités à court, moyen et long terme.",
            "Veiller au respect des procédures de travail et de la réglementation."
        ]
    },

    {
        "poste": "Chargé de la programmation",
        "periode": "04/2016 - 10/2018",
        "entreprise": "SPA TMF Logistics",
        "missions": [
            "Exécuter et suivre régulièrement la programmation et l'utilisation des ressources.",
            "Établir un planning optimal en optimisant les coûts et les délais.",
            "Anticiper les situations imprévues et prendre rapidement les décisions correctives.",
            "Étudier la faisabilité d'une mission avant d'affecter les ressources."
        ]
    }
]


# ============================================================
# FORMATIONS
# ============================================================

formations = [

    {
        "annee": "2021",
        "titre": "Formation en Transport international des marchandises",
        "organisme": "Chambre algérienne de commerce et d'industrie, Alger - Algérie"
    },

    {
        "annee": "2020",
        "titre": "Formation en Planification et optimisation logistique",
        "organisme": "Institut international de Management, Bejaia - Algérie"
    },

    {
        "annee": "2019",
        "titre": "Formation en Logistique et transport",
        "organisme": "Institut international de management, Bejaia - Algérie"
    },

    {
        "annee": "2019",
        "titre": "Formation en Gestion des temps et des priorités",
        "organisme": "Institut international de management, Bejaia - Algérie"
    },

    {
        "annee": "2018",
        "titre": "Formation en Gestion des opérations de transport",
        "organisme": "Institut international de management, Bejaia - Algérie"
    },

    {
        "annee": "2015",
        "titre": "Master 2 en Recherche opérationnelle",
        "organisme": (
            "Option : Fiabilité et évaluation des performances des réseaux. "
            "Université Abderrahmane Mira, Bejaia - Algérie"
        )
    },

    {
        "annee": "2012",
        "titre": "Licence en Recherche opérationnelle",
        "organisme": (
            "Option : Aide à la décision. "
            "Université Abderrahmane Mira, Bejaia - Algérie"
        )
    },

    {
        "annee": "2012",
        "titre": "Attestation de stage en gestion portuaire",
        "organisme": "Entreprise portuaire de Bejaia, Bejaia - Algérie"
    },

    {
        "annee": "2008",
        "titre": "Diplôme Baccalauréat",
        "organisme": (
            "Option : Science de la nature et de la vie. "
            "Lycée Mohamed Boudiaf, Tazmalt - Algérie"
        )
    }
]


# ============================================================
# COMPETENCES
# ============================================================

competences = [

    "Maîtrise du Pack Office : Excel, Word, PowerPoint et Outlook.",

    "Maîtrise de Matlab, LaTeX, Photoshop, Illustrator et InDesign.",

    "Langages de programmation : HTML, Java, Delphi et C++.",

    "Planification et optimisation des ressources.",

    "Gestion des opérations de transport.",

    "Supervision des opérations de transport.",

    "Élaboration et mise en place des indicateurs de suivi de transport.",

    "Élaboration des reportings et KPI liés à l'activité.",

    "Gestion des partenariats avec les prestataires de transport.",

    "Coordination avec les autres services.",

    "Gestion des ressources humaines et matérielles.",

    "Gestion et génération des ordres de mission."
]


# ============================================================
# LANGUES
# ============================================================

langues = [

    ("Kabyle", "Maîtrise très bien"),

    ("Arabe", "Maîtrise très bien"),

    ("Français", "Maîtrise bien"),

    ("Anglais", "Maîtrise moyenne")
]


# ============================================================
# CENTRES D'INTERET
# ============================================================

interets = [

    ("✈️", "Voyage"),

    ("⚽", "Passion pour le sport"),

    ("🤝", "Activités associatives"),

    ("🎬", "Cinéma"),

    ("🎨", "Arts créatifs"),

    ("💻", "Informatique")
]


# ============================================================
# HEADER AVEC PHOTO
# ============================================================

col_photo, col_header = st.columns([1, 4])

with col_photo:

    st.markdown(
        """
<div style="
background: linear-gradient(135deg, #102a43, #1f5f8b);
padding: 25px;
border-radius: 22px;
height: 100%;
text-align: center;
">
""",
        unsafe_allow_html=True
    )

    if PHOTO.exists():

        st.image(
            str(PHOTO),
            width=180
        )

    else:

        st.markdown(
            """
<div style="
font-size:100px;
padding:30px;
">
👤
</div>
""",
            unsafe_allow_html=True
        )

        st.warning("Photo non trouvée")

    st.markdown(
        """
</div>
""",
        unsafe_allow_html=True
    )


with col_header:

    st.markdown(
        """
<div class="cv-header">

<div class="cv-name">
HAMIDOUCHE REDJDAL
</div>

<div class="cv-title">
🚚 Planificateur &amp; Superviseur Logistique
</div>

<div class="cv-subtitle">
Master 2 en Recherche Opérationnelle
<br><br>
Logistique &nbsp; • &nbsp;
Transport &nbsp; • &nbsp;
Planification &nbsp; • &nbsp;
Supervision &nbsp; • &nbsp;
Optimisation
</div>

</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
<div style="
text-align:center;
padding:15px 5px 20px 5px;
">

<div style="font-size:45px;">
🚚
</div>

<div style="
font-size:20px;
font-weight:800;
">
HAMIDOUCHE REDJDAL
</div>

<div style="
font-size:13px;
margin-top:6px;
">
CURRICULUM VITAE
</div>

</div>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "🏠 Accueil",
        "👤 Profil",
        "💼 Expériences",
        "🎓 Diplômes & Formations",
        "🛠️ Compétences",
        "🌐 Langues",
        "⭐ Centres d'intérêt",
        "📞 Contact"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
**DOMAINES PROFESSIONNELS**

🚚 Transport

📦 Logistique

📊 Planification

👥 Supervision

📈 Optimisation
"""
)


# ============================================================
# ACCUEIL
# ============================================================

if page == "🏠 Accueil":

    st.markdown(
        "<div class='section-title'>Profil professionnel</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
<div class="card">

<p class="card-text">
{profil}
</p>

</div>
""",
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # INDICATEURS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Expérience",
            "9 ans"
        )

    with col2:

        st.metric(
            "Postes",
            "5"
        )

    with col3:

        st.metric(
            "Formations",
            "9"
        )

    with col4:

        st.metric(
            "Langues",
            "4"
        )


   # --------------------------------------------------------
   # DOMAINES D'EXPERTISE
   # --------------------------------------------------------
    st.markdown(
    "<div class='section-title'>Domaines d'expertise</div>",
    unsafe_allow_html=True,
)

domaines = [
    (
        "🚚",
        "Transport",
        "Organisation, suivi et supervision des opérations de transport.",
    ),
    (
        "📦",
        "Logistique",
        "Gestion des flux, des opérations logistiques et des ressources.",
    ),
    (
        "📅",
        "Planification",
        "Élaboration des programmes et planification des ressources humaines et matérielles.",
    ),
    (
        "👥",
        "Supervision",
        "Suivi des équipes et contrôle du bon déroulement des opérations.",
    ),
    (
        "📈",
        "Optimisation",
        "Recherche de solutions permettant d'améliorer les coûts, les délais et l'utilisation des ressources.",
    ),
    (
        "📊",
        "Reporting",
        "Élaboration et suivi des reportings d'activité pour faciliter le pilotage.",
    ),
    (
        "🎯",
        "KPI",
        "Mise en place et suivi des indicateurs de performance liés à l'activité.",
    ),
    (
        "🤝",
        "Coordination",
        "Coordination entre les différents services et intervenants afin d'assurer la continuité des opérations.",
    ),
    (
        "⚙️",
        "Gestion des ressources",
        "Préparation, affectation et utilisation optimale des ressources disponibles.",
    ),
]

col1, col2, col3 = st.columns(3)

for index, (icone, titre, definition) in enumerate(domaines):
    if index % 3 == 0:
        colonne = col1
    elif index % 3 == 1:
        colonne = col2
    else:
        colonne = col3

    with colonne:
        st.markdown(
            f"""
            <div class="card" style="min-height: 190px;">
                <div style="font-size: 34px; margin-bottom: 10px;">
                    {icone}
                </div>
                <div class="card-title">
                    {titre}
                </div>
                <div style="color:#52606d; font-size:14px; line-height:1.7; margin-top:10px;">
                    {definition}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # --------------------------------------------------------
    # EXPERIENCE ACTUELLE
    # --------------------------------------------------------

    st.markdown(
        "<div class='section-title'>Expérience actuelle</div>",
        unsafe_allow_html=True
    )

    current = experiences[0]

    st.markdown(
        f"""
<div class="experience-card">

<div class="experience-position">
{current["poste"]}
</div>

<div class="experience-company">
🏢 {current["entreprise"]}
</div>

<div class="experience-date">
📅 {current["periode"]}
</div>

</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# PROFIL
# ============================================================
elif page == "👤 Profil":
   st.markdown(
        "<div class='section-title'>Profil professionnel</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
<div class="card">

<p class="card-text">
{profil}
</p>

</div>
""",
        unsafe_allow_html=True
    )


    st.markdown(
        "<div class='section-title'>Informations personnelles</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
<div class="card">

<div class="card-title">
👤 Identité
</div>

<p>
<strong>Nom :</strong><br>
{nom}
</p>

<p>
<strong>Nationalité :</strong><br>
{nationalite}
</p>

<p>
<strong>Situation familiale :</strong><br>
{situation}
</p>

</div>
""",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            f"""
<div class="card">

<div class="card-title">
📋 Informations professionnelles
</div>

<p>
<strong>Fonction :</strong><br>
{fonction}
</p>

<p>
<strong>Adresse :</strong><br>
{adresse}
</p>

<p>
<strong>Service national :</strong><br>
{service_national}
</p>

</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# EXPERIENCES
# ============================================================
elif page == "💼 Expériences":

    st.markdown(
        "<div class='section-title'>Expériences professionnelles</div>",
        unsafe_allow_html=True
    )

    for exp in experiences:

        st.markdown(
            f"""
<div class="experience-card">

<div class="experience-position">
{exp["poste"]}
</div>

<div class="experience-company">
🏢 {exp["entreprise"]}
</div>

<div class="experience-date">
📅 {exp["periode"]}
</div>

<strong>Principales missions</strong>

""",
            unsafe_allow_html=True
        )

        for mission in exp["missions"]:

            st.markdown(
                f"""
<div class="mission">
✓ {mission}
</div>
""",
                unsafe_allow_html=True
            )

        st.markdown(
            """
</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# DIPLOMES ET FORMATIONS
# ============================================================
elif page == "🎓 Diplômes & Formations":

    st.markdown(
        "<div class='section-title'>Diplômes & Formations</div>",
        unsafe_allow_html=True
    )

    for formation in formations:

        st.markdown(
            f"""
<div class="education-card">

<div class="year">
{formation["annee"]}
</div>

<div class="education-title">
{formation["titre"]}
</div>

<div class="education-school">
🏫 {formation["organisme"]}
</div>

</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# COMPETENCES
# ============================================================
elif page == "🛠️ Compétences":

    st.markdown(
        "<div class='section-title'>Compétences professionnelles</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    for index, competence in enumerate(competences):

        if index % 2 == 0:

            with col1:

                st.markdown(
                    f"""
<div class="skill-card">
✓ {competence}
</div>
""",
                    unsafe_allow_html=True
                )

        else:

            with col2:

                st.markdown(
                    f"""
<div class="skill-card">
✓ {competence}
</div>
""",
                    unsafe_allow_html=True
                )


# ============================================================
# LANGUES
# ============================================================
elif page == "🌐 Langues":

    st.markdown(
        "<div class='section-title'>Langues</div>",
        unsafe_allow_html=True
    )

    columns = st.columns(4)

    for index, langue in enumerate(langues):

        with columns[index]:

            st.markdown(
                f"""
<div class="card" style="text-align:center;">

<div style="font-size:38px;">
🌐
</div>

<div class="card-title">
{langue[0]}
</div>

<div style="
color:#1f5f8b;
font-weight:700;
margin-top:10px;
">
{langue[1]}
</div>

</div>
""",
                unsafe_allow_html=True
            )


# ============================================================
# CENTRES D'INTERET
# ============================================================

elif page == "⭐ Centres d'intérêt":

    st.markdown(
        "<div class='section-title'>Centres d'intérêt</div>",
        unsafe_allow_html=True
    )

    columns = st.columns(3)

    for index, item in enumerate(interets):

        icone = item[0]
        titre = item[1]

        with columns[index % 3]:

            st.markdown(
                f"""
<div class="card" style="text-align:center;">

<div style="font-size:40px;">
{icone}
</div>

<div class="card-title">
{titre}
</div>

</div>
""",
                unsafe_allow_html=True
            )


# ============================================================
# CONTACT
# ============================================================

elif page == "📞 Contact":

    st.markdown(
        "<div class='section-title'>Contact</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
<div class="contact-card">

<div class="contact-icon">
📱
</div>

<div class="contact-title">
Téléphone
</div>

<div class="contact-value">
{telephone}
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            f"""
<div class="contact-card">

<div class="contact-icon">
📧
</div>

<div class="contact-title">
Email
</div>

<div class="contact-value">
{email}
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            f"""
<div class="contact-card">

<div class="contact-icon">
📍
</div>

<div class="contact-title">
Adresse
</div>

<div class="contact-value">
{adresse}
</div>

</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">

<strong>HAMIDOUCHE REDJDAL</strong>

<br><br>

Planificateur &amp; Superviseur Logistique

<br>

Logistique • Transport • Planification • Supervision • Optimisation

</div>
""",
    unsafe_allow_html=True
)
