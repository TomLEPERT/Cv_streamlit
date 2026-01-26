import streamlit as st
from pathlib import Path

# --- Paths robustes (app.py est dans /src)
BASE_DIR = Path(__file__).resolve().parent

def pth(rel: str) -> Path:
    """Convertit un chemin relatif repo -> Path absolu."""
    return (BASE_DIR / rel).resolve()

# --- Page config
st.set_page_config(
    page_title="CV - Tom LEPERT",
    page_icon="📄",
    layout="wide",
)

# --- CSS
def load_css():
    css_path = pth("assets/styles.css")
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
    else:
        st.error(f"CSS introuvable: {css_path}")

load_css()

# ---------------- DATA PROJETS ----------------
PROJECTS = [
    {
        "id": "mimicom",
        "title": "MimiCom — Pilotage de campagnes mailing (Streamlit + FastAPI + MongoDB)",
        "desc": "Plateforme d’analyse et d’optimisation de campagnes mailing : centralisation prospects, KPIs, segmentation, import/export CSV et assistants ML (clustering, recommandations).",
        "tech": ["Python", "Streamlit", "FastAPI", "MongoDB", "Pandas", "Pydantic", "Scikit-learn", "Docker", "Matplotlib"],
        "cover": "assets/projects/mimicom/cover.png",
        "images_dir": "assets/projects/mimicom",
        "github": "https://github.com/TomLEPERT/MimiCom.git",
        "demo": None,
        "status": "🟡 En cours",
        "highlights": [
            "Auth + accès restreint",
            "Gestion prospects + détection doublons + logs modifications",
            "Import/Export CSV (prévisualisation, conflits, rapport d’import)",
            "Dashboard KPIs + drill-down & filtres dynamiques",
            "Campagnes : segmentation, suivi performance, historique",
            "Assistants ML : clustering, segmentation, templates, recommandations",
            "Architecture : Streamlit UI + FastAPI + MongoDB (Docker/Compose)",
        ],
        "details": {
            "Objectifs": [
                "Centraliser les prospects dans une base unique",
                "Faciliter la création/gestion de campagnes mailing",
                "Visualiser KPIs et performances",
                "Automatiser l’analyse via Machine Learning",
                "Rendre l’outil accessible à des utilisateurs non techniques",
            ],
            "Fonctionnalités": [
                "Authentification (connexion sécurisée, pages sensibles protégées)",
                "Prospects : dataset global, fiche détail, CRUD contrôlé, segmentation, dédoublonnage email/téléphone, journalisation",
                "CSV : import massif avec prévisualisation, détection erreurs/doublons, gestion conflits, rapport détaillé, export filtré + limitation anti-abus",
                "KPIs : géographie, types prospects, tailles audience, statuts, acceptation communication, données manquantes, jamais contactés, taux de retour, délai moyen réponse",
                "Campagnes : création, sous-base par campagne, historique, suivi performances, analyse par segment",
                "Assistants ML : clustering (K-Means), segmentation, génération templates, checklist/rétroplanning, recommandations stratégie",
                "Exports & sauvegardes : exports visuels/données, backup historique",
            ],
            "Architecture": [
                "Streamlit : UI",
                "FastAPI : logique métier + validation (Pydantic) + accès DB",
                "MongoDB : stockage prospects, logs, imports",
                "Services : prospects, imports CSV, exports CSV, KPIs",
                "Docker / Docker Compose : conteneurisation",
            ],
            "ML": [
                "Clustering (K-Means) pour segmentation",
                "Modèles supervisés (ex: Random Forest) envisagés pour recommandations/prédiction",
            ],
            "Équipe": [
                "Louisa Toudji",
                "Thomas Constantin",
                "Tom Lepert",
            ],
        },
    },
    {
        "id": "toys_models_bi",
        "title": "SQL & BI — Toys & Models",
        "desc": "Exploration d’une base transactionnelle, calcul de KPI en SQL, création de vues et modélisation en étoile pour Power BI.",
        "tech": ["MySQL", "SQL", "Power BI", "Data Modeling (OLTP→OLAP)", "Star Schema"],
        "cover": "assets/projects/toys_models_bi/cover.png",
        "images_dir": "assets/projects/toys_models_bi",
        "github": "https://github.com/TomLEPERT/DataAnalyst_Projet_1.git",
        "demo": None,
        "highlights": [
            "KPIs Ventes / Finances / Logistique / RH",
            "Requêtes SQL complexes + optimisation pour BI",
            "Vues SQL préparant tables de faits & dimensions",
            "Dashboard Power BI actualisable quotidiennement",
        ],
        "details": {
            "Contexte": "Entreprise de maquettes avec base de données existante (employés, produits, commandes, paiements…).",
            "Objectif": "Construire un dashboard dynamique pour le directeur, mis à jour chaque matin.",
            "Axes KPI": [
                "Ventes (CA par mois/région, best/worst produits par catégorie, etc.)",
                "Finances (clients +/-, recouvrement, paiements, croissance)",
                "Logistique (stocks sous seuil, délais traitement, retards)",
                "Ressources humaines (CA par commercial, perf bureaux, ratio commandes/paiements)",
            ],
            "Approche": [
                "Exploration du schéma transactionnel (OLTP) et des relations clés",
                "Requêtes SQL pour calculer les KPI demandés + propositions complémentaires",
                "Transformation en modèle analytique (OLAP) pour Power BI",
                "Création de vues SQL pour tables de faits/dimensions (star schema)",
                "Construction du dashboard Power BI (relations, filtres, KPIs, visuels)",
            ],
            "Livrables": [
                "Requêtes SQL KPI",
                "Vues SQL (fact/dim) prêtes pour Power BI",
                "Dashboard Power BI interactif et actualisable",
            ],
        },
    },
    {
        "id": "cinema_de_la_cite",
        "title": "Cinéma de la Cité — Reco films",
        "desc": "Application Streamlit : recherche multi-critères, fiches films détaillées, recommandations ML (Nearest Neighbors) + visualisations.",
        "tech": ["Python", "Streamlit", "Pandas", "NumPy", "JupyterLab", "Scikit-learn", "Matplotlib", "HTML/CSS", "API TMDB/IMDb"],
        "cover": "assets/projects/cinema_de_la_cite/cover.png",
        "images_dir": "assets/projects/cinema_de_la_cite",
        "github": "https://github.com/TomLEPERT/Projet_recommandation_film.git",
        "demo": "https://cinemadelacite.streamlit.app/",
        "highlights": [
            "Recherche par titre, genre, acteurs, production, année/décennie",
            "Stickers interactifs (hover + pagination)",
            "Fiche film complète (poster, synopsis API, casting, production)",
            "Recommandation ML : NearestNeighbors (cosine similarity)",
            "Page DataViz : genres, notes, acteurs fréquents, décennies…",
        ],
        "details": {
            "Contexte": "Projet Data/ML (Simplon) : base TMDB/IMDb nettoyée/enrichie, focus films français (popularité ≥ 6).",
            "Objectif": "Proposer une expérience de découverte de films : recherche + exploration + recommandations.",
            "Fonctionnalités": [
                "Recherche multi-critères avec résultats en cartes + pagination",
                "Stickers visuels (hover infos clés) et navigation vers fiche film",
                "Fiche film : affiche, synopsis (API), acteurs, production/scénaristes, note",
                "Reco : 5 films similaires via features (genres, réalisateurs, acteurs fréquents, année)",
                "5 films aléatoires au chargement (disparaissent après recherche)",
                "Page visualisation : top acteurs, répartition genres, distribution notes, etc.",
            ],
            "Approche ML": [
                "Encodage multi-label (genres / réalisateurs / acteurs fréquents)",
                "Normalisation des features",
                "Similarité cosinus + modèle NearestNeighbors",
            ],
            "Livrables": [
                "Application Streamlit déployée",
                "Pipeline de préparation des données (clean/enrich)",
                "Système de recommandation + page DataViz",
            ],
        },
    },
    {
        "id": "streamlit_never_sleep",
        "title": "Streamlit Never Sleep — Wake Apps (Actions + Playwright)",
        "desc": "Automatisation GitHub Actions + Playwright pour réveiller des apps Streamlit Cloud (cold start) chaque jour à 10h (heure FR), avec clic automatique sur le bouton de démarrage.",
        "tech": ["Python", "GitHub Actions", "Playwright", "Cron (UTC)", "Automation", "Streamlit Cloud"],
        "cover": "assets/projects/streamlit_never_sleep/cover.png",
        "images_dir": "assets/projects/streamlit_never_sleep",
        "github": "https://github.com/TomLEPERT/Streamlit_nerver_sleep.git",
        "demo": None,
        "highlights": [
            "Réveil quotidien à 10h (heure française) — été + hiver",
            "Vrai navigateur headless (Chromium) via Playwright",
            "Clic automatique sur bouton (yes/start/run/launch...)",
            "Logs clairs dans GitHub Actions — 100% gratuit, sans serveur",
        ],
        "details": {
            "Problème": "Les apps Streamlit Cloud passent en cold start après inactivité, parfois avec un bouton à cliquer pour relancer l’app.",
            "Solution": "Un workflow GitHub Actions lance un script Python qui ouvre l’app via Playwright, attend l’UI, clique le bouton et force un rerun.",
            "Fonctionnalités": [
                "Réveil automatique des apps",
                "Gestion des cold starts même avec bouton obligatoire",
                "Planification quotidienne à 10h heure FR (gestion été/hiver via 2 crons UTC)",
                "Clic basé sur mots-clés (fallback sur premier bouton visible)",
                "Logs dans Actions",
                "Gratuit (aucun serveur requis)",
            ],
            "Comment ça marche": [
                "GitHub Actions exécute wake.py selon un cron",
                "Playwright lance Chromium en headless",
                "Ouverture de chaque URL Streamlit",
                "Attente chargement UI",
                "Clic auto du bouton identifié via KEYWORDS",
            ],
            "Configuration": [
                "Modifier SITES (liste d’URLs Streamlit)",
                "Adapter KEYWORDS (texte du bouton à cliquer)",
                "Activer Actions et tester via workflow_dispatch",
            ],
            "Bonnes pratiques": [
                "1 réveil/jour suffit",
                "Éviter les refresh agressifs",
                "Réservé à ses propres apps",
            ],
        },
    },
    {
        "id": "poe2_trade_analyzer",
        "title": "PoE2 Trade Analyzer — Arbitrage & Scoring",
        "desc": "Outil Streamlit d’analyse du marché PoE2 : taux de change croisés Chaos/Divine/Exalted, liquidité/volumes, et détection automatique d’opportunités d’arbitrage avec scoring.",
        "tech": ["Python", "Streamlit", "JSON", "Data Analysis", "Scoring"],
        "cover": "assets/projects/poe2_trade_analyzer/cover.png",
        "images_dir": "assets/projects/poe2_trade_analyzer",
        "github": "https://github.com/TomLEPERT/poe2-trade-analyzer.git",
        "demo": None,
        "highlights": [
            "Overview : taux de change croisés + volumes + liquidité",
            "Scanner d’opportunités : slippage achat/vente + filtres liquidité/profit",
            "Métriques : Profit %, profit/unité, volume exploitable, priorité",
            "Scoring anti-faux-positifs : profit × √liquidité × spread factor",
        ],
        "details": {
            "But": "Repérer rapidement des opportunités d’arbitrage exploitables entre Chaos / Divine / Exalted, en tenant compte des contraintes de marché (liquidité, spread, slippage).",
            "Modules": [
                "Overview : état global du marché, taux de change croisés, volumes, indicateurs de liquidité, accès au détail d’une devise",
                "Opportunities Scanner : comparaison multi-paires (C↔D, C↔E, D↔E), application de slippage, filtres liquidité/profit, tri par score",
            ],
            "Métriques calculées": [
                "Profit (%)",
                "Profit par unité",
                "Volume exploitable",
                "Score de priorité (exploitabilité)",
            ],
            "Scoring": [
                "Score = Profit% × √(liquidité) × SpreadFactor + Bonus(profit valeur)",
                "Objectif : éviter les opportunités théoriques impossibles à exécuter (faible liquidité) ou peu rentables",
            ],
            "Données": [
                "Ingestion de données de marché au format JSON",
                "Calculs et agrégations côté Python",
            ],
        },
    },
    {
        "id": "nutrifood",
        "title": "NutriFood — Substituts alimentaires (Django)",
        "desc": "Application Django : recherche de produits alimentaires et proposition automatique d’alternatives plus saines via Nutri-Score et catégories (OpenFoodFacts API).",
        "tech": ["Python", "Django 5.2", "PostgreSQL", "HTML", "CSS", "OpenFoodFacts API", "Tests"],
        "cover": "assets/projects/nutrifood/cover.png",
        "images_dir": "assets/projects/nutrifood",
        "github": "https://github.com/TomLEPERT/NutriFood",
        "demo": None,
        "highlights": [
            "Recherche produits par nom ou catégorie",
            "Proposition automatique de substitut plus sain",
            "Badges Nutri-Score colorés",
            "Import automatisé OpenFoodFacts (commande Django)",
            "Tests Django (modèles, vues, logique métier)",
        ],
        "details": {
            "Contexte": "Projet Data Analyst (Simplon) : application web pour aider à choisir des alternatives alimentaires plus saines.",
            "Objectif": "Proposer un substitut nutritionnellement meilleur pour un produit donné, basé sur Nutri-Score et catégorie.",
            "Fonctionnalités": [
                "Recherche par nom ou catégorie",
                "Page de détail produit",
                "Suggestion visuelle d’un substitut plus sain",
                "Badges Nutri-Score colorés",
                "Layout responsive",
                "Commande Django pour importer les produits depuis OpenFoodFacts",
                "Tests unitaires Django (TestCase)",
            ],
            "Algorithme": [
                "Sélection du premier produit trouvé comme référence",
                "Recherche de produits de catégorie proche",
                "Filtrage sur Nutri-Score meilleur",
                "Classement par Nutri-Score puis par nom",
                "Proposition du meilleur candidat",
            ],
            "Stack": [
                "Backend : Django 5.2",
                "Base de données : PostgreSQL",
                "Frontend : HTML5 / CSS3",
                "Données : OpenFoodFacts API",
                "Tests : Django TestCase",
            ],
            "Améliorations possibles": [
                "Pagination des résultats",
                "Authentification utilisateur",
                "Favoris & historique",
                "Filtrage par catégorie",
                "API REST (Django Rest Framework)",
                "Score nutritionnel plus précis",
            ],
        },
    },
]

by_id = {p["id"]: p for p in PROJECTS}
st.session_state.setdefault("selected_project", None)

# ---------------- Helpers UI ----------------
IMG_EXT = {".jpg", ".jpeg", ".png", ".webp"}

def show_image(path: Path, **kwargs):
    if path.exists():
        st.image(str(path), **kwargs)
        return True
    return False

# ---------------- Sidebar ----------------
with st.sidebar:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">TOM LEPERT</div>
          <div class="muted">Data Engineer — Recherche d’alternance</div>
          <div class="accent"></div>
          <div class="muted">France</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Photo
    photo = pth("assets/img/portrait.jpg")
    if photo.exists():
        st.image(str(photo), use_container_width=True)

    # CV
    cv_path = pth("assets/cv/CV_2026_LEPERT_TOM.pdf")
    if cv_path.exists():
        with open(cv_path, "rb") as f:
            st.download_button(
                "Télécharger mon CV (PDF)",
                data=f,
                file_name="CV_TOM_LEPERT.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

    st.markdown(
        """
        <div class="card">
          <div class="card-title">Liens</div>
          <div class="muted">Me contacter</div>
          <div class="accent"></div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.link_button("LinkedIn", "https://www.linkedin.com/in/tom-lepert", use_container_width=True)
    st.link_button("GitHub", "https://github.com/TomLEPERT", use_container_width=True)
    st.markdown("📧 **tom.lepert@laposte.net**")

# ---------------- Hero ----------------
st.markdown(
    """
    <div class="hero">
      <h1>Bonjour, moi c’est Tom</h1>
      <p>
        Reconversion restauration → web → data. Aujourd’hui je me spécialise en <b>Data Engineering</b>
        et je recherche une <b>alternance de 18 mois</b> à partir du <b>16 mars 2026</b>.
        J’aime construire des solutions data utiles, avec du sens : <b>recherche scientifique</b>, <b>santé</b>,
        <b>éducation</b>, <b>inclusion</b>, <b>innovation sociale</b>.
      </p>
      <div class="hero-row">
        <span class="hero-pill">🧪 Connaissance</span>
        <span class="hero-pill">🧠 Cognition</span>
        <span class="hero-pill">🌱 Éco-responsable</span>
        <span class="hero-pill">🤝 Inclusif</span>
        <span class="hero-pill">🐍 Python</span>
        <span class="hero-pill">🗄️ SQL</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("## Mes projets")

# ---------------- Cartes projets ----------------
def project_card(p):
    st.markdown('<div class="pcard">', unsafe_allow_html=True)

    # Cover (chemin absolu)
    cover = pth(p["cover"])
    if not show_image(cover, use_container_width=True):
        st.info(f"Cover introuvable : {p['cover']}")

    st.markdown(f'<div class="ptitle">{p["title"]}</div>', unsafe_allow_html=True)

    if p.get("status"):
        st.markdown(f"<div class='muted' style='margin-top:-6px; margin-bottom:8px'>{p['status']}</div>", unsafe_allow_html=True)

    st.markdown(f'<div class="pdesc">{p["desc"]}</div>', unsafe_allow_html=True)

    badges_html = "".join([f'<span class="badge know">{t}</span>' for t in p["tech"]])
    st.markdown(f'<div class="badges">{badges_html}</div>', unsafe_allow_html=True)

    if p.get("highlights"):
        st.markdown(
            "<ul style='margin:10px 0 0 16px; color: var(--muted);'>"
            + "".join([f"<li>{h}</li>" for h in p["highlights"][:4]])
            + "</ul>",
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="small")
    with c1:
        if st.button("Voir le projet →", key=f"open_{p['id']}", use_container_width=True):
            st.session_state["selected_project"] = p["id"]

    with c2:
        if p.get("demo"):
            st.link_button("Démo", p["demo"], use_container_width=True)
        elif p.get("github"):
            st.link_button("Repo GitHub", p["github"], use_container_width=True)
        else:
            st.button("Repo privé", disabled=True, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

cols = st.columns(2, gap="large")
for i, p in enumerate(PROJECTS):
    with cols[i % 2]:
        project_card(p)

# ---------------- Détail projet ----------------
if st.session_state["selected_project"]:
    p = by_id[st.session_state["selected_project"]]

    st.markdown("<div style='height:26px'></div>", unsafe_allow_html=True)
    st.markdown(f"## {p['title']}")
    st.write(p["desc"])
    st.caption("Tech : " + " • ".join(p["tech"]))

    # Boutons
    b1, b2 = st.columns(2)
    with b1:
        if p.get("github"):
            st.link_button("Voir sur GitHub", p["github"], use_container_width=True)
        else:
            st.button("Repo privé", disabled=True, use_container_width=True)
    with b2:
        if p.get("demo"):
            st.link_button("Ouvrir la démo", p["demo"], use_container_width=True)

    # Highlights
    if p.get("highlights"):
        st.markdown("### Points clés")
        for h in p["highlights"]:
            st.write(f"- {h}")

    # Détails (toutes les sections)
    d = p.get("details", {})
    if d:
        st.markdown("### Détails")
        for section, content in d.items():
            st.markdown(f"#### {section}")
            if isinstance(content, list):
                for item in content:
                    st.write(f"- {item}")
            else:
                st.write(content)

    # Captures
    img_dir = pth(p["images_dir"])
    if img_dir.exists():
        imgs = sorted([x for x in img_dir.iterdir() if x.suffix.lower() in IMG_EXT])
        imgs = [x for x in imgs if x.name.lower() not in {"cover.jpg","cover.jpeg","cover.png","cover.webp"}]
        if imgs:
            st.markdown("### Captures")
            st.image([str(x) for x in imgs], use_container_width=True)
        else:
            st.info(f"Aucune capture dans : {p['images_dir']}")
    else:
        st.info(f"Dossier images introuvable : {p['images_dir']}")

    if st.button("← Retour aux projets", use_container_width=True):
        st.session_state["selected_project"] = None

# ---------------- Footer ----------------
st.markdown(
    """
    <div class="footer">
      © 2026 Tom Lepert — <a href="https://www.linkedin.com/in/tom-lepert" target="_blank">LinkedIn</a> •
      <a href="https://github.com/TomLEPERT" target="_blank">GitHub</a> •
      <a href="mailto:tom.lepert@laposte.net">tom.lepert@laposte.net</a>
    </div>
    """,
    unsafe_allow_html=True
)
