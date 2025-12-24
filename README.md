# 📚 AcademiQ - Academic Load Index System

**Smart. Simple. Actionable.**

A transparent, rule-based system to detect academic overload early and enable proactive student support.

---

## 🎯 What is the Academic Load Index (ALI)?

The Academic Load Index (ALI) is a transparent, rule-based metric that quantifies whether a student's assigned academic workload exceeds their realistic time availability.

Unlike predictive models that estimate stress or burnout (which require extensive data and raise privacy concerns), ALI simply compares:

- **How much time is needed** to complete all assignments
- **How much time is realistically available** before the tightest deadline

### Formula

```
ALI = Total Required Study Hours ÷ Available Study Hours
```

### Interpretation

| ALI Range | Status | Meaning |
|-----------|--------|---------|
| ALI < 1.0 | ✅ Safe | Student has more time than needed; good buffer |
| 1.0 ≤ ALI ≤ 1.3 | ⚠️ Warning | Workload is tight; minimal room for disruption |
| ALI > 1.3 | 🚨 Critical | Workload exceeds realistic capacity; intervention needed |

### Examples

**Example 1: Safe Zone**
- Assignments require: 20 hours
- Days available: 10 days
- Study hours per day: 3 hours
- Available time: 3 × 10 = 30 hours
- **ALI = 20 ÷ 30 = 0.67** ✅ Safe

**Example 2: Warning Zone**
- Assignments require: 25 hours
- Days available: 10 days
- Study hours per day: 2 hours
- Available time: 2 × 10 = 20 hours
- **ALI = 25 ÷ 20 = 1.25** ⚠️ Warning

**Example 3: Critical Zone**
- Assignments require: 30 hours
- Days available: 10 days
- Study hours per day: 2 hours
- Available time: 2 × 10 = 20 hours
- **ALI = 30 ÷ 20 = 1.5** 🚨 Critical

---

## 💡 Why Academic Overload Detection?

### The Problem

Existing Learning Management Systems (LMS) track grades and completion but fail to detect cumulative workload pressure before it causes burnout or failure.

Students experiencing silent academic overload often remain undetected until:
- Performance deteriorates
- Mental stress becomes severe
- They drop out

### The Solution

This system provides explainable, early-warning detection that educators can act on immediately.

#### ✅ Explainable
- No black-box AI
- Every decision is rule-based and transparent

#### 🔒 Respects Privacy
- No emotion detection
- No personal monitoring

#### ⏰ Early Detection
- Identifies risk before performance drops
- Enables proactive intervention

#### 🚀 Ready to Deploy
- Simple logic that institutions can adopt immediately
- No special infrastructure needed

---

## 👨‍🏫 Mentor Workflow

1. **Assessment**: Students input their current workload (subjects, assignments, hours, deadlines)
2. **Detection**: System calculates ALI and flags overload status
3. **Dashboard**: Mentors view all students sorted by risk
4. **Intervention**: Reach out to students at risk before they fail
5. **Action**: Extend deadlines, redistribute work, or reduce scope as needed

### Sample Mentor Actions

- ✅ **Safe students**: Celebrate balance; encourage continued discipline
- ⚠️ **Warning students**: Check in regularly; offer workload review
- 🚨 **Critical students**: Prioritize intervention immediately

### Key Message to Communicate

> "This system doesn't predict emotion or stress.
> It simply tells us if your assigned workload fits your available time.
> Our job is to help you manage that balance."

---

## 🛠️ Design Principles

### 1. Rule-Based, Not Predictive
We quantify workload feasibility using simple math, not machine learning.

### 2. Explainable to All Stakeholders
Students, mentors, and administrators understand the logic immediately.

### 3. Conservative Estimate
We use the tightest deadline to ensure realistic capacity assessment.
This means our thresholds are conservative (less likely to miss overload).

### 4. Low Barrier to Adoption
- No special infrastructure
- No AI ethics review
- No privacy concerns
- Institutions can implement this today

### 5. Privacy-Respecting
- No emotion detection
- No biometric data
- No surveillance
- Only explicit workload input from students

---

## ⚠️ Limitations & Future Work

### Current Limitations

- Assumes uniform study distribution
- Treats all assignments as equally difficult
- Doesn't factor in student prior knowledge
- Manual input only (no automatic LMS integration)
- Doesn't detect deadline clustering periods

### Future Enhancements

- **LMS Integration**: Auto-pull assignments and deadlines
- **Deadline Clustering**: Flag high-pressure periods
- **Student Profile**: Adjust thresholds based on major/year
- **Predictive Scheduling**: Suggest optimal deadline redistribution
- **Intervention Templates**: Guide mentors on support

---

## 📖 Quick Reference

### When to Worry (ALI > 1.3)

A student with ALI = 1.5 needs 50% more time than they have.
Without intervention, they will miss deadlines and experience burnout.

### When to Monitor (1.0 ≤ ALI ≤ 1.3)

These students are on the edge. Any disruption could tip them into crisis.
Check in regularly and offer support.

### When They're Safe (ALI < 1.0)

These students have breathing room.
Use this time to deepen learning and prevent complacency.

---

## 🚀 Getting Started

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```bash
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

### Features

- ✅ Simple ALI calculation
- 📊 Student dashboard with metrics
- 📥 CSV export functionality
- 🎨 Modern dark theme UI
- 💾 Session-based data storage

---

## 📋 System Pages

### 1. Home
- ALI explanation and system overview
- Feature cards explaining Safe/Warning/Critical
- Real-world examples
- System statistics

### 2. Assess
- Calculate your personal ALI
- Input your name and study hours per day
- Add subjects and assignment details
- Get instant feedback on your workload
- View assignment breakdown

### 3. Dashboard
- View all assessments and statistics
- Visual ALI gauges for each student
- System overview metrics
- Download reports in CSV format
- Clear data as needed

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit** - Web framework
- **Pandas** - Data processing
- **DateTime** - Timestamp management

---

## 📁 Project Structure

```
academiq/
├── app.py                 # Main application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
└── docs/
    └── DESIGN.md         # Detailed design documentation
```

---


***

## 🚀 How to Run AcademiQ

To try AcademiQ on your own laptop, you only need Python and a few commands. First, download or clone this repository to your machine. Then open a terminal in the project folder and create a small isolated Python environment so this project doesn’t interfere with your other work. On most systems you can do:

```bash
python -m venv venv
```

Activate this environment (`venv\Scripts\activate` on Windows, `source venv/bin/activate` on macOS/Linux), then install the required packages:

```bash
pip install -r requirements.txt
```

Once the setup is done, start the app with:

```bash
streamlit run app.py
```

A browser window will open automatically. From there you can explore the student view, the mentor dashboard, and see how the Academic Load Index highlights overload before it turns into burnout.

---


## 💾 Requirements

```
streamlit==1.28.1
pandas==2.0.3
```

---

## 📝 License

MIT License - Feel free to use, modify, and distribute.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

---

## 📧 Contact & Support

For questions, feedback, or suggestions, please open an issue on GitHub.

---

## 💡 Bottom Line

**Academic overload is predictable and preventable with transparent data and timely intervention.**

This system gives mentors and institutions the tools to:
- Detect workload problems early
- Intervene before students fail
- Maintain sustainable academic environments
- Support student success

---

**Made with ❤️ for student success**
