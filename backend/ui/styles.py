import streamlit as st


def apply_styles():
    st.markdown(
        """
        <style>
        :root {
            --app-bg: #ffffff;
            --surface: #ffffff;
            --surface-soft: #f7f8fb;

            --text-primary: #1f2937;
            --text-secondary: #5f6b7a;
            --border: #d9dee8;

            --accent: #4f46e5;
            --accent-soft: #eef2ff;

            --info-bg: #eaf4ff;
            --info-text: #0f4c81;

            --success-bg: #ecfdf3;
            --success-text: #166534;

            --warning-bg: #fff8e6;
            --warning-text: #854d0e;
        }

        @media (prefers-color-scheme: dark) {
            :root {
                --app-bg: #0e1117;
                --surface: #171b22;
                --surface-soft: #1d232d;

                --text-primary: #f3f4f6;
                --text-secondary: #b8c0cc;
                --border: #343b46;

                --accent: #8b83ff;
                --accent-soft: #24233a;

                --info-bg: #15263a;
                --info-text: #79b8ff;

                --success-bg: #143222;
                --success-text: #86efac;

                --warning-bg: #382f12;
                --warning-text: #fde68a;
            }
        }

        /* Main application text */
        .stApp {
            color: var(--text-primary);
        }

        /* General headings and paragraphs */
        h1,
        h2,
        h3,
        h4,
        h5,
        h6,
        p,
        li {
            color: var(--text-primary);
        }

        /* Custom cards */
        .section-card,
        .report-card {
            background: var(--surface);
            color: var(--text-primary);

            border: 1px solid var(--border);
            border-radius: 16px;

            padding: 24px;
            margin: 16px 0;

            box-sizing: border-box;
        }

        .section-card h1,
        .section-card h2,
        .section-card h3,
        .section-card h4,
        .section-card p,
        .report-card h1,
        .report-card h2,
        .report-card h3,
        .report-card h4,
        .report-card p {
            color: var(--text-primary) !important;
        }

        /* Secondary / metadata text */
        .muted {
            color: var(--text-secondary) !important;
        }

        .small-label {
            color: var(--accent) !important;

            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            text-transform: uppercase;

            margin-bottom: 8px;
        }

        /* Takeaway card */
        .takeaway {
            background: var(--accent-soft);
            color: var(--text-primary);

            border-left: 4px solid var(--accent);
            border-radius: 10px;

            padding: 18px;
            margin-top: 18px;
        }

        .takeaway strong,
        .takeaway p {
            color: var(--text-primary) !important;
        }

        /* Improve custom informational areas */
        div[data-testid="stAlert"] {
            border-radius: 10px;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            border-right: 1px solid var(--border);
        }

        /* Inputs */
        textarea,
        input {
            color: var(--text-primary) !important;
        }

        /* Improve card spacing on smaller screens */
        @media (max-width: 768px) {
            .section-card,
            .report-card {
                padding: 18px;
                border-radius: 12px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )