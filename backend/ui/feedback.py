import streamlit as st


def render_revision_form(scenario, api_base_url, requests):
    revised_response = st.text_area(
        "Revise your answer after considering the coaching questions.",
        height=150,
        placeholder="Write your revised solution here..."
    )

    if st.button("Get Feedback", type="primary"):
        if not revised_response.strip():
            st.warning("Please write a revised answer before getting feedback.")
            return

        feedback_response = requests.post(
            f"{api_base_url}/feedback",
            json={
                "scenario_id": scenario["id"],
                "initial_response": st.session_state["initial_response"],
                "revised_response": revised_response
            }
        )

        st.session_state["feedback"] = feedback_response.json()
        st.session_state["step"] = "feedback"
        st.rerun()


def render_feedback_report():
    feedback = st.session_state["feedback"]

    st.markdown("### Step 3 of 3: Cognitive Flexibility Report")
    st.progress(1.0)

    st.metric("Score", f"{feedback['score']}/10")

    st.markdown("#### Original Frame")
    st.write(feedback["original_frame"])

    st.markdown("#### Better Frame")
    st.write(feedback["better_frame"])

    st.markdown("#### Hidden Assumption")
    st.write(feedback["hidden_assumption"])

    st.markdown("#### Simple Solution")
    st.write(feedback["simple_solution"])

    st.markdown("#### Coaching Feedback")
    st.write(feedback["feedback"])

    st.markdown("#### Key Takeaway")
    st.success(feedback.get("key_takeaway", "Pause before solving. Question the frame before choosing a solution."))

    st.markdown("#### Reflection Prompt")
    st.write(feedback.get("reflection_prompt", "Where else could you apply this thinking strategy?"))

    st.markdown("#### Where This Skill Applies")
    for application in feedback.get("real_world_applications", []):
        st.write(f"- {application}")

    if st.button("Try Again"):
        st.session_state.clear()
        st.session_state["step"] = "welcome"
        st.rerun()