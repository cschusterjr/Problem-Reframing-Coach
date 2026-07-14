import streamlit as st


def render_revision_form(scenario, api_base_url, requests):
    st.markdown("#### Revised Response")

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

    st.metric("Reframing Score", f"{feedback['score']}/10")

    st.markdown(
        f"""
        <div class="report-card">
            <div class="small-label">Original Frame</div>
            <p>{feedback["original_frame"]}</p>
        </div>

        <div class="report-card">
            <div class="small-label">Better Frame</div>
            <p>{feedback["better_frame"]}</p>
        </div>

        <div class="report-card">
            <div class="small-label">Hidden Assumption</div>
            <p>{feedback["hidden_assumption"]}</p>
        </div>

        <div class="report-card">
            <div class="small-label">Simple Solution</div>
            <p>{feedback["simple_solution"]}</p>
        </div>

        <div class="takeaway">
            <strong>Key Takeaway</strong>
            <p>{feedback["key_takeaway"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("#### Coaching Feedback")
    st.write(feedback["feedback"])

    st.markdown("#### Reflection Prompt")
    st.write(feedback["reflection_prompt"])

    st.markdown("#### Where This Skill Applies")
    for application in feedback.get("real_world_applications", []):
        st.write(f"- {application}")

    if st.button("Try Another Challenge"):
        st.session_state.clear()
        st.session_state["step"] = "welcome"
        st.rerun()