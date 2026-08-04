import streamlit as st


def render_revision_form(scenario, api_base_url, requests):
    st.markdown("#### Revised Response")

    revised_response = st.text_area(
        "Revise your answer after considering the coaching questions.",
        height=150,
        placeholder="Write your revised solution here...",
    )

    if st.button("Get Feedback", type="primary"):
        if not revised_response.strip():
            st.warning(
                "Please write a revised answer before getting feedback."
            )
            return

        try:
            feedback_response = requests.post(
                f"{api_base_url}/feedback",
                json={
                    "scenario_id": scenario["id"],
                    "initial_response": st.session_state[
                        "initial_response"
                    ],
                    "revised_response": revised_response,
                },
                timeout=60,
            )

            feedback_response.raise_for_status()
            feedback_data = feedback_response.json()

        except requests.exceptions.ConnectionError:
            st.error(
                "The coaching service is unavailable. "
                "Confirm that FastAPI is running, then try again."
            )
            return

        except requests.exceptions.Timeout:
            st.error(
                "The assessment took too long to complete. "
                "Please try again."
            )
            return

        except requests.exceptions.HTTPError:
            st.error(
                "The coaching service could not generate feedback. "
                f"Status code: {feedback_response.status_code}"
            )
            return

        except requests.exceptions.JSONDecodeError:
            st.error(
                "The coaching service returned an invalid response."
            )
            return

        except requests.exceptions.RequestException as error:
            st.error(
                f"Unable to retrieve feedback: {error}"
            )
            return

        st.session_state["feedback"] = feedback_data
        st.session_state["step"] = "feedback"
        st.rerun()


def render_feedback_report():
    feedback = st.session_state["feedback"]

    st.markdown("### Step 3 of 3: Cognitive Flexibility Report")
    st.progress(1.0)

    overall_score = feedback.get("overall_rubric_score", 0)
    rubric_dimensions = feedback.get("rubric_dimensions", [])

    st.metric(
        "Overall Cognitive Score",
        f"{overall_score:.1f}/5",
    )

    if rubric_dimensions:
        strongest_dimension = max(
            rubric_dimensions,
            key=lambda dimension: dimension.get("score", 0),
        )

        growth_dimension = min(
            rubric_dimensions,
            key=lambda dimension: dimension.get("score", 0),
        )

        strength_column, growth_column = st.columns(2)

        with strength_column:
            st.success(
                f"**Top Strength**\n\n"
                f"{strongest_dimension['name']} "
                f"({strongest_dimension['score']}/5)"
            )

        with growth_column:
            st.warning(
                f"**Next Growth Area**\n\n"
                f"{growth_dimension['name']} "
                f"({growth_dimension['score']}/5)"
            )

        st.markdown("#### Cognitive Skill Breakdown")

        for dimension in rubric_dimensions:
            score = dimension.get("score", 0)
            name = dimension.get(
                "name",
                "Assessment Dimension",
            )
            dimension_feedback = dimension.get(
                "feedback",
                "",
            )

            filled_stars = "★" * score
            empty_stars = "☆" * (5 - score)

            st.markdown(f"### {name}")
            st.markdown(
                f"**{filled_stars}{empty_stars}** "
                f"({score}/5)"
            )
            st.progress(score / 5)
            st.write(dimension_feedback)
            st.divider()

    else:
        st.warning(
            "Detailed rubric results were not available."
        )

    st.markdown("#### Coaching Summary")
    st.write(feedback["feedback"])

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
        unsafe_allow_html=True,
    )

    st.markdown("#### Reflection Prompt")
    st.write(feedback["reflection_prompt"])

    st.markdown("#### Where This Skill Applies")

    for application in feedback.get(
        "real_world_applications",
        [],
    ):
        st.write(f"- {application}")

    if st.button("Try Another Challenge"):
        st.session_state.clear()
        st.session_state["step"] = "welcome"
        st.rerun()