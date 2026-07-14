import streamlit as st


def render_scenario_selector(scenarios):
    scenario_options = {
        scenario["title"]: scenario
        for scenario in scenarios
    }

    selected_title = st.selectbox(
        "Choose a challenge",
        list(scenario_options.keys())
    )

    return scenario_options[selected_title]


def render_scenario_card(scenario):
    st.markdown("### Step 1 of 3: Understand")
    st.progress(0.33)

    st.markdown(
        f"""
        <div class="section-card">
            <div class="small-label">{scenario["category"]}</div>
            <h2>{scenario["title"]}</h2>
            <p class="muted">
                Difficulty: {scenario["difficulty"]} · Estimated time: {scenario["estimated_time"]}
            </p>
            <p>{scenario["scenario"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="section-card">
            <div class="small-label">Thinking Skill</div>
            <h3>{scenario["cognitive_skill"]}</h3>
            <p>{scenario["why_it_matters"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "Before answering, pause and ask: What is the actual goal? Which constraints are real, and which might be assumptions?"
    )