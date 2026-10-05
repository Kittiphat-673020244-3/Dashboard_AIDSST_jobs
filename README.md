# AI, Data Science & Statistics Talent Supply & Demand Dashboard

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.18%2B-3F4F75.svg)](https://plotly.com/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-38B2AC.svg)](https://tailwindcss.com/)
[![Open Data](https://img.shields.io/badge/Open%20Data-Kaggle%20%7C%20BLS%20%7C%20GovData-brightgreen.svg)](#open-data-sources-repository)

An interactive analytical platform designed to evaluate and bridge the equilibrium between **Higher Education Talent Supply** and **Labor Market Demand** in Artificial Intelligence (AI), Data Science (DS), and Statistics.

---

## 📌 Executive Summary & Vision

Higher education institutions and industry employers often operate in silos, creating severe structural friction: graduates face challenges landing high-impact roles, while tech companies face shortages in specialized skills such as MLOps, LLM fine-tuning, and scalable cloud architectures.

This project delivers a dual-interface intelligence platform:
1. **Interactive Analytical Python Dashboard (Streamlit & Plotly):** A full-featured executive analysis tool supporting deep cross-filtering across academic production capacity, labor vacancies, salary benchmarks, and quantitative skill mismatch diagnostics.
2. **Global Career & Open Data Hub (Responsive Web App):** A client-side portal featuring career salary estimators, personal skill readiness checklists (0–100% gauge), and a searchable repository of curated open data sets.

---

## 🏗️ System Architecture & Feature Breakdown

```
[ AI / DS / Statistics Talent Intelligence Platform ]
 │
 ├── 🎓 Tab 1: Graduate Supply & Curriculum Skills
 │    ├── Global Filters: Field, Degree Level, Year Range (2020-2025)
 │    ├── Graph 1.1: Production Capacity by Program & Year (Bar/Line Combo)
 │    ├── Graph 1.2: Core Required Skills in Curriculum (Sunburst / Stacked Bar)
 │    ├── Graph 1.3: Post-Graduation Employment Rate (Yr 1, Yr 2, Yr 3)
 │    └── Graph 1.4: Tuition Fee vs. Employment Success (Interactive Scatter Plot)
 │
 ├── 💼 Tab 2: Labor Market Demand & Industry Requirements
 │    ├── Global Filters: Industry Sector, Experience Level, Region / Location
 │    ├── Graph 2.1: Open Job Vacancies Trend (Timeline Area Chart)
 │    ├── Graph 2.2: Top In-Demand Technical & Soft Skills (Sorted Frequency Bar)
 │    ├── Graph 2.3: Top Hiring Companies & Market Share Distribution
 │    └── Graph 2.4: Salary Distribution by Career Level (Box & Violin Plots)
 │
 ├── ⚖️ Tab 3: Skill Mismatch Analysis (Supply vs. Demand)
 │    ├── Graph 3.1: Skill Gap Heatmap (Curriculum Taught vs. Industry Required)
 │    ├── Graph 3.2: Skill Surplus vs. Shortage (Diverging Bar Chart)
 │    ├── Graph 3.3: Talent Volume vs. Job Vacancies Gap (Butterfly / Grouped Bar)
 │    └── Interactive Mismatch Diagnostic & Policy Recommendation Table
 │
 └── 🌐 Career & Open Data Hub Modules (Interactive Companion)
      ├── Executive KPI Highlights (Average Entry Salary, Job Growth Rate, Open Data Count)
      ├── Module A: Salary & Career Estimator Calculator
      ├── Module B: Interactive Skill Matrix Checklist & Readiness Gauge (0-100%)
      └── Module C: Searchable Open Data Directory & Direct Download Catalog
```

---

## 🔬 Core Dashboards & Visualizations

### Tab 1: Graduate Supply & Curriculum Skills
* **Production Capacity by Program & Year:** Tracks annual graduate counts across universities and degree levels (Bachelor's, Master's, Doctorate).
* **Core Curriculum Skill Coverage:** Evaluates what percentage of academic curricula mandate foundational and modern technologies (e.g., Core Math, Machine Learning, Python/R, SQL, MLOps).
* **Longitudinal Employment Tracking:** Evaluates career placement rates 1, 2, and 3 years post-graduation.
* **Tuition ROI Scatter Matrix:** Correlates total program tuition costs against first-year employment placement rates and cohort sizes.

### Tab 2: Labor Market Demand & Industry Requirements
* **Open Job Vacancies Trend:** Analyzes real-time job posting momentum across roles (AI Engineer, Data Scientist, Data Engineer, Statistician).
* **In-Demand Skills Frequency:** Quantifies market pull for specialized frameworks (PyTorch, TensorFlow, Docker, Kubernetes, AWS/GCP, LangChain, Distributed Spark).
* **Hiring Leaders & Sector Concentration:** Maps active recruitment by sector (Tech, Finance & Banking, Healthcare, Consulting, Manufacturing).
* **Compensation Benchmarking:** Granular salary intervals broken down by career tier (Entry-Level, Mid-Level, Senior, Lead/Executive).

### Tab 3: Quantitative Skill Mismatch Analysis
* **Supply vs. Demand Heatmap:** Exposes blind spots where industry demand is surging but university core curricula remain sparse (e.g., MLOps, Generative AI).
* **Surplus vs. Shortage Divergence:** Clear visual indicators of under-supplied vs. over-saturated skill sets.
* **Volume Equilibrium Gap:** Directly contrasts cohort graduation volumes against entry-level industry capacity.
* **Policy Diagnostic Engine:** Actionable institutional recommendations to optimize syllabus design and reduce skill mismatch by up to 35%.

---

## 📊 Open Data Sources Repository

The dashboard integrates synthesized empirical benchmarks based on major international and Thai open data sources:

| Source | Dataset / Focus | Scope & Content | License | Primary Reference |
| :--- | :--- | :--- | :--- | :--- |
| **Kaggle** | Data Science & AI Salaries (2020–2025) | Global compensation data by role, experience, country, and remote work ratio | CC0: Public Domain | [Kaggle Dataset](https://www.kaggle.com/datasets/adilshamim8/salaries-for-data-science-jobs/data) |
| **U.S. BLS** | Occupational Employment & Wages (OEWS) | Employment statistics, median wages, and 10-year job growth projections | Public Domain | [U.S. BLS Data](https://www.bls.gov/oews/tables.htm) |
| **Our World in Data** | AI Research & Workforce Index | Global AI talent migration, publication volume, and private investment trends | CC-BY 4.0 | [OWID AI Repository](https://github.com/owid/notebooks/tree/main/DataTeam/projects/ai) |
| **NCES IPEDS** | Postsecondary Completion Data | Degree completions in Computer Science, Data Science, and Mathematical Statistics | Public Domain | [NCES IPEDS](https://nces.ed.gov/ipeds/use-the-data) |
| **Hugging Face** | Data Science & AI Job Postings | Parsed job descriptions, required skill taxonomy, and tech stack frequencies | Apache 2.0 | [Hugging Face Datasets](https://huggingface.co/datasets) |
| **UNESCO** | Science, Technology & Education Stats | Global STEM tertiary education enrollment and female researcher participation | CC-BY-SA | [UNESCO Data Centre](http://data.uis.unesco.org/) |
| **GovData (Thailand)** | กระทรวง อว. / สถิติแรงงาน (NSO) | Thai higher education graduation statistics in STEM, digital sciences, and local employment | Open Gov License | [data.go.th](https://data.go.th) |

---

## 🗂️ Project Directory Structure

```plaintext
Dashboard_AIDSST_jobs/
├── app.py                             # Main Streamlit + Plotly Interactive Dashboard
├── index.html                         # Standalone Responsive Web App (Tailwind CSS + Chart.js)
├── business_requirements_document.md  # Core BRD specification
├── gemini-code-1791193319830.md      # Web UI & Open Data specification
├── README.md                          # Project documentation and user guide
├── PROJECT_STATUS.md                  # Step-by-step progress tracking
├── requirements.txt                   # Python package dependencies
├── data/
│   ├── graduates_data.csv             # Synthetic empirical university graduate & curriculum data
│   ├── jobs_data.csv                  # Open job postings, employer demands, and salary data
│   ├── open_data_catalog.json         # Metadata and download links for the 7 open datasets
│   └── data_loader.py                 # Data generator, DuckDB / Pandas processing engine
└── assets/
    └── custom.css                     # Premium styling for Streamlit & web layouts
```

---

## 🚀 Quickstart & Installation

### 1. Prerequisites
* **Python:** Version 3.10 or higher
* Modern web browser (Chrome, Edge, Firefox, Safari)

### 2. Environment Setup
Clone the repository and create an isolated virtual environment:

```bash
# Clone the repository
git clone https://github.com/Kittiphat-673020244-3/Dashboard_AIDSST_jobs.git
cd Dashboard_AIDSST_jobs

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 3. Launching the Interactive Python Dashboard
Run the Streamlit analytical application:

```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser.

### 4. Viewing the Standalone Web Dashboard
You can directly open `index.html` in any web browser without needing a backend server:
```bash
# Windows
start index.html

# macOS
open index.html
```

---

## ⚡ Cross-Filtering & User Interaction Guide

* **Coordinated State Synchronization:** In each tab, selecting or clicking any category (e.g. filtering by *Data Science* or clicking an institution) dynamically updates all sister charts simultaneously.
* **Instant Reset:** Every tab includes a dedicated `Clear All Filters` button to instantly restore default views.
* **Salary & Readiness Calculators:** Explore personalized career pathways by selecting your degree, experience level, and mastered skills to calculate real-time career readiness and salary potential.

---

## 📄 License & Attribution

This project is open-source under the [MIT License](LICENSE).  
Data citations belong to their respective publishers (BLS, Kaggle, OWID, NCES, Hugging Face, UNESCO, and Digital Government Development Agency Thailand).
