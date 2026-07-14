import requests
import streamlit as st

from ui.styles import apply_styles
from ui.welcome import render_welcome
from ui.scenario import render_scenario_selector, render_scenario_card
from ui.coaching import render_initial_response_form, render_coaching_questions
from ui.feedback import render_revision_form, render_feedback_report

API_BASE_URL = "http://127.0.0.1:8001"

st.set_page_config(
    page_title="Problem Reframing Coach",
    page_icon="🧠",
    layout="centered"
)

apply_styles()

if "step" not in st.session_state:
    st.session_state["step"] = "welcome"

scenario_response = requests.get(f"{API_BASE_URL}/scenarios")
scenarios = scenario_response.json()
if "selected_scenario" not in st.session_state:
    st.session_state["selected_scenario"] = scenarios[0]

scenario = st.session_state["selected_scenario"]

if st.session_state["step"] == "welcome":
    render_welcome()
    st.markdown("### Choose a challenge")
    selected_scenario = render_scenario_selector(scenarios)
    st.session_state["selected_scenario"] = selected_scenario

elif st.session_state["step"] == "challenge":
    render_scenario_card(scenario)
    render_initial_response_form(scenario, API_BASE_URL, requests)

elif st.session_state["step"] == "coaching":
    render_coaching_questions()
    render_revision_form(scenario, API_BASE_URL, requests)

elif st.session_state["step"] == "feedback":
    render_feedback_report()