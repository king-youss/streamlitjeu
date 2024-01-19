import streamlit as st
import random

# Définition des logos avec les liens fournis
logos = [
    {"name": "Apple", "image": "https://freepngimg.com/thumb/apple_logo/28105-1-apple-logo.png"},
    {"name": "Google", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/363px-Google_2015_logo.svg.png"},
    {"name": "Microsoft", "image": "https://news-cdn.softpedia.com/images/news2/Microsoft-Redesigns-Its-Logo-for-the-First-Time-in-25-Years-Here-It-Is-3.png"},
    {"name": "Amazon", "image": "https://pngimg.com/uploads/amazon/amazon_PNG11.png"},
    {"name": "Facebook", "image": "https://pngimg.com/uploads/facebook_logos/facebook_logos_PNG19753.png"},
    {"name": "Twitter", "image": "https://pngimg.com/uploads/twitter/twitter_PNG3.png"},
    {"name": "LinkedIn", "image": "https://pngimg.com/uploads/linkedIn/linkedIn_PNG27.png"},
    # Ajoutez autant de logos que vous le souhaitez avec les noms correspondants et les liens vers les images
]

# Définition du style CSS pour améliorer l'apparence
css = """
    body {
        background-color: #f8f9fa;
        font-family: 'Helvetica', sans-serif;
    }
    .stApp {
        max-width: 800px;
        margin: auto;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .stButton {
        font-size: 18px;
        padding: 10px 20px;
        margin-top: 20px;
    }
    .image-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
        border: 2px solid #dee2e6;
        border-radius: 10px;
        padding: 10px;
    }
    .score-container {
        text-align: center;
        margin-top: 20px;
        padding: 10px;
        background-color: #f0f0f0;
        border-radius: 5px;
    }
    .progress-container {
        margin-top: 10px;
    }
    .progress-bar {
        background-color: #28a745;
        border-radius: 5px;
    }
    .button-label {
        color: white;
    }
"""

def main():
    st.title("Devine le Logo")
    
    # Ajout du style CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

    if "game_state" not in st.session_state:
        st.session_state.game_state = {
            "current_logo": None,
            "options": [],
            "score": 0,
            "questions_answered": 0,
            "incorrect_answers": 0
        }
    
    # Démarrer le jeu si ce n'est pas déjà fait
    if not st.session_state.game_state["current_logo"]:
        start_game()

    # Centrer l'image
    st.markdown('<div class="image-container"></div>', unsafe_allow_html=True)
    logo_container = st.empty()
    logo_container.image(st.session_state.game_state["current_logo"]["image"], caption="Devine le logo", width=300)

    # Affichage des boutons de propositions
    selected_option = st.radio("Quel est le nom du logo?", [option["name"] for option in st.session_state.game_state["options"]])

    # Vérification de la réponse
    if st.button("Vérifier", key="verify_button"):
        st.session_state.game_state["questions_answered"] += 1
        if selected_option == st.session_state.game_state["current_logo"]["name"]:
            st.success("Bravo! C'est le bon logo.")
            st.session_state.game_state["score"] += 1
        else:
            st.error("Mauvaise réponse. Essaye à nouveau.")
            st.session_state.game_state["incorrect_answers"] += 1
        if st.session_state.game_state["questions_answered"] < 10:
            start_game()
            # Rerun l'application après chaque réponse
            st.experimental_rerun()
        else:
            st.success("La partie est terminée. Merci d'avoir joué!")
            st.write(f"Score final : {st.session_state.game_state['score']}")
            st.write(f"Mauvaises réponses : {st.session_state.game_state['incorrect_answers']}")
            st.session_state.game_state["questions_answered"] = 0
            st.session_state.game_state["score"] = 0
            st.session_state.game_state["incorrect_answers"] = 0

    # Affichage du score et du nombre de questions répondues pendant la partie
    st.markdown('<div class="score-container"></div>', unsafe_allow_html=True)
    st.write(f"Score : {st.session_state.game_state['score']}")
    st.write(f"Questions répondues : {st.session_state.game_state['questions_answered']}/10")
    st.write("---")

# Fonction pour démarrer une nouvelle manche du jeu
def start_game():
    st.session_state.game_state["current_logo"] = random.choice(logos)
    st.session_state.game_state["options"] = generate_options()

# Fonction pour générer les options pour chaque manche
def generate_options():
    current_logo = st.session_state.game_state["current_logo"]
    other_logos = random.sample([logo for logo in logos if logo != current_logo], 3)
    options = random.sample([current_logo] + other_logos, 4)
    return options

# Exécution du jeu
if __name__ == "__main__":
    main()
