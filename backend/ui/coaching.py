import streamlit as st


def render_initial_response_form(scenario, api_base_url, requests):
    initial_response = st.text_area(
        "What would you do first?",
        height=150,
        placeholder="Write your initial solution here..."
    )

    if st.button("Submit Initial Answer", type="primary"):
        if not initial_response.strip():
            st.warning("Please write an initial answer before continuing.")
            return

        coach_response = requests.post(
            f"{api_base_url}/coach",
            json={
                "scenario_id": scenario["id"],
                "user_response": initial_response
            }
        )

        st.session_state["initial_response"] = initial_response
        st.session_state["coaching_questions"] = coach_response.json()["coaching_questions"]
        st.session_state["step"] = "coaching"
        st.rerun()


def render_coaching_questions():
    st.markdown("### Step 2 of 3: Pause and Reframe")
    st.progress(0.66)

    st.write("Before revising your answer, consider these coaching questions:")

    for question in st.session_state["coaching_questions"]:
        st.write(f"- {question}")