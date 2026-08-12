import requests
import streamlit as st


def render_dashboard(api_base_url: str):
    st.markdown("# 🧠 Learner Dashboard")
    st.caption(
        "Track your cognitive growth and continue building better "
        "problem-reframing habits."
    )

    try:
        response = requests.get(
            f"{api_base_url}/analytics/summary",
            timeout=10,
        )
        response.raise_for_status()
        analytics = response.json()

    except requests.exceptions.ConnectionError:
        st.error(
            "The coaching service is unavailable. "
            "Confirm that FastAPI is running."
        )
        return

    except requests.exceptions.Timeout:
        st.error(
            "The analytics service took too long to respond."
        )
        return

    except requests.exceptions.RequestException as error:
        st.error(
            f"Unable to load learner analytics: {error}"
        )
        return

    challenges_completed = analytics.get(
        "challenges_completed",
        0,
    )

    average_score = analytics.get(
        "average_score",
        0.0,
    )

    strongest_skill = analytics.get(
        "strongest_skill"
    )

    growth_area = analytics.get(
        "growth_area"
    )

    metric_column_1, metric_column_2 = st.columns(2)

    with metric_column_1:
        st.metric(
            "Challenges Completed",
            challenges_completed,
        )

    with metric_column_2:
        st.metric(
            "Average Cognitive Score",
            f"{average_score:.1f}/5",
        )

    st.markdown("### Cognitive Profile")

    profile_column_1, profile_column_2 = st.columns(2)

    with profile_column_1:
        if strongest_skill:
            st.success(
                f"**Strongest Skill**\n\n{strongest_skill}"
            )
        else:
            st.info(
                "Complete a challenge to identify your strongest skill."
            )

    with profile_column_2:
        if growth_area:
            st.warning(
                f"**Growth Area**\n\n{growth_area}"
            )
        else:
            st.info(
                "Complete a challenge to identify your growth area."
            )

    st.markdown("---")

    st.markdown("### Keep Practicing")

    if challenges_completed == 0:
        st.write(
            "Complete your first challenge to begin tracking "
            "your cognitive growth."
        )
    else:
        st.write(
            "Continue practicing to strengthen your reasoning "
            "across different cognitive skills."
        )

    if st.button(
        "Start a Challenge",
        type="primary",
    ):
        st.session_state["requested_navigation"] = "Practice"
        st.session_state["step"] = "welcome"
        st.rerun()