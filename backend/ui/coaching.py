import streamlit as st


def render_initial_response_form(scenario, api_base_url, requests):
    st.markdown("#### Your First Response")

    initial_response = st.text_area(
        "What would you do first?",
        height=150,
        placeholder="Write your initial solution here...",
    )

    if st.button("Submit Initial Answer", type="primary"):
        if not initial_response.strip():
            st.warning("Please write an initial answer before continuing.")
            return

        coach_response = requests.post(
            f"{api_base_url}/coach",
            json={
                "scenario_id": scenario["id"],
                "user_response": initial_response,
            },
            timeout=60,
        )

        if not coach_response.ok:
            st.error(
                "The coaching service returned an error. "
                f"Status code: {coach_response.status_code}"
            )
            return

        response_data = coach_response.json()

        st.session_state["initial_response"] = initial_response
        st.session_state["coaching_questions"] = response_data[
            "coaching_questions"
        ]
        st.session_state["step"] = "coaching"

        st.rerun()


def render_coaching_questions():
    stages = [
        {
            "label": "🧠 Step 1",
            "title": "Inspect Your Assumptions",
            "description": (
                "Pause and notice what may be shaping your first solution."
            ),
        },
        {
            "label": "🧱 Step 2",
            "title": "Challenge Fixed Constraints",
            "description": (
                "Consider whether every part of the problem is truly fixed."
            ),
        },
        {
            "label": "✂️ Step 3",
            "title": "Simplify Before Adding",
            "description": (
                "Look for something you could remove, reduce, separate, "
                "change, or test."
            ),
        },
        {
            "label": "🎯 Step 4",
            "title": "Reframe the Goal",
            "description": (
                "Focus on the outcome you need, not the method you first chose."
            ),
        },
    ]

    st.markdown("## Step 2 of 3: Pause and Reframe")
    st.progress(0.66)

    st.info(
        "Good problem solvers do not immediately improve their first solution. "
        "They first improve how they understand the problem."
    )

    questions = st.session_state.get("coaching_questions", [])

    if not questions:
        st.warning(
            "No coaching questions are available. "
            "Return to the challenge and submit an initial response."
        )
        return

    for stage, question in zip(stages, questions):
        st.markdown(
            f"### {stage['label']} - {stage['title']}"
        )
        st.caption(stage["description"])
        st.write(question)
        st.divider()