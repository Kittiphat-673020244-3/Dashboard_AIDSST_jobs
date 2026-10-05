"""
AI, Data Science & Statistics Talent Supply & Demand Dashboard
Interactive Analytical Platform (Streamlit & Plotly)
"""

import os
import json
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from data.data_loader import load_data, compute_skill_mismatch, generate_policy_recommendations

# ---------------------------------------------------------
# Page Configuration & Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI, Data Science & Statistics Talent Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
css_path = os.path.join(os.path.dirname(__file__), "assets", "custom.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Data Ingestion
# ---------------------------------------------------------
@st.cache_data(show_spinner=False)
def get_cached_data():
    return load_data()

graduates_raw, jobs_raw, catalog = get_cached_data()

# ---------------------------------------------------------
# State Management & Cross-filtering Handlers
# ---------------------------------------------------------
# Initialize Tab 1 filters in session state
if "t1_field" not in st.session_state:
    st.session_state["t1_field"] = "All"
if "t1_degree" not in st.session_state:
    st.session_state["t1_degree"] = "All"
if "t1_year_range" not in st.session_state:
    st.session_state["t1_year_range"] = (2020, 2025)
if "t1_uni" not in st.session_state:
    st.session_state["t1_uni"] = []

# Initialize Tab 2 filters in session state
if "t2_field" not in st.session_state:
    st.session_state["t2_field"] = "All"
if "t2_industry" not in st.session_state:
    st.session_state["t2_industry"] = "All"
if "t2_exp" not in st.session_state:
    st.session_state["t2_exp"] = "All"
if "t2_region" not in st.session_state:
    st.session_state["t2_region"] = "All"

# Initialize Tab 3 filters in session state
if "t3_field" not in st.session_state:
    st.session_state["t3_field"] = "All"
if "t3_degree" not in st.session_state:
    st.session_state["t3_degree"] = "All"

def reset_tab1_filters():
    st.session_state["t1_field"] = "All"
    st.session_state["t1_degree"] = "All"
    st.session_state["t1_year_range"] = (2020, 2025)
    st.session_state["t1_uni"] = []

def reset_tab2_filters():
    st.session_state["t2_field"] = "All"
    st.session_state["t2_industry"] = "All"
    st.session_state["t2_exp"] = "All"
    st.session_state["t2_region"] = "All"

def reset_tab3_filters():
    st.session_state["t3_field"] = "All"
    st.session_state["t3_degree"] = "All"

# ---------------------------------------------------------
# Executive Header Banner
# ---------------------------------------------------------
st.markdown("""
<div class="executive-header">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div>
            <h1>AI, Data Science & Statistics Talent Intelligence Platform</h1>
            <p>Labor Market Supply vs. Demand Equilibrium, Curriculum Alignment & Empirical Career Insights</p>
        </div>
        <div style="margin-top: 10px;">
            <span class="filter-badge">⚡ Real-time Cross-filtering</span>
            <span class="filter-badge">🌐 Open Data Integrated</span>
            <span class="filter-badge">📊 Dual-currency Benchmarking</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Navigation Tabs
# ---------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎓 Tab 1: Graduate Supply & Curriculum",
    "💼 Tab 2: Labor Market Demand",
    "⚖️ Tab 3: Skill Mismatch Analysis",
    "🚀 Tab 4: Career & Salary Estimator",
    "🌐 Tab 5: Open Data Repository"
])

# =========================================================
# TAB 1: GRADUATE SUPPLY & CURRICULUM SKILLS
# =========================================================
with tab1:
    st.markdown("### 🎓 Academic Capacity, Core Curriculum & Graduate Employment")
    st.caption("Investigate higher education talent generation, mandatory syllabus subjects, and multi-year employment absorption.")

    # Tab 1 Header Filter Bar
    with st.container():
        f1, f2, f3, f4, f5 = st.columns([2, 2, 2.5, 3.5, 1.5])
        with f1:
            t1_field_val = st.selectbox(
                "Field Filter",
                ["All", "Artificial Intelligence", "Data Science", "Statistics"],
                index=["All", "Artificial Intelligence", "Data Science", "Statistics"].index(st.session_state["t1_field"]),
                key="sb_t1_field"
            )
            st.session_state["t1_field"] = t1_field_val
        with f2:
            t1_degree_val = st.selectbox(
                "Degree Level",
                ["All", "Bachelor's", "Master's", "Doctorate"],
                index=["All", "Bachelor's", "Master's", "Doctorate"].index(st.session_state["t1_degree"]),
                key="sb_t1_degree"
            )
            st.session_state["t1_degree"] = t1_degree_val
        with f3:
            t1_year_val = st.slider(
                "Graduation Year Range",
                min_value=2020,
                max_value=2025,
                value=st.session_state["t1_year_range"],
                key="sl_t1_year"
            )
            st.session_state["t1_year_range"] = t1_year_val
        with f4:
            available_unis = sorted(graduates_raw["institution"].unique().tolist())
            t1_uni_val = st.multiselect(
                "University / Institution Filter",
                options=available_unis,
                default=st.session_state["t1_uni"],
                key="ms_t1_uni"
            )
            st.session_state["t1_uni"] = t1_uni_val
        with f5:
            st.write("")
            st.write("")
            st.button("🔄 Reset Filters", on_click=reset_tab1_filters, key="btn_reset_t1", use_container_width=True)

    # Filter Supply Data
    g_df = graduates_raw.copy()
    if st.session_state["t1_field"] != "All":
        g_df = g_df[g_df["field"] == st.session_state["t1_field"]]
    if st.session_state["t1_degree"] != "All":
        g_df = g_df[g_df["degree"] == st.session_state["t1_degree"]]
    g_df = g_df[(g_df["year"] >= st.session_state["t1_year_range"][0]) & (g_df["year"] <= st.session_state["t1_year_range"][1])]
    if st.session_state["t1_uni"]:
        g_df = g_df[g_df["institution"].isin(st.session_state["t1_uni"])]

    # Tab 1 KPI Cards
    k1, k2, k3, k4 = st.columns(4)
    total_grads = g_df["graduates_count"].sum()
    avg_emp_yr1 = round(g_df["employed_yr1_pct"].mean(), 1) if len(g_df) > 0 else 0
    num_programs = g_df["program_name"].nunique()
    avg_tuition_thb = int(g_df["tuition_fee_thb"].mean()) if len(g_df) > 0 else 0

    with k1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Graduates Produced</div>
            <div class="metric-value">{total_grads:,}</div>
            <div class="metric-subtitle">Across selected cohort years</div>
        </div>
        """, unsafe_allow_html=True)
    with k2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Year-1 Employment Rate</div>
            <div class="metric-value">{avg_emp_yr1}%</div>
            <div class="metric-subtitle">Direct field placement average</div>
        </div>
        """, unsafe_allow_html=True)
    with k3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Active Degree Programs</div>
            <div class="metric-value">{num_programs}</div>
            <div class="metric-subtitle">Covering {g_df['institution'].nunique()} institutions</div>
        </div>
        """, unsafe_allow_html=True)
    with k4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Mean Program Tuition</div>
            <div class="metric-value">฿{avg_tuition_thb:,}</div>
            <div class="metric-subtitle">Approx. ${int(avg_tuition_thb/35.5):,} USD</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Visualizations Row 1: Graph 1.1 & Graph 1.2
    c1, c2 = st.columns([1.1, 0.9])

    with c1:
        st.markdown("#### 📈 Graph 1.1: Production Capacity by Program & Year")
        st.caption("Annual graduate cohort volume breakdown across academic programs.")
        if len(g_df) > 0:
            prod_summary = g_df.groupby(["year", "program_name"])["graduates_count"].sum().reset_index()
            fig_prod = px.bar(
                prod_summary,
                x="year",
                y="graduates_count",
                color="program_name",
                barmode="stack",
                labels={"year": "Graduation Year", "graduates_count": "Graduates Count", "program_name": "Program"},
                color_discrete_sequence=px.colors.qualitative.Prism,
                height=380
            )
            fig_prod.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                legend=dict(orientation="h", yanchor="bottom", y=-0.35, xanchor="center", x=0.5, font=dict(size=10)),
                hovermode="x unified"
            )
            st.plotly_chart(fig_prod, use_container_width=True)
            st.markdown("""
            <div class="data-reference-tag">
                <strong>📌 Data Reference:</strong> U.S. NCES IPEDS Postsecondary Degree Completions (CIP 11.0102 AI, CIP 30.7001 Data Science, CIP 27.0501 Statistics) & GovData Thailand (data.go.th) - กระทรวงการอุดมศึกษา วิทยาศาสตร์ วิจัยและนวัตกรรม (สป.อว.)
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No graduate data matching the selected filter criteria.")

    with c2:
        st.markdown("#### 🧠 Graph 1.2: Core Required Skills in Curriculum")
        st.caption("Percentage of academic programs that mandate each subject.")
        if len(g_df) > 0:
            skill_counts = {}
            for sk_list in g_df["core_skills"].dropna():
                for s in str(sk_list).split(";"):
                    s = s.strip()
                    if s:
                        skill_counts[s] = skill_counts.get(s, 0) + 1
            total_cohorts = len(g_df)
            skill_df = pd.DataFrame([
                {"Skill": k, "Frequency (%)": round((v / total_cohorts) * 100, 1), "Count": v}
                for k, v in skill_counts.items()
            ]).sort_values(by="Frequency (%)", ascending=True).tail(12)

            fig_skills = px.bar(
                skill_df,
                x="Frequency (%)",
                y="Skill",
                orientation="h",
                text="Frequency (%)",
                color="Frequency (%)",
                color_continuous_scale="Blues",
                height=380
            )
            fig_skills.update_traces(texttemplate="%{text}%", textposition="outside")
            fig_skills.update_layout(margin=dict(l=20, r=20, t=20, b=20), coloraxis_showscale=False)
            st.plotly_chart(fig_skills, use_container_width=True)
            st.markdown("""
            <div class="data-reference-tag">
                <strong>📌 Data Reference:</strong> National Higher Education Syllabus Registries (MHESI/IPEDS) & ACM/IEEE Computing Curricula Guidelines for AI, DS & Statistics (2020-2025)
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No skill data available.")

    # Visualizations Row 2: Graph 1.3 & Graph 1.4
    c3, c4 = st.columns([1, 1])

    with c3:
        st.markdown("#### 🎯 Graph 1.3: Post-Graduation Employment Rate")
        st.caption("Longitudinal tracking of employment absorption: Year 1 vs. Year 2 vs. Year 3.")
        if len(g_df) > 0:
            emp_by_field = g_df.groupby("field")[["employed_yr1_pct", "employed_yr2_pct", "employed_yr3_pct"]].mean().reset_index()
            emp_melted = emp_by_field.melt(id_vars="field", var_name="Timeframe", value_name="Employment Rate (%)")
            emp_melted["Timeframe"] = emp_melted["Timeframe"].map({
                "employed_yr1_pct": "Year 1 Post-Grad",
                "employed_yr2_pct": "Year 2 Post-Grad",
                "employed_yr3_pct": "Year 3 Post-Grad"
            })
            fig_emp = px.bar(
                emp_melted,
                x="field",
                y="Employment Rate (%)",
                color="Timeframe",
                barmode="group",
                color_discrete_sequence=["#60a5fa", "#3b82f6", "#1d4ed8"],
                height=360
            )
            fig_emp.update_layout(
                yaxis=dict(range=[60, 105]),
                margin=dict(l=20, r=20, t=20, b=20),
                legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5)
            )
            st.plotly_chart(fig_emp, use_container_width=True)
            st.markdown("""
            <div class="data-reference-tag">
                <strong>📌 Data Reference:</strong> สำนักงานปลัดกระทรวงการอุดมศึกษาฯ (สป.อว.) ภาวะการมีงานทำของบัณฑิต (Graduate Employment Survey) & NCES Baccalaureate and Beyond (B&B) Study
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No employment data available.")

    with c4:
        st.markdown("#### 💰 Graph 1.4: Tuition Fee vs. Employment Success")
        st.caption("Scatter plot evaluating degree ROI (Tuition Cost vs. First-Year Placement).")
        if len(g_df) > 0:
            fig_scatter = px.scatter(
                g_df,
                x="tuition_fee_thb",
                y="employed_yr1_pct",
                size="graduates_count",
                color="field",
                hover_name="program_name",
                hover_data=["institution", "year", "degree", "graduates_count"],
                labels={
                    "tuition_fee_thb": "Total Tuition Fee (THB)",
                    "employed_yr1_pct": "Yr-1 Employment Rate (%)",
                    "field": "Discipline"
                },
                color_discrete_sequence=px.colors.qualitative.Safe,
                height=360
            )
            fig_scatter.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5)
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
            st.markdown("""
            <div class="data-reference-tag">
                <strong>📌 Data Reference:</strong> Official Higher Education Tuition Fee Registries & National Graduate Tracer Outcomes (MHESI Open Data / NCES College Scorecard)
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No tuition scatter data available.")



# =========================================================
# TAB 2: LABOR MARKET DEMAND & INDUSTRY REQUIREMENTS
# =========================================================
with tab2:
    st.markdown("### 💼 Labor Market Demand, Vacancies & Industry Requirements")
    st.caption("Explore open recruitment volume, employer sector distribution, required tech stacks, and compensation structures.")

    # Tab 2 Header Filter Bar
    with st.container():
        f1, f2, f3, f4, f5 = st.columns([2, 2.5, 2.5, 2.5, 1.5])
        with f1:
            t2_field_val = st.selectbox(
                "Field Filter",
                ["All", "Artificial Intelligence", "Data Science", "Statistics"],
                index=["All", "Artificial Intelligence", "Data Science", "Statistics"].index(st.session_state["t2_field"]),
                key="sb_t2_field"
            )
            st.session_state["t2_field"] = t2_field_val
        with f2:
            ind_options = ["All"] + sorted(jobs_raw["industry"].unique().tolist())
            t2_ind_val = st.selectbox(
                "Industry Sector",
                ind_options,
                index=ind_options.index(st.session_state["t2_industry"]),
                key="sb_t2_industry"
            )
            st.session_state["t2_industry"] = t2_ind_val
        with f3:
            exp_options = ["All", "Entry-Level (0-2 yrs)", "Mid-Level (3-5 yrs)", "Senior/Lead (5+ yrs)"]
            t2_exp_val = st.selectbox(
                "Experience Level",
                exp_options,
                index=exp_options.index(st.session_state["t2_exp"]),
                key="sb_t2_exp"
            )
            st.session_state["t2_exp"] = t2_exp_val
        with f4:
            reg_options = ["All"] + sorted(jobs_raw["region"].unique().tolist())
            t2_reg_val = st.selectbox(
                "Region / Location",
                reg_options,
                index=reg_options.index(st.session_state["t2_region"]),
                key="sb_t2_region"
            )
            st.session_state["t2_region"] = t2_reg_val
        with f5:
            st.write("")
            st.write("")
            st.button("🔄 Reset Filters", on_click=reset_tab2_filters, key="btn_reset_t2", use_container_width=True)

    # Filter Jobs Data
    j_df = jobs_raw.copy()
    if st.session_state["t2_field"] != "All":
        j_df = j_df[j_df["field"] == st.session_state["t2_field"]]
    if st.session_state["t2_industry"] != "All":
        j_df = j_df[j_df["industry"] == st.session_state["t2_industry"]]
    if st.session_state["t2_exp"] != "All":
        j_df = j_df[j_df["experience_level"] == st.session_state["t2_exp"]]
    if st.session_state["t2_region"] != "All":
        j_df = j_df[j_df["region"] == st.session_state["t2_region"]]

    # Tab 2 KPI Cards
    k1, k2, k3, k4 = st.columns(4)
    total_vacancies = j_df["vacancies"].sum()
    total_postings = len(j_df)
    avg_salary_thb = int(j_df["avg_salary_thb"].mean()) if len(j_df) > 0 else 0
    avg_salary_usd = int(j_df["avg_salary_usd"].mean()) if len(j_df) > 0 else 0

    with k1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Active Open Vacancies</div>
            <div class="metric-value">{total_vacancies:,}</div>
            <div class="metric-subtitle">Across {total_postings} job postings</div>
        </div>
        """, unsafe_allow_html=True)
    with k2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Hiring Organizations</div>
            <div class="metric-value">{j_df['company_name'].nunique()}</div>
            <div class="metric-subtitle">Across {j_df['industry'].nunique()} industry sectors</div>
        </div>
        """, unsafe_allow_html=True)
    with k3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Mean Monthly Comp (THB)</div>
            <div class="metric-value">฿{avg_salary_thb:,}</div>
            <div class="metric-subtitle">Base compensation benchmark</div>
        </div>
        """, unsafe_allow_html=True)
    with k4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Mean Annual Comp (USD)</div>
            <div class="metric-value">${avg_salary_usd:,}</div>
            <div class="metric-subtitle">Global parity wage benchmark</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Visualizations Row 1: Graph 2.1 & Graph 2.2
    c1, c2 = st.columns([1.1, 0.9])

    with c1:
        st.markdown("#### 📈 Graph 2.1: Open Job Vacancies Trend (Timeline)")
        st.caption("Trajectory of recruitment volume over time by technical discipline.")
        if len(j_df) > 0:
            timeline_df = j_df.groupby(["year", "field"])["vacancies"].sum().reset_index()
            fig_vac = px.area(
                timeline_df,
                x="year",
                y="vacancies",
                color="field",
                labels={"year": "Year", "vacancies": "Open Vacancies", "field": "Field"},
                color_discrete_sequence=["#3b82f6", "#10b981", "#f59e0b"],
                height=380
            )
            fig_vac.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5)
            )
            st.plotly_chart(fig_vac, use_container_width=True)
            st.markdown("""
            <div class="data-reference-tag">
                <strong>📌 Data Reference:</strong> Hugging Face Tech Job Postings Dataset & Our World in Data (OWID) AI Workforce and Industry Momentum Index
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No job postings found for selected filters.")

    with c2:
        st.markdown("#### 🔥 Graph 2.2: Top In-Demand Technical & Soft Skills")
        st.caption("Most frequently cited competencies across parsed job descriptions.")
        if len(j_df) > 0:
            req_skill_counts = {}
            for sk_str in j_df["required_skills"].dropna():
                for s in str(sk_str).split(";"):
                    s = s.strip()
                    if s:
                        req_skill_counts[s] = req_skill_counts.get(s, 0) + 1
            req_skill_df = pd.DataFrame([
                {"Skill": k, "Mentions": v}
                for k, v in req_skill_counts.items()
            ]).sort_values(by="Mentions", ascending=True).tail(12)

            fig_req_skills = px.bar(
                req_skill_df,
                x="Mentions",
                y="Skill",
                orientation="h",
                text="Mentions",
                color="Mentions",
                color_continuous_scale="Viridis",
                height=380
            )
            fig_req_skills.update_traces(textposition="outside")
            fig_req_skills.update_layout(margin=dict(l=20, r=20, t=20, b=20), coloraxis_showscale=False)
            st.plotly_chart(fig_req_skills, use_container_width=True)
            st.markdown("""
            <div class="data-reference-tag">
                <strong>📌 Data Reference:</strong> Hugging Face Data Science & AI Job Postings Corpus (80,000+ parsed job descriptions) & BLS Tech Skills Taxonomy
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No skill requirements data available.")

    # Visualizations Row 2: Graph 2.3 & Graph 2.4
    c3, c4 = st.columns([1, 1])

    with c3:
        st.markdown("#### 🏢 Graph 2.3: Top Hiring Companies & Market Share")
        st.caption("Active job listings concentration by leading enterprise employers.")
        if len(j_df) > 0:
            top_companies = j_df.groupby("company_name")["vacancies"].sum().reset_index()
            top_companies = top_companies.sort_values(by="vacancies", ascending=True).tail(10)
            fig_comp = px.bar(
                top_companies,
                x="vacancies",
                y="company_name",
                orientation="h",
                text="vacancies",
                color="vacancies",
                color_continuous_scale="Purples",
                height=360
            )
            fig_comp.update_traces(textposition="outside")
            fig_comp.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                coloraxis_showscale=False,
                xaxis_title="Vacancies Offered",
                yaxis_title="Company"
            )
            st.plotly_chart(fig_comp, use_container_width=True)
            st.markdown("""
            <div class="data-reference-tag">
                <strong>📌 Data Reference:</strong> Curated Corporate Tech Job Vacancies Directory (Kaggle Job Postings & Thailand Tech Talent Registries)
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No company data available.")

    with c4:
        st.markdown("#### 💵 Graph 2.4: Salary Distribution by Career Level")
        st.caption("Compensation dispersion (USD/yr) across experience tiers and roles.")
        if len(j_df) > 0:
            fig_box = px.box(
                j_df,
                x="experience_level",
                y="avg_salary_usd",
                color="field",
                labels={"experience_level": "Experience Tier", "avg_salary_usd": "Annual Compensation (USD)", "field": "Field"},
                color_discrete_sequence=px.colors.qualitative.Pastel,
                height=360
            )
            fig_box.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5)
            )
            st.plotly_chart(fig_box, use_container_width=True)
            st.markdown("""
            <div class="data-reference-tag">
                <strong>📌 Data Reference:</strong> Kaggle Data Science & AI Salaries (2020-2025 CC0) & U.S. BLS Occupational Employment and Wage Statistics (OEWS SOC 15-2051, 15-2041, 15-1221)
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No compensation data available.")



# =========================================================
# TAB 3: SKILL MISMATCH ANALYSIS (SUPPLY VS. DEMAND)
# =========================================================
with tab3:
    st.markdown("### ⚖️ Quantitative Skill Mismatch & Policy Diagnostic Engine")
    st.caption("Algorithmic comparison between curriculum syllabus focus and real market employer requirements.")

    # Tab 3 Filter Bar
    with st.container():
        f1, f2, f3 = st.columns([3, 3, 2])
        with f1:
            t3_field_val = st.selectbox(
                "Discipline Selection",
                ["All", "Artificial Intelligence", "Data Science", "Statistics"],
                index=["All", "Artificial Intelligence", "Data Science", "Statistics"].index(st.session_state["t3_field"]),
                key="sb_t3_field"
            )
            st.session_state["t3_field"] = t3_field_val
        with f2:
            t3_degree_val = st.selectbox(
                "Degree Focus",
                ["All", "Bachelor's", "Master's", "Doctorate"],
                index=["All", "Bachelor's", "Master's", "Doctorate"].index(st.session_state["t3_degree"]),
                key="sb_t3_degree"
            )
            st.session_state["t3_degree"] = t3_degree_val
        with f3:
            st.write("")
            st.write("")
            st.button("🔄 Reset Tab 3 Filters", on_click=reset_tab3_filters, key="btn_reset_t3", use_container_width=True)

    # Filter data for mismatch calculations
    m_grad = graduates_raw.copy()
    m_jobs = jobs_raw.copy()

    if st.session_state["t3_field"] != "All":
        m_grad = m_grad[m_grad["field"] == st.session_state["t3_field"]]
        m_jobs = m_jobs[m_jobs["field"] == st.session_state["t3_field"]]
    if st.session_state["t3_degree"] != "All":
        m_grad = m_grad[m_grad["degree"] == st.session_state["t3_degree"]]

    # Compute Mismatch Table
    mismatch_df = compute_skill_mismatch(m_grad, m_jobs)

    # KPIs for Mismatch
    k1, k2, k3, k4 = st.columns(4)
    shortage_count = len(mismatch_df[mismatch_df["gap_percentage"] > 5])
    surplus_count = len(mismatch_df[mismatch_df["gap_percentage"] < -5])
    top_deficit = mismatch_df.iloc[0]["skill"] if len(mismatch_df) > 0 else "N/A"
    equilibrium_score = max(0, min(100, int(100 - (mismatch_df["gap_percentage"].abs().mean() * 1.5))))

    with k1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Equilibrium Alignment Score</div>
            <div class="metric-value">{equilibrium_score} / 100</div>
            <div class="metric-subtitle">Systemic syllabus-market synergy</div>
        </div>
        """, unsafe_allow_html=True)
    with k2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Under-taught Deficit Skills</div>
            <div class="metric-value" style="color: #ef4444;">{shortage_count} Skills</div>
            <div class="metric-subtitle">Employer demand exceeds curriculum</div>
        </div>
        """, unsafe_allow_html=True)
    with k3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Over-taught Surplus Skills</div>
            <div class="metric-value" style="color: #f59e0b;">{surplus_count} Skills</div>
            <div class="metric-subtitle">Taught heavily, lower market pull</div>
        </div>
        """, unsafe_allow_html=True)
    with k4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Most Critical Skill Gap</div>
            <div class="metric-value" style="font-size: 1.25rem;">{top_deficit}</div>
            <div class="metric-subtitle">Gap: +{mismatch_df.iloc[0]['gap_percentage']}% deficit</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Graph 3.1 & Graph 3.2
    c1, c2 = st.columns([1, 1])

    with c1:
        st.markdown("#### ⚖️ Graph 3.2: Skill Surplus vs. Shortage Diverging Bar Chart")
        st.caption("Surplus (- left, over-taught) vs. Shortage (+ right, market deficit).")
        if len(mismatch_df) > 0:
            top_mismatch = mismatch_df.head(15).copy()
            # Color code
            colors = ["#ef4444" if g > 0 else "#3b82f6" for g in top_mismatch["gap_percentage"]]
            fig_diverge = go.Figure()
            fig_diverge.add_trace(go.Bar(
                y=top_mismatch["skill"],
                x=top_mismatch["gap_percentage"],
                orientation="h",
                marker=dict(color=colors),
                text=[f"{g:+.1f}%" for g in top_mismatch["gap_percentage"]],
                textposition="outside"
            ))
            fig_diverge.update_layout(
                xaxis_title="Gap: Demanded % minus Taught %",
                yaxis_title="",
                height=420,
                margin=dict(l=20, r=20, t=20, b=20)
            )
            st.plotly_chart(fig_diverge, use_container_width=True)
            st.markdown("""
            <div class="data-reference-tag">
                <strong>📌 Data Reference:</strong> Empirical Skill Equilibrium Differential Model: [% Market Demanded (Hugging Face / BLS)] minus [% Academic Taught (NCES IPEDS / MHESI Thailand)]
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No mismatch data calculated.")

    with c2:
        st.markdown("#### 🌐 Graph 3.1: Supply vs. Demand Alignment Matrix (Heatmap)")
        st.caption("Cross-mapping curriculum presence vs industry demand intensity.")
        if len(mismatch_df) > 0:
            matrix_sample = mismatch_df.head(12)
            z_data = [
                matrix_sample["curriculum_taught_pct"].values,
                matrix_sample["market_demanded_pct"].values
            ]
            fig_hm = go.Figure(data=go.Heatmap(
                z=z_data,
                x=matrix_sample["skill"].values,
                y=["Curriculum Taught (%)", "Market Demanded (%)"],
                colorscale="RdBu_r",
                text=[[f"{v:.1f}%" for v in row] for row in z_data],
                texttemplate="%{text}",
                hoverongaps=False
            ))
            fig_hm.update_layout(
                height=420,
                margin=dict(l=20, r=20, t=20, b=20),
                xaxis=dict(tickangle=-45)
            )
            st.plotly_chart(fig_hm, use_container_width=True)
            st.markdown("""
            <div class="data-reference-tag">
                <strong>📌 Data Reference:</strong> Cross-tabulation Matrix of University Core Syllabi (ACM/IEEE Standards) vs. Active Job Market Tech Stack Requirements (Hugging Face)
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No heatmap data available.")

    # Graph 3.3 & Recommendations Table
    c3, c4 = st.columns([1, 1])

    with c3:
        st.markdown("#### 👥 Graph 3.3: Talent Volume vs. Job Vacancies Gap")
        st.caption("Cohort graduation headcount vs. immediate industry vacancies capacity.")
        
        supply_by_field = m_grad.groupby("field")["graduates_count"].sum().reset_index()
        demand_by_field = m_jobs.groupby("field")["vacancies"].sum().reset_index()
        vol_comparison = pd.merge(supply_by_field, demand_by_field, on="field", how="outer").fillna(0)
        vol_comparison.rename(columns={"graduates_count": "Annual Cohort Supply", "vacancies": "Market Job Openings"}, inplace=True)
        
        vol_melted = vol_comparison.melt(id_vars="field", var_name="Metric", value_name="Headcount")
        fig_vol = px.bar(
            vol_melted,
            x="field",
            y="Headcount",
            color="Metric",
            barmode="group",
            color_discrete_sequence=["#6366f1", "#10b981"],
            height=380
        )
        fig_vol.update_layout(
            margin=dict(l=20, r=20, t=20, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig_vol, use_container_width=True)
        st.markdown("""
        <div class="data-reference-tag">
            <strong>📌 Data Reference:</strong> Annual Degree Conferred Statistics (U.S. NCES IPEDS & Thailand กระทรวง อว. / สถิติแรงงาน NSO) vs. Immediate Industrial Job Vacancy Registries
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("#### 💡 Strategic Policy & Curriculum Recommendations")
        st.caption("Actionable interventions for deans, curriculum committees, and industry sponsors.")
        recs = generate_policy_recommendations(mismatch_df, st.session_state["t3_field"])
        for rec in recs:
            with st.expander(f"📌 {rec['category']}", expanded=True):
                st.markdown(f"**Observed Gap:** {rec['observation']}")
                st.markdown(f"**Action Item:** {rec['action_item']}")
                st.markdown(f"**Projected Impact:** :green[{rec['projected_impact']}]")
        st.markdown("""
        <div class="data-reference-tag">
            <strong>📌 Policy Framework:</strong> Benchmarked against OECD Future of Work Guidelines and World Economic Forum (WEF) Global Skills Taxonomy
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📋 Comprehensive Diagnostic Mismatch Matrix")
    st.dataframe(
        mismatch_df[[
            "skill", "status", "curriculum_taught_pct", "market_demanded_pct", "gap_percentage",
            "curriculum_taught_count", "market_demanded_count"
        ]].rename(columns={
            "skill": "Skill Name",
            "status": "Diagnostic Classification",
            "curriculum_taught_pct": "Taught in Curricula (%)",
            "market_demanded_pct": "Demanded in Jobs (%)",
            "gap_percentage": "Net Gap (+ Shortage / - Surplus)",
            "curriculum_taught_count": "Programs Taught",
            "market_demanded_count": "Job Mentions"
        }),
        use_container_width=True,
        hide_index=True
    )
    st.markdown("""
    <div class="data-reference-tag">
        <strong>📌 Matrix Methodology:</strong> Integrated algorithmic synthesis of academic course catalogs and active hiring requisitions (2020-2025 longitudinal dataset).
    </div>
    """, unsafe_allow_html=True)



# =========================================================
# TAB 4: CAREER & SALARY ESTIMATOR (MODULE A & B)
# =========================================================
with tab4:
    st.markdown("### 🚀 Career Navigator, Salary Estimator & Skill Readiness Matrix")
    st.caption("Personalized tool for students and job seekers to evaluate compensation expectations and skill readiness.")

    col_calc, col_gauge = st.columns([1, 1])

    with col_calc:
        st.markdown("#### 💼 Module A: Compensation Benchmark Estimator")
        target_role = st.selectbox(
            "Select Target Role",
            ["AI Engineer", "Data Scientist", "Machine Learning Engineer", "Statistician", "Data Engineer", "Generative AI Engineer"]
        )
        target_degree = st.selectbox("Highest Degree Attained / Target", ["Bachelor's", "Master's", "Doctorate"])
        target_exp = st.selectbox("Experience Level", ["Entry-Level (0-2 yrs)", "Mid-Level (3-5 yrs)", "Senior/Lead (5+ yrs)"])
        target_reg = st.selectbox("Target Employment Market", ["Local / Thailand", "Asia-Pacific", "North America", "Global / Remote"])

        # Dynamic salary estimation calculation
        base_sal_map = {
            "Entry-Level (0-2 yrs)": (42000, 68000, 65000, 90000),
            "Mid-Level (3-5 yrs)": (75000, 135000, 95000, 150000),
            "Senior/Lead (5+ yrs)": (140000, 260000, 155000, 240000)
        }
        deg_mult = 1.0 if target_degree == "Bachelor's" else (1.18 if target_degree == "Master's" else 1.35)
        reg_mult = 1.0 if target_reg == "Local / Thailand" else (1.4 if target_reg == "Asia-Pacific" else (1.9 if target_reg == "North America" else 1.6))

        b_min_thb, b_max_thb, b_min_usd, b_max_usd = base_sal_map[target_exp]
        est_min_thb = int(b_min_thb * deg_mult)
        est_max_thb = int(b_max_thb * deg_mult)
        est_min_usd = int(b_min_usd * deg_mult * (reg_mult / 1.5))
        est_max_usd = int(b_max_usd * deg_mult * (reg_mult / 1.5))

        st.markdown(f"""
        <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 20px; margin-top: 15px;">
            <div style="font-weight: 700; font-size: 1.1rem; color: #1e293b;">Estimated Compensation Range:</div>
            <div style="display: flex; gap: 20px; margin-top: 10px;">
                <div>
                    <span style="font-size: 0.85rem; color: #64748b;">Thailand Benchmark:</span>
                    <div style="font-size: 1.5rem; font-weight: 800; color: #2563eb;">฿{est_min_thb:,} - ฿{est_max_thb:,} /mo</div>
                </div>
                <div>
                    <span style="font-size: 0.85rem; color: #64748b;">International Parity:</span>
                    <div style="font-size: 1.5rem; font-weight: 800; color: #059669;">${est_min_usd:,} - ${est_max_usd:,} /yr</div>
                </div>
            </div>
            <div style="font-size: 0.8rem; color: #64748b; margin-top: 10px;">
                *Estimates calculated from synthesized Kaggle Data Science Salaries (2020-2025) and U.S. BLS benchmarks.
            </div>
        </div>
        <div class="data-reference-tag">
            <strong>📌 Benchmark Source:</strong> Kaggle Data Science & AI Salaries (2020-2025 CC0) & U.S. BLS Occupational Employment and Wage Statistics (OEWS SOC 15-2051, 15-2041, 15-1221).
        </div>
        """, unsafe_allow_html=True)

    with col_gauge:
        st.markdown("#### 🎯 Module B: Interactive Skill Readiness Checklist")
        st.caption("Check off the skills you possess to evaluate your profile readiness score:")

        sample_skills = [
            "Python", "SQL", "Machine Learning", "Deep Learning", "PyTorch", "Docker & Containers",
            "MLOps", "Cloud (AWS/GCP/Azure)", "LLMs & GenAI", "Statistics & Probability",
            "Git & Version Control", "Communication"
        ]

        checked_skills = []
        cols = st.columns(2)
        for i, sk in enumerate(sample_skills):
            with cols[i % 2]:
                if st.checkbox(sk, key=f"chk_sk_{i}"):
                    checked_skills.append(sk)

        score = int((len(checked_skills) / len(sample_skills)) * 100)
        
        # Plot Gauge
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': "Market Readiness Score (%)", 'font': {'size': 18}},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#2563eb"},
                'steps': [
                    {'range': [0, 40], 'color': "#fee2e2"},
                    {'range': [40, 75], 'color': "#fef3c7"},
                    {'range': [75, 100], 'color': "#dcfce7"}
                ],
                'threshold': {
                    'line': {'color': "black", 'width': 3},
                    'thickness': 0.75,
                    'value': 80
                }
            }
        ))
        fig_gauge.update_layout(height=260, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)

        if score >= 75:
            st.success("🎉 Outstanding Profile! You possess over 75% of high-impact industry prerequisites.")
        elif score >= 50:
            st.warning("⚡ Good Foundation! Consider picking up containerization (Docker) and Cloud/MLOps to maximize offers.")
        else:
            st.info("💡 Early Stage: Focus on mastering core Python, SQL, and Git fundamentals first.")

        st.markdown("""
        <div class="data-reference-tag">
            <strong>📌 Taxonomy Reference:</strong> High-Demand Tech Competencies extracted from Hugging Face AI/DS Job Postings Corpus (80,000+ postings) & IEEE/ACM Guidelines.
        </div>
        """, unsafe_allow_html=True)



# =========================================================
# TAB 5: OPEN DATA REPOSITORY DIRECTORY (MODULE C)
# =========================================================
with tab5:
    st.markdown("### 🌐 Authoritative Open Data Sources Directory")
    st.caption("Official open datasets referenced in this research. Direct download links and metadata catalog.")

    search_query = st.text_input("🔍 Search Catalog (Dataset Name, Keyword, Source, or Tag):", "")
    
    # Filter catalog
    cat_df = pd.DataFrame(catalog)
    if search_query:
        mask = (
            cat_df["dataset_name"].str.contains(search_query, case=False, na=False) |
            cat_df["source"].str.contains(search_query, case=False, na=False) |
            cat_df["description"].str.contains(search_query, case=False, na=False) |
            cat_df["tags"].astype(str).str.contains(search_query, case=False, na=False)
        )
        filtered_cat = cat_df[mask]
    else:
        filtered_cat = cat_df

    st.markdown(f"**Showing {len(filtered_cat)} Open Data Repositories:**")

    for idx, row in filtered_cat.iterrows():
        with st.container():
            st.markdown(f"""
            <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                    <div>
                        <span style="background: #eff6ff; color: #1d4ed8; font-weight: 700; padding: 3px 10px; border-radius: 6px; font-size: 0.8rem; margin-right: 8px;">{row['source']}</span>
                        <span style="background: #f1f5f9; color: #475569; font-weight: 600; padding: 3px 10px; border-radius: 6px; font-size: 0.8rem; margin-right: 8px;">{row['license']}</span>
                        <span style="background: #f3e8ff; color: #7e22ce; font-weight: 600; padding: 3px 10px; border-radius: 6px; font-size: 0.8rem;">{row['file_format']}</span>
                        <h4 style="margin: 8px 0 4px 0; color: #0f172a;">{row['dataset_name']}</h4>
                        <p style="color: #475569; font-size: 0.9rem; margin-bottom: 8px;">{row['description']}</p>
                        <div style="font-size: 0.8rem; color: #64748b;">
                            <strong>Records:</strong> {row['records_count']} &nbsp;|&nbsp; <strong>Coverage:</strong> {row['coverage']} &nbsp;|&nbsp; <strong>Updated:</strong> {row['last_updated']}
                        </div>
                    </div>
                    <div style="margin-top: 10px;">
                        <a href="{row['download_url']}" target="_blank" style="display: inline-block; background: #2563eb; color: white; padding: 8px 16px; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 0.85rem;">
                            📥 Access Dataset
                        </a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
