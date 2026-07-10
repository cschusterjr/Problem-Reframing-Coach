import streamlit as st


def apply_styles():
    st.markdown(
        """
        <style>
        .main {
            max-width: 900px;
            margin: 0 auto;
        }

        .section-card {
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            background-color: #ffffff;
            margin-bottom: 1.5rem;
        }

        .muted {
            color: #6b7280;
            font-size: 0.95rem;
        }

        .small-label {
            font-size: 0.85rem;
            font-weight: 600;
            color: #4b5563;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }
        </style>
        """,
        unsafe_allow_html=True
    )