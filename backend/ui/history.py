import streamlit as st
import requests


def render_learning_history(api_base_url: str):
    st.markdown("# 📚 Learning History")

    try:
        response = requests.get(
            f"{api_base_url}/attempts",
            timeout=10,
        )

        response.raise_for_status()

        attempts = response.json()

    except requests.exceptions.RequestException:
        st.warning(
            "Unable to load learning history."
        )
        return

    if not attempts:
        st.info(
            "No completed learning attempts yet."
        )
        return

    for attempt in attempts:

        with st.expander(
            f"{attempt['scenario_id']} • "
            f"{attempt['overall_score']:.1f}/5"
        ):

            st.write(
                "**Completed:**",
                attempt["timestamp"],
            )

            st.write(
                "**Initial Response**"
            )

            st.write(
                attempt["initial_response"]
            )

            st.write(
                "**Revised Response**"
            )

            st.write(
                attempt["revised_response"]
            )

            st.write(
                "**Key Takeaway**"
            )

            st.success(
                attempt["key_takeaway"]
            )