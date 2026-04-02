# Student Performance Analysis & Prediction

## Project Overview

This project performs **end-to-end data analysis and machine learning** on a student dataset. It explores student performance, visualizes insights, and builds a predictive model to determine whether a student will **Pass or Fail**.

The dataset is intentionally small (15 students) to help understand each step clearly.

---

## Dataset Description

File: `students.csv`

Each row represents a student with the following features:

| Column                              | Description                          |
| ----------------------------------- | ------------------------------------ |
| name                                | Student name                         |
| math, science, english, history, pe | Subject scores                       |
| attendance_pct                      | Attendance percentage                |
| study_hours_per_day                 | Daily study hours                    |
| passed                              | Target variable (1 = Pass, 0 = Fail) |

---

## Technologies Used

* Python
* Pandas (Data Analysis)
* NumPy
* Matplotlib (Visualization)
* Seaborn (Advanced Visualization)
* Scikit-learn (Machine Learning)

---

## How to Run the Project

1. Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

2. Place files in the same folder:

```
main.py
students.csv
```

---

## Task Breakdown

### Task 1 — Data Exploration

* Loaded dataset using Pandas
* Checked structure and data types
* Generated summary statistics
* Compared Pass vs Fail students
* Identified top-performing student

---

### Task 2 — Matplotlib Visualizations

Generated and saved:

1. Bar Chart — Average score per subject
2. Histogram — Math score distribution
3. Scatter Plot — Study hours vs average score
4. Box Plot — Attendance (Pass vs Fail)
5. Line Plot — Math & Science scores per student

---

### Task 3 — Seaborn Visualizations

* Bar plots comparing Math & Science scores by Pass/Fail
* Scatter plot with regression lines (Attendance vs Performance)

**Observation:**
Seaborn simplifies statistical plotting and styling, while Matplotlib offers more flexibility but requires more manual effort.

---

### Task 4 — Machine Learning Model

#### Model Used:

* Logistic Regression

#### Steps:

* Feature selection
* Train-test split (80/20)
* Feature scaling using StandardScaler
* Model training & evaluation

#### Outputs:

* Training Accuracy
* Test Accuracy
* Individual predictions with correctness check

---

### Feature Importance

* Extracted coefficients from Logistic Regression
* Visualized impact of each feature

Interpretation:

* Positive coefficient → increases chance of Pass
* Negative coefficient → increases chance of Fail

---

### Bonus — Prediction

* Predicted result for a new student
* Displayed probability of Pass/Fail

---

## Output Files

The following plots are generated:

```
plot1_bar.png
plot2_hist.png
plot3_scatter.png
plot4_box.png
plot5_line.png
plot6_seaborn_bar.png
plot7_seaborn_scatter.png
plot8_feature_importance.png
```

---

## Important Notes

* Small dataset → results may not generalize well
* Model accuracy may vary due to limited data
* Focus is on **understanding workflow**, not optimization

---
