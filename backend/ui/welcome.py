import streamlit as st


def render_welcome():
    st.title("Problem Reframing Coach")
    st.caption("Learn to identify assumptions, reframe problems, and find simpler solutions.")

    st.markdown("---")

    st.subheader("Most difficult problems are not solved with better answers.")
    st.write("They are often solved by asking better questions.")

    st.write(
        """
        In this challenge, you will practice a simple but powerful thinking routine:

        1. Understand the situation.
        2. Submit your first solution.
        3. Pause and question your assumptions.
        4. Revise your answer.
        5. Review your cognitive flexibility report.
        """
    )

    if st.button("Start Challenge", type="primary"):
        st.session_state["step"] = "challenge"
        st.rerun()