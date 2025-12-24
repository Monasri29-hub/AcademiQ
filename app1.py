import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import math

# ============================================================================
# PAGE CONFIG & ADVANCED STYLING
# ============================================================================
st.set_page_config(
    page_title="Academic Overload Detection System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# PROFESSIONAL DARK THEME WITH ANIMATIONS & GLASSMORPHISM
st.markdown("""
<style>
    /* Root Colors */
    :root {
        --primary: #58a6ff;
        --primary-dark: #1f6feb;
        --success: #3fb950;
        --warning: #d29922;
        --danger: #f85149;
        --bg-primary: #0d1117;
        --bg-secondary: #161b22;
        --bg-tertiary: #21262d;
        --text-primary: #e6edf3;
        --text-secondary: #8b949e;
        --border: #30363d;
    }
    
    /* Main Container */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
    }
    
    [data-testid="stSidebar"] {
        background: rgba(22, 27, 34, 0.8);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(88, 166, 255, 0.1);
    }
    
    /* Typography */
    h1 {
        color: #58a6ff;
        font-size: 2.8rem !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #58a6ff, #79c0ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1.5rem !important;
        letter-spacing: -1px;
    }
    
    h2 {
        color: #79c0ff;
        font-size: 2rem !important;
        margin-top: 2.5rem !important;
        margin-bottom: 1.5rem !important;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    h3 {
        color: #79c0ff;
        font-size: 1.4rem !important;
        margin-top: 1.5rem !important;
    }
    
    p, span, label {
        color: #e6edf3 !important;
        line-height: 1.6;
    }
    
    /* Input Fields with Glassmorphism */
    input, textarea, select {
        background: rgba(13, 17, 23, 0.5) !important;
        color: #e6edf3 !important;
        border: 1.5px solid rgba(88, 166, 255, 0.2) !important;
        border-radius: 8px !important;
        padding: 0.75rem !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
        font-size: 1rem !important;
    }
    
    input:focus, textarea:focus, select:focus {
        border-color: #58a6ff !important;
        box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.15) !important;
        background: rgba(13, 17, 23, 0.8) !important;
    }
    
    /* Buttons - Enhanced */
    button {
        background: linear-gradient(135deg, #238636, #2ea043) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.8rem 1.8rem !important;
        font-size: 1rem !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(48, 54, 61, 0.3) !important;
        position: relative;
        overflow: hidden;
    }
    
    button:hover {
        background: linear-gradient(135deg, #2ea043, #3fb950) !important;
        box-shadow: 0 8px 20px rgba(63, 185, 80, 0.3) !important;
        transform: translateY(-2px) !important;
    }
    
    button:active {
        transform: translateY(0) !important;
    }
    
    /* Metrics */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(22, 27, 34, 0.6), rgba(33, 38, 45, 0.6)) !important;
        border: 1px solid rgba(88, 166, 255, 0.15) !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="metric-container"]:hover {
        border-color: rgba(88, 166, 255, 0.3) !important;
        box-shadow: 0 12px 32px rgba(88, 166, 255, 0.2) !important;
        transform: translateY(-4px) !important;
    }
    
    /* Status Cards */
    .status-card {
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
    }
    
    .status-card-safe {
        background: linear-gradient(135deg, rgba(13, 57, 34, 0.4), rgba(13, 57, 34, 0.2)) !important;
        border-color: rgba(63, 185, 80, 0.3) !important;
    }
    
    .status-card-warning {
        background: linear-gradient(135deg, rgba(61, 40, 23, 0.4), rgba(61, 40, 23, 0.2)) !important;
        border-color: rgba(210, 153, 34, 0.3) !important;
    }
    
    .status-card-critical {
        background: linear-gradient(135deg, rgba(61, 31, 26, 0.4), rgba(61, 31, 26, 0.2)) !important;
        border-color: rgba(248, 81, 73, 0.3) !important;
    }
    
    .status-card-safe:hover, .status-card-warning:hover, .status-card-critical:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.5) !important;
    }
    
    /* Explanation Boxes */
    .explanation-box {
        background: linear-gradient(135deg, rgba(13, 31, 60, 0.5), rgba(31, 110, 251, 0.1)) !important;
        border: 1px solid rgba(31, 110, 251, 0.2) !important;
        padding: 1.5rem !important;
        border-radius: 12px !important;
        line-height: 1.8 !important;
        margin: 1.5rem 0 !important;
        color: #79c0ff !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Forms */
    [data-testid="stForm"] {
        background: linear-gradient(135deg, rgba(22, 27, 34, 0.5), rgba(33, 38, 45, 0.3)) !important;
        border: 1px solid rgba(88, 166, 255, 0.1) !important;
        padding: 2rem !important;
        border-radius: 16px !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4) !important;
    }
    
    /* Dividers */
    hr {
        border-color: rgba(88, 166, 255, 0.1) !important;
        margin: 2rem 0 !important;
    }
    
    /* Tables */
    [data-testid="dataframe"] {
        background: linear-gradient(135deg, rgba(22, 27, 34, 0.6), rgba(33, 38, 45, 0.4)) !important;
    }
    
    .dataframe {
        color: #e6edf3 !important;
    }
    
    /* Alerts */
    [data-testid="stAlert"] {
        background: linear-gradient(135deg, rgba(22, 27, 34, 0.6), rgba(33, 38, 45, 0.4)) !important;
        border-radius: 12px !important;
        border-left: 4px solid !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Progress Bars */
    .progress-container {
        width: 100%;
        height: 8px;
        background: rgba(48, 54, 61, 0.5);
        border-radius: 4px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .progress-bar {
        height: 100%;
        border-radius: 4px;
        transition: width 0.5s ease;
        background: linear-gradient(90deg, #58a6ff, #79c0ff);
        box-shadow: 0 0 10px rgba(88, 166, 255, 0.5);
    }
    
    /* Radio buttons */
    [role="radio"], [role="checkbox"] {
        accent-color: #58a6ff !important;
    }
    
    /* Links */
    a {
        color: #58a6ff !important;
        transition: color 0.3s ease !important;
    }
    
    a:hover {
        color: #79c0ff !important;
        text-decoration: underline !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #c9d1d9 !important;
    }
    
    /* Animations */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.8;
        }
    }
    
    [data-testid="metric-container"] {
        animation: slideIn 0.5s ease-out;
    }
    
    /* Gradient Text */
    .gradient-text {
        background: linear-gradient(135deg, #58a6ff, #79c0ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, rgba(31, 110, 251, 0.1), rgba(88, 166, 255, 0.05)) !important;
        border: 1px solid rgba(88, 166, 255, 0.2) !important;
        border-radius: 16px !important;
        padding: 3rem !important;
        margin-bottom: 2rem !important;
        text-align: center !important;
        backdrop-filter: blur(10px) !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR: NAVIGATION
# ============================================================================
st.sidebar.markdown("## 📋 Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["🏠 Home", "📊 Student Assessment", "👨‍🏫 Mentor Dashboard", "📚 System Guide"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    ### ℹ️ Quick Help
    
    **📊 Student Assessment:**  
    Input your workload to calculate ALI.
    
    **👨‍🏫 Mentor Dashboard:**  
    Monitor all students and identify risks.
    
    **📚 System Guide:**  
    Learn how the system works.
    """
)

# ============================================================================
# SESSION STATE
# ============================================================================
if "student_records" not in st.session_state:
    st.session_state.student_records = []

# ============================================================================
# PAGE 0: HOME
# ============================================================================
if page == "🏠 Home":
    st.markdown("# 📚 Academic Overload Detection System")
    
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h2 style="color: #58a6ff; margin: 0;">Detect Academic Overload Before It Causes Failure</h2>
        <p style="font-size: 1.1rem; color: #8b949e; margin-top: 1rem;">
        A transparent, rule-based system for early identification of students at risk. 
        No black-box AI. No privacy concerns. Just clear data and actionable insights.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Three Feature Cards
    st.markdown("## 🌟 Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="status-card status-card-safe">
            <h3 style="color: #3fb950; margin: 0;">✅ Transparent</h3>
            <p>Rule-based algorithm. Every decision is explainable. No hidden logic.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="status-card status-card-warning">
            <h3 style="color: #d29922; margin: 0;">⏰ Early Warning</h3>
            <p>Identify students at risk BEFORE performance drops or burnout occurs.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="status-card status-card-critical">
            <h3 style="color: #f85149; margin: 0;">🚀 Ready Now</h3>
            <p>No database needed. No complex infrastructure. Deploy today.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Stats Section
    st.markdown("## 📈 System Status")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Students Assessed", len(st.session_state.student_records), help="Total assessments")
    
    with col2:
        safe = sum(1 for r in st.session_state.student_records if r["ALI"] < 1.0)
        st.metric("Safe Students", safe, help="ALI < 1.0")
    
    with col3:
        warning = sum(1 for r in st.session_state.student_records if 1.0 <= r["ALI"] <= 1.3)
        st.metric("At Risk", warning, help="1.0 ≤ ALI ≤ 1.3")
    
    with col4:
        critical = sum(1 for r in st.session_state.student_records if r["ALI"] > 1.3)
        st.metric("Critical", critical, help="ALI > 1.3")
    
    st.markdown("---")
    
    # CTA
    st.markdown("## 🚀 Get Started")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### For Students
        
        Go to **Student Assessment** to:
        - Enter your current workload
        - Calculate your Academic Load Index
        - Get personalized recommendations
        - Track your workload over time
        """)
    
    with col2:
        st.markdown("""
        ### For Mentors
        
        Go to **Mentor Dashboard** to:
        - Monitor all students' workloads
        - Filter by risk level
        - Identify intervention priorities
        - Export records for reporting
        """)

# ============================================================================
# PAGE 1: STUDENT ASSESSMENT
# ============================================================================
elif page == "📊 Student Assessment":
    st.markdown("# 📊 Student Workload Assessment")
    
    st.markdown(
        """
        <div class="explanation-box">
        <strong>🎯 How it works:</strong><br>
        Enter your subjects, assignments, and study hours available. 
        We calculate your <strong>Academic Load Index (ALI)</strong> — a simple metric 
        showing if your workload fits your available time.
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.form("student_assessment_form", border=True):
        
        st.markdown("### 👤 Your Information")
        col1, col2 = st.columns(2)

        with col1:
            student_name = st.text_input(
                "Full Name",
                value="",
                placeholder="Enter your name",
            )
            
        with col2:
            daily_study_hours = st.number_input(
                "Daily Study Hours Available",
                min_value=1.0,
                max_value=16.0,
                value=6.0,
                step=0.5,
            )

        st.markdown("---")
        
        st.markdown("### 📚 Subjects")
        num_subjects = st.slider(
            "How many subjects?",
            min_value=1,
            max_value=10,
            value=3,
            label_visibility="collapsed"
        )

        st.markdown("---")
        st.markdown("### 📖 Assignment Details")
        
        subject_data = []
        
        cols = st.columns(4)
        cols[0].markdown("**Subject**")
        cols[1].markdown("**# Assignments**")
        cols[2].markdown("**Hours Each**")
        cols[3].markdown("**Days Left**")
        st.divider()

        for i in range(num_subjects):
            cols = st.columns(4)
            
            with cols[0]:
                subject_name = st.text_input(
                    f"Subject name",
                    value=f"Subject {i+1}",
                    key=f"subj_name_{i}",
                    label_visibility="collapsed"
                )
            
            with cols[1]:
                num_assignments = st.number_input(
                    f"Assignments",
                    min_value=0,
                    max_value=20,
                    value=1,
                    key=f"num_assign_{i}",
                    label_visibility="collapsed"
                )
            
            with cols[2]:
                hours_per_assignment = st.number_input(
                    f"Hours per assignment",
                    min_value=0.5,
                    max_value=20.0,
                    value=3.0,
                    step=0.5,
                    key=f"hours_assign_{i}",
                    label_visibility="collapsed"
                )
            
            with cols[3]:
                deadline_days = st.number_input(
                    f"Days until deadline",
                    min_value=1,
                    max_value=60,
                    value=7,
                    key=f"deadline_{i}",
                    label_visibility="collapsed"
                )

            subject_data.append({
                "name": subject_name,
                "assignments": num_assignments,
                "hours_per_assignment": hours_per_assignment,
                "deadline_days": deadline_days
            })

        st.markdown("---")
        submit_button = st.form_submit_button(
            "🔍 Calculate My Academic Load Index",
            use_container_width=True,
            type="primary"
        )

    # ========================================================================
    # RESULTS
    # ========================================================================
    if submit_button:
        if not student_name or student_name.strip() == "":
            st.error("❌ Please enter your name to proceed.")
        else:
            total_required_hours = sum(
                subject["assignments"] * subject["hours_per_assignment"]
                for subject in subject_data
            )

            deadlines = [subject["deadline_days"] for subject in subject_data]
            min_deadline = min(deadlines) if deadlines else 1

            available_hours = daily_study_hours * min_deadline

            if available_hours > 0:
                ali = total_required_hours / available_hours
            else:
                ali = float('inf')

            # Determine status
            if ali < 1.0:
                status = "Safe"
                status_emoji = "✅"
                status_color = "safe"
            elif ali <= 1.3:
                status = "Warning"
                status_emoji = "⚠️"
                status_color = "warning"
            else:
                status = "Critical Overload"
                status_emoji = "🚨"
                status_color = "critical"

            record = {
                "Name": student_name,
                "ALI": round(ali, 2),
                "Status": f"{status_emoji} {status}",
                "Total Hours": round(total_required_hours, 1),
                "Available Hours": round(available_hours, 1),
                "Tightest Deadline": min_deadline,
                "Daily Capacity": daily_study_hours,
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            st.session_state.student_records.append(record)

            # Display Results
            st.markdown("---")
            st.markdown("## 📈 Your Results")

            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Academic Load Index", f"{ali:.2f}")
            
            with col2:
                st.metric("Total Required Hours", f"{total_required_hours:.1f}h")
            
            with col3:
                st.metric("Available Hours", f"{available_hours:.1f}h")

            # ALI Gauge Visual
            st.markdown("### ALI Gauge")
            
            # Create a visual gauge
            gauge_percentage = min(ali * 33.33, 100)  # Convert to percentage
            
            st.markdown(f"""
            <div style="margin: 1.5rem 0;">
                <div class="progress-container">
                    <div class="progress-bar" style="width: {gauge_percentage}%"></div>
                </div>
                <p style="text-align: center; color: #8b949e; font-size: 0.9rem;">
                    {ali:.2f} / 3.0 (Safe / Warning / Critical)
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Status Card
            st.markdown(f"""
            <div class="status-card status-card-{status_color}">
                <h2 style="margin: 0; color: {'#3fb950' if status_color == 'safe' else '#d29922' if status_color == 'warning' else '#f85149'};">
                    {status_emoji} {status}
                </h2>
                <p style="margin-top: 0.5rem;">
                    {'Your workload fits within your available time.' if status_color == 'safe' else 'Your workload is tight with little buffer.' if status_color == 'warning' else 'Your workload exceeds your realistic capacity.'}
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Explanation
            st.markdown("### 📋 How We Calculated This")
            
            explanation = f"""
            **Step 1: Total Required Hours**  
            {total_required_hours:.1f}h = all assignments across all subjects
            
            **Step 2: Available Hours**  
            {available_hours:.1f}h = {daily_study_hours}h/day × {min_deadline} day(s)
            
            **Step 3: Academic Load Index**  
            ALI = {total_required_hours:.1f} ÷ {available_hours:.1f} = **{ali:.2f}**
            
            **Interpretation:**
            - **< 1.0:** You have more time than needed ✅
            - **1.0–1.3:** Tight fit ⚠️
            - **> 1.3:** Not manageable 🚨
            """
            
            st.markdown(
                f"""
                <div class="explanation-box">
                {explanation}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Recommendation
            st.markdown("### 💡 Your Next Steps")
            
            # Move the helper function definition above its first usage
            def _get_recommendation(ali, total_hours, available_hours, deadline, daily_hours):
                if ali < 1.0:
                    buffer_hours = available_hours - total_hours
                    return (
                        f"✅ **You're in Good Shape!**  \n"
                        f"You have **{buffer_hours:.1f} hours of buffer**. Use this time to deepen learning and rest."
                    )
                elif ali <= 1.3:
                    shortage = total_hours - available_hours
                    return (
                        f"⚠️ **Stay Disciplined**  \n"
                        f"You need **{shortage:.1f} more hours than available**. Any disruption could cause problems. "
                        f"Reach out to your mentor and consider asking for deadline extensions."
                    )
                else:
                    shortage = total_hours - available_hours
                    return (
                        f"🚨 **Action Required**  \n"
                        f"Your workload exceeds capacity by **{shortage:.1f} hours**. **Contact your mentor immediately.** "
                        f"Request deadline extensions, workload reduction, or academic support."
                    )

            recommendation = _get_recommendation(ali, total_required_hours, available_hours, min_deadline, daily_study_hours)
            st.info(recommendation)

            # Breakdown Table
            st.markdown("### 📊 Subject Breakdown")
            breakdown_df = pd.DataFrame([
                {
                    "Subject": s["name"],
                    "Assignments": s["assignments"],
                    "Hours Each": s["hours_per_assignment"],
                    "Total": round(s["assignments"] * s["hours_per_assignment"], 1),
                    "Deadline": s["deadline_days"]
                }
                for s in subject_data
            ])
            st.dataframe(breakdown_df, use_container_width=True, hide_index=True)

            st.success("✅ Assessment saved! Check the Mentor Dashboard to see all results.")

# ============================================================================
# HELPER: RECOMMENDATION
# ============================================================================
# (Removed duplicate definition of _get_recommendation)

# ============================================================================
# PAGE 2: MENTOR DASHBOARD
# ============================================================================
elif page == "👨‍🏫 Mentor Dashboard":
    st.markdown("# 👨‍🏫 Mentor Dashboard")
    
    st.markdown(
        """
        <div class="explanation-box">
        <strong>Monitor & Intervene:</strong><br>
        Track all student workloads in real-time. Identify risks early and take action.
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.session_state.student_records:
        dashboard_df = pd.DataFrame(st.session_state.student_records)

        # Summary
        st.markdown("## 📌 Overview")
        
        col1, col2, col3, col4 = st.columns(4)

        total_students = len(dashboard_df)
        safe_count = sum(1 for r in st.session_state.student_records if r["ALI"] < 1.0)
        warning_count = sum(1 for r in st.session_state.student_records if 1.0 <= r["ALI"] <= 1.3)
        critical_count = sum(1 for r in st.session_state.student_records if r["ALI"] > 1.3)

        with col1:
            st.metric("Total Students", total_students)
        with col2:
            st.metric("Safe ✅", safe_count)
        with col3:
            st.metric("Warning ⚠️", warning_count)
        with col4:
            st.metric("Critical 🚨", critical_count)

        st.markdown("---")

        # Student Cards View
        st.markdown("## 👥 Student Workload Cards")
        
        dashboard_df_sorted = dashboard_df.sort_values("ALI", ascending=False)
        
        for idx, row in dashboard_df_sorted.iterrows():
            ali_value = row["ALI"]
            
            if ali_value < 1.0:
                card_style = "safe"
                color = "#3fb950"
            elif ali_value <= 1.3:
                card_style = "warning"
                color = "#d29922"
            else:
                card_style = "critical"
                color = "#f85149"
            
            st.markdown(f"""
            <div class="status-card status-card-{card_style}">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                    <div>
                        <h3 style="margin: 0; color: {color};">{row['Name']}</h3>
                        <p style="margin: 0.5rem 0; color: #8b949e;">{row['Status']}</p>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 2.5rem; font-weight: bold; color: {color};">{ali_value:.2f}</div>
                        <p style="margin: 0; color: #8b949e; font-size: 0.9rem;">ALI Score</p>
                    </div>
                </div>
                <hr style="border-color: rgba(88, 166, 255, 0.1); margin: 1rem 0;">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    <div>
                        <p style="margin: 0; color: #8b949e; font-size: 0.9rem;">Required Hours</p>
                        <p style="margin: 0.5rem 0; font-size: 1.2rem; color: #e6edf3;">{row['Total Hours']:.1f}h</p>
                    </div>
                    <div>
                        <p style="margin: 0; color: #8b949e; font-size: 0.9rem;">Available Hours</p>
                        <p style="margin: 0.5rem 0; font-size: 1.2rem; color: #e6edf3;">{row['Available Hours']:.1f}h</p>
                    </div>
                    <div>
                        <p style="margin: 0; color: #8b949e; font-size: 0.9rem;">Tightest Deadline</p>
                        <p style="margin: 0.5rem 0; font-size: 1.2rem; color: #e6edf3;">{row['Tightest Deadline']} day(s)</p>
                    </div>
                    <div>
                        <p style="margin: 0; color: #8b949e; font-size: 0.9rem;">Last Updated</p>
                        <p style="margin: 0.5rem 0; font-size: 0.95rem; color: #8b949e;">{row['Timestamp']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # Filters
        st.markdown("## 🔍 Quick Filters")
        
        filter_col1, filter_col2, filter_col3 = st.columns(3)

        with filter_col1:
            if st.button("🚨 Critical Students", use_container_width=True, type="primary"):
                critical = dashboard_df[dashboard_df["ALI"] > 1.3]
                if len(critical) > 0:
                    st.markdown(f"### Critical Overload ({len(critical)})")
                    st.dataframe(critical[["Name", "ALI", "Total Hours", "Available Hours"]], use_container_width=True, hide_index=True)
                    st.error("⚠️ These students need immediate intervention!")
                else:
                    st.success("✅ No critical students!")

        with filter_col2:
            if st.button("⚠️ Warning Zone", use_container_width=True):
                at_risk = dashboard_df[dashboard_df["ALI"] >= 1.0]
                if len(at_risk) > 0:
                    st.markdown(f"### At Risk ({len(at_risk)})")
                    st.dataframe(at_risk[["Name", "ALI", "Total Hours", "Available Hours"]], use_container_width=True, hide_index=True)
                    st.warning("Monitor these students closely.")
                else:
                    st.success("✅ No at-risk students!")

        with filter_col3:
            if st.button("✅ Safe Students", use_container_width=True):
                safe = dashboard_df[dashboard_df["ALI"] < 1.0]
                if len(safe) > 0:
                    st.markdown(f"### Safe ({len(safe)})")
                    st.dataframe(safe[["Name", "ALI", "Total Hours", "Available Hours"]], use_container_width=True, hide_index=True)
                    st.success("Great workload balance!")
                else:
                    st.info("No safe students yet.")

        st.markdown("---")

        # Export
        st.markdown("## 📥 Export & Manage")
        
        col_export, col_clear = st.columns(2)

        with col_export:
            csv = dashboard_df.to_csv(index=False)
            st.download_button(
                label="📊 Download Records (CSV)",
                data=csv,
                file_name=f"ali_records_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )

        with col_clear:
            if st.button("🗑️ Clear All", use_container_width=True, type="secondary"):
                st.session_state.student_records = []
                st.rerun()

    else:
        st.info("📭 No assessments yet. Start with Student Assessment.")

# ============================================================================
# PAGE 3: SYSTEM GUIDE
# ============================================================================
elif page == "📚 System Guide":
    st.markdown("# 📚 System Guide")

    st.markdown("## 🎯 What is ALI?")
    
    st.markdown(
        """
        <div class="explanation-box">
        The <strong>Academic Load Index (ALI)</strong> quantifies whether a student's 
        assigned workload exceeds their realistic time availability.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.latex(r"ALI = \frac{\text{Total Required Hours}}{\text{Available Hours}}")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="status-card status-card-safe">
            <h3 style="margin: 0; color: #3fb950;">✅ Safe</h3>
            <p style="margin: 0.5rem 0;">ALI < 1.0</p>
            <p style="margin: 0; font-size: 0.9rem; color: #8b949e;">Good buffer, manageable workload</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="status-card status-card-warning">
            <h3 style="margin: 0; color: #d29922;">⚠️ Warning</h3>
            <p style="margin: 0.5rem 0;">1.0 ≤ ALI ≤ 1.3</p>
            <p style="margin: 0; font-size: 0.9rem; color: #8b949e;">Tight fit, monitor closely</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="status-card status-card-critical">
            <h3 style="margin: 0; color: #f85149;">🚨 Critical</h3>
            <p style="margin: 0.5rem 0;">ALI > 1.3</p>
            <p style="margin: 0; font-size: 0.9rem; color: #8b949e;">Intervention needed now</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("## 💡 Why This System?")
    
    st.markdown(
        """
        Current LMS systems track **grades**, not **workload pressure**.
        
        Students experience silent academic overload → performance drops → too late to help.
        
        **ALI fixes this** by detecting overload *before* failure occurs.
        """
    )

    st.markdown("---")

    st.markdown("## 🎓 For Mentors")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Actions by Status
        
        **✅ Safe (ALI < 1.0)**
        - Celebrate balance
        - Encourage continued discipline
        - Use time for deeper learning
        
        **⚠️ Warning (1.0–1.3)**
        - Check in regularly
        - Offer workload review
        - Help prioritize assignments
        - Suggest deadline adjustments
        """)
    
    with col2:
        st.markdown("""
        ### Critical (ALI > 1.3)
        
        - **Contact immediately**
        - Discuss extensions
        - Reduce or remove assignments
        - Connect to support services
        - Follow up weekly
        
        **Remember:** This isn't about grades. It's about feasibility and wellness.
        """)

    st.markdown("---")

    st.markdown("## ✨ Key Principles")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ✅ **Transparent** — No black-box AI  
        ✅ **Rule-based** — Everyone understands it  
        ✅ **Conservative** — Errs on the side of caution  
        ✅ **Privacy-first** — No monitoring, no emotion detection
        """)
    
    with col2:
        st.markdown("""
        ✅ **Actionable** — Clear interventions  
        ✅ **Scalable** — Works institution-wide  
        ✅ **Low-friction** — No database needed  
        ✅ **Ready now** — Deploy today
        """)

# ============================================================================
# HELPER: RECOMMENDATION
# ============================================================================
def _get_recommendation(ali, total_hours, available_hours, deadline, daily_hours):
    if ali < 1.0:
        buffer_hours = available_hours - total_hours
        return (
            f"✅ **You're in Good Shape!**  \n"
            f"You have **{buffer_hours:.1f} hours of buffer**. Use this time to deepen learning and rest."
        )
    elif ali <= 1.3:
        shortage = total_hours - available_hours
        return (
            f"⚠️ **Stay Disciplined**  \n"
            f"You need **{shortage:.1f} more hours than available**. Any disruption could cause problems. "
            f"Reach out to your mentor and consider asking for deadline extensions."
        )
    else:
        shortage = total_hours - available_hours
        return (
            f"🚨 **Action Required**  \n"
            f"Your workload exceeds capacity by **{shortage:.1f} hours**. **Contact your mentor immediately.** "
            f"Request deadline extensions, workload reduction, or academic support."
        )
