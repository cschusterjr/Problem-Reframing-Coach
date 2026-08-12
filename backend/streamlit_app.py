import os

import requests
import streamlit as st

from ui.coaching import (
    render_coaching_questions,
    render_initial_response_form,
)
from ui.dashboard import render_dashboard
from ui.feedback import (
    render_feedback_report,
    render_revision_form,
)
from ui.history import render_learning_history
from ui.scenario import (
    render_scenario_card,
    render_scenario_selector,
)
from ui.styles import apply_styles
from ui.welcome import render_welcome


API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "http://127.0.0.1:8001",
)


def load_scenarios(api_base_url: str) -> list[dict]:
    """
    Load scenarios from the FastAPI backend.

    Returns an empty list when the backend cannot be reached so the
    Streamlit interface can display a friendly error instead of crashing.
    """

    try:
        response = requests.get(
            f"{api_base_url}/scenarios",
            timeout=10,
        )
        response.raise_for_status()

        scenarios = response.json()

        if not isinstance(scenarios, list):
            st.error(
                "The coaching service returned an unexpected response."
            )
            return []

        return scenarios

    except requests.exceptions.ConnectionError:
        st.error(
            "The coaching service is unavailable. "
            "Start the FastAPI backend on port 8001, then refresh this page."
        )

    except requests.exceptions.Timeout:
        st.error(
            "The coaching service took too long to respond. "
            "Confirm that FastAPI is running, then try again."
        )

    except requests.exceptions.HTTPError as error:
        status_code = (
            error.response.status_code
            if error.response is not None
            else "unknown"
        )

        st.error(
            "The coaching service returned an error. "
            f"Status code: {status_code}"
        )

    except requests.exceptions.JSONDecodeError:
        st.error(
            "The coaching service returned invalid data."
        )

    except requests.exceptions.RequestException as error:
        st.error(
            f"Unable to connect to the coaching service: {error}"
        )

    return []


st.set_page_config(
    page_title="Problem Reframing Coach",
    page_icon="🧠",
    layout="centered",
)

apply_styles()


# ---------------------------------------------------------
# Navigation state
# ---------------------------------------------------------

if "navigation" not in st.session_state:
    st.session_state["navigation"] = "Dashboard"

if "requested_navigation" in st.session_state:
    st.session_state["navigation"] = st.session_state.pop(
        "requested_navigation"
    )


# ---------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Practice",
        "Learning History",
    ],
    key="navigation",
)


# ---------------------------------------------------------
# Dashboard
# ---------------------------------------------------------

if page == "Dashboard":
    render_dashboard(API_BASE_URL)
    st.stop()


# ---------------------------------------------------------
# Learning History
# ---------------------------------------------------------

if page == "Learning History":
    render_learning_history(API_BASE_URL)
    st.stop()


# ---------------------------------------------------------
# Practice
# ---------------------------------------------------------

if "step" not in st.session_state:
    st.session_state["step"] = "welcome"


scenarios = load_scenarios(API_BASE_URL)

if not scenarios:
    st.info(
        "FastAPI can be started from the backend folder with:"
    )

    st.code(
        "python -m uvicorn app.main:app --reload --port 8001",
        language="powershell",
    )

    st.stop()


if "selected_scenario" not in st.session_state:
    st.session_state["selected_scenario"] = scenarios[0]


scenario = st.session_state["selected_scenario"]


if st.session_state["step"] == "welcome":
    render_welcome()

    selected_scenario = render_scenario_selector(
        scenarios
    )

    st.session_state[
        "selected_scenario"
    ] = selected_scenario


elif st.session_state["step"] == "challenge":
    render_scenario_card(
        scenario
    )

    render_initial_response_form(
        scenario,
        API_BASE_URL,
        requests,
    )


elif st.session_state["step"] == "coaching":
    render_coaching_questions()

    render_revision_form(
        scenario,
        API_BASE_URL,
        requests,
    )


elif st.session_state["step"] == "feedback":
    render_feedback_report()


else:
    st.error(
        "The application entered an unknown state. "
        "Resetting the learning experience."
    )

    st.session_state["step"] = "welcome"
    st.rerun()