import streamlit as st


def apply_styles():
    st.markdown(
        """
        <style>
        .block-container {
            max-width: 950px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        .hero-card {
            padding: 2rem;
            border-radius: 18px;
            border: 1px solid #e5e7eb;
            background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
            margin-bottom: 1.5rem;
        }

        .section-card {
            padding: 1.5rem;
            border-radius: 14px;
            border: 1px solid #e5e7eb;
            background-color: #ffffff;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }

        .coach-card {
            padding: 1.25rem;
            border-radius: 14px;
            border-left: 5px solid #4f46e5;
            background-color: #f8fafc;
            margin-bottom: 1rem;
        }

        .report-card {
            padding: 1.25rem;
            border-radius: 14px;
            border: 1px solid #e5e7eb;
            background-color: #ffffff;
            margin-bottom: 1rem;
        }

        .muted {
            color: #6b7280;
            font-size: 0.95rem;
        }

        .small-label {
            font-size: 0.78rem;
            font-weight: 700;
            color: #4f46e5;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        .takeaway {
            padding: 1rem;
            border-radius: 12px;
            background-color: #ecfdf5;
            border: 1px solid #a7f3d0;
            margin-top: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )