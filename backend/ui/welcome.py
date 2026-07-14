import streamlit as st


def render_welcome():
    st.markdown(
        """
        <div class="hero-card">
            <div class="small-label">AI Learning Product Demo</div>
            <h1>Problem Reframing Coach</h1>
            <p class="muted">
                Practice identifying hidden assumptions, reframing problems, and finding simpler solutions.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Most difficult problems are not solved with better answers.")
    st.write("They are often solved by asking better questions.")

    st.markdown(
        """
        This experience guides learners through a structured thinking routine:

        1. Understand the problem.
        2. Submit an initial solution.
        3. Pause and question assumptions.
        4. Revise the response.
        5. Review a cognitive flexibility report.
        """
    )

    st.info(
        "The goal is not to give learners the answer. The goal is to coach better thinking."
    )

    if st.button("Start Challenge", type="primary"):
        st.session_state["step"] = "challenge"
        st.rerun()