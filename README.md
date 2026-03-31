# Titanic Dataset - Exploratory Data Analysis (EDA)  

## 📊 Project Overview  

This project performs a comprehensive Exploratory Data Analysis on the famous Titanic dataset, analyzing survival patterns, demographics, and key factors that influenced passenger outcomes during the tragic disaster.
   
**Project Type:** Data Science / Exploratory Data Analysis    
**Dataset:** Titanic Passenger Data (891 passengers)           
**Tools:** Python, Pandas, Matplotlib, Seaborn     
**Completion Date:** February 2026    
      
---

## 🎯 Objectives  
 
1. **Data Cleaning:** Handle missing values and prepare data for analysis
2. **Statistical Analysis:** Compute survival rates, correlations, and distributions
3. **Feature Engineering:** Create meaningful derived variables
4. **Visualization:** Generate comprehensive charts to identify patterns    
5. **Insight Generation:** Extract actionable insights about survival factors

---  

## 📁 Project Structure 

```
titanic-eda/
│
├── titanic_eda.py                      # Main analysis script
├── titanic.csv                         # Original dataset
├── titanic_cleaned.csv                 # Cleaned dataset with new features
├── titanic_summary_statistics.csv      # Statistical summaries
├── TITANIC_EDA_REPORT.md              # Comprehensive analysis report
├── README.md                           # This file
│
└── figures/                            # Visualization outputs
    ├── 01_survival_distribution.png
    ├── 02_survival_by_gender.png
    ├── 03_survival_by_class.png
    ├── 04_age_distribution.png
    ├── 05_fare_distribution.png
    ├── 06_correlation_heatmap.png
    ├── 07_survival_by_embarkation.png
    ├── 08_survival_by_family_size.png
    ├── 09_survival_by_title.png
    └── 10_class_gender_survival.png 
```

---

## 🔑 Key Findings
 
### Survival Statistics
- **Overall Survival Rate:** 36.59% (326/891 passengers)
- **By Class:**
  - 1st Class: 62.78% ⭐
  - 2nd Class: 44.12%
  - 3rd Class: 22.29% 
- **By Gender:** 
  - Female: 42.68%
  - Male: 33.28%

### Critical Insights
1. **Class Matters Most** - First-class passengers had 2.8x higher survival rate than third-class
2. **Gender Played a Role** - "Women and children first" protocol evident
3. **Family Dynamics** - Small families (2-4 members) showed best survival outcomes
4. **Economic Disparity** - Higher fares strongly correlated with better survival
5. **Age Impact Limited** - Weak direct correlation, but children slightly favored

---

## 🛠️ Technologies Used

### Core Libraries
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **matplotlib** - Data visualization
- **seaborn** - Statistical plotting

### Python Version
- Python 3.8+

---

## 🚀 How to Run

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn
```

### Execution
```bash
python titanic_eda.py
```

### Expected Output
- Cleaned dataset (CSV)
- Summary statistics (CSV)
- 10 visualization images (PNG)
- Console output with analysis results

---

## 📈 Analysis Steps

### 1. Data Loading & Exploration
- Load dataset (891 rows × 12 columns)
- Initial inspection of data types and structure
- Identify missing values and data quality issues

### 2. Data Cleaning
- **Age:** Filled 178 missing values (19.98%) with median
- **Embarked:** Filled 1 missing value with mode
- **Cabin:** Created binary indicator for cabin presence
- **Duplicates:** None found

### 3. Feature Engineering
- **FamilySize:** SibSp + Parch + 1
- **IsAlone:** Binary indicator for solo travelers
- **AgeGroup:** Categorical age bins
- **FareGroup:** Quartile-based fare categories
- **Title:** Extracted from passenger names

### 4. Statistical Analysis
- Survival rate calculations
- Cross-tabulations by demographics
- Correlation analysis
- Distribution analysis

### 5. Visualization
- 10 comprehensive charts covering:
  - Univariate distributions
  - Bivariate relationships
  - Multi-variate interactions
  - Correlation heatmaps

---

## 📊 Visualizations

### 1. Survival Distribution
Overall count of survivors vs. non-survivors showing 2:1 ratio

### 2. Survival by Gender
Gender comparison highlighting "women first" protocol

### 3. Survival by Passenger Class
Dramatic disparity across socioeconomic classes

### 4. Age Distribution
Comparison of age patterns between survivors and non-survivors

### 5. Fare Distribution
Box plots showing fare variation by class and survival status

### 6. Correlation Heatmap
Inter-variable correlation matrix with survival focus

### 7. Survival by Embarkation Port
Minimal variation across Cherbourg, Queenstown, and Southampton

### 8. Survival by Family Size
Optimal survival for small families (2-4 members)

### 9. Survival by Title
Social status indicator impact on outcomes

### 10. Class-Gender-Survival Interaction
Three-way interaction showing compounded effects 

---

## 📝 Dataset Description

### Variables (12 total)

| Variable | Type | Description |
|----------|------|-------------|
| PassengerId | int | Unique identifier |
| Survived | int | 0 = No, 1 = Yes |
| Pclass | int | Ticket class (1/2/3) |
| Name | str | Passenger name |
| Sex | str | Gender (male/female) |
| Age | float | Age in years |
| SibSp | int | # siblings/spouses aboard |
| Parch | int | # parents/children aboard |
| Ticket | str | Ticket number |
| Fare | float | Passenger fare (£) |
| Cabin | str | Cabin number |
| Embarked | str | Port (C/Q/S) |

---

## 📖 Documentation

### Main Report
See `TITANIC_EDA_REPORT.md` for the comprehensive analysis report including:
- Executive Summary
- Detailed Statistical Analysis
- Visual Analysis
- Key Insights & Conclusions
- Technical Appendix
- Recommendations for Further Analysis

### Code Documentation
The `titanic_eda.py` script is well-commented and organized into sections:
1. Data Loading
2. Data Exploration
3. Data Cleaning
4. Feature Engineering
5. Statistical Analysis
6. Visualizations
7. Key Insights
8. Data Export 

---

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- ✅ Data cleaning and preprocessing
- ✅ Handling missing values appropriately
- ✅ Feature engineering for enhanced analysis
- ✅ Statistical analysis and hypothesis testing
- ✅ Data visualization best practices
- ✅ Correlation analysis
- ✅ Insight extraction and communication
- ✅ Professional documentation

---

## 🔮 Future Enhancements

### Potential Extensions
1. **Predictive Modeling**
   - Build logistic regression model
   - Random forest classification
   - Model comparison and evaluation

2. **Advanced Analysis**
   - Survival time analysis (if timestamp data available)
   - Network analysis of family connections
   - Spatial analysis of cabin locations

3. **Interactive Dashboard**
   - Build Streamlit/Dash dashboard
   - Interactive filtering and exploration
   - Real-time statistical updates

4. **Machine Learning**
   - Feature importance analysis
   - Cross-validation techniques
   - Ensemble methods

---

## 📜 License

This project is created for educational purposes as part of the HEX Softwares data science curriculum.

---

## 👥 Author

**HEX Softwares**  
*Innovate | Connect | Inspire*

---

## 📞 Contact

For questions or feedback about this analysis:
- Review the comprehensive report in `TITANIC_EDA_REPORT.md`
- Examine the code in `titanic_eda.py`
- Check visualizations in the `figures/` directory

---

## ✅ Completion Checklist

- [x] Load and explore dataset
- [x] Handle missing values
- [x] Perform data cleaning
- [x] Engineer new features
- [x] Conduct statistical analysis  
- [x] Generate visualizations
- [x] Extract key insights
- [x] Create comprehensive report
- [x] Document code properly
- [x] Organize project files

-----
 
**Project Status:** ✅ **COMPLETE**

*Last Updated: February 2026*    
