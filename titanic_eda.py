"""
Exploratory Data Analysis (EDA) on Titanic Dataset
Author: HEX Softwares
Date: February 2026

This script performs comprehensive exploratory data analysis on the Titanic dataset,
including data cleaning, statistical analysis, and visualization.
"""

import pandas as pd # pyright: ignore[reportMissingModuleSource]
import numpy as np
import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]
import seaborn as sns # type: ignore
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

print("="*80)
print("EXPLORATORY DATA ANALYSIS - TITANIC DATASET")
print("="*80)

# ============================================================================
# 1. DATA LOADING
# ============================================================================
print("\n1. LOADING DATA...")
print("-"*80)

df = pd.read_csv('/home/claude/titanic.csv')

print(f"✓ Dataset loaded successfully")
print(f"  Shape: {df.shape[0]} rows × {df.shape[1]} columns")

# ============================================================================
# 2. DATA EXPLORATION
# ============================================================================
print("\n2. DATA EXPLORATION")
print("-"*80)

print("\nFirst 5 rows:")
print(df.head())

print("\n\nDataset Information:")
print(df.info())

print("\n\nStatistical Summary:")
print(df.describe())

print("\n\nColumn Names:")
print(df.columns.tolist())

# ============================================================================
# 3. DATA CLEANING
# ============================================================================
print("\n3. DATA CLEANING")
print("-"*80)

print("\nMissing Values:")
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({
    'Column': missing.index,
    'Missing Count': missing.values,
    'Percentage': missing_pct.values
})
print(missing_df[missing_df['Missing Count'] > 0])

# Handle missing values
print("\nHandling missing values:")

# Age: Fill with median
age_median = df['Age'].median()
df['Age'].fillna(age_median, inplace=True)
print(f"  ✓ Age: Filled {missing['Age']} missing values with median ({age_median:.1f})")

# Embarked: Fill with mode
embarked_mode = df['Embarked'].mode()[0]
df['Embarked'].fillna(embarked_mode, inplace=True)
print(f"  ✓ Embarked: Filled {missing['Embarked']} missing values with mode ('{embarked_mode}')")

# Cabin: Create binary feature for cabin availability
df['Has_Cabin'] = df['Cabin'].notna().astype(int)
print(f"  ✓ Cabin: Created 'Has_Cabin' binary feature")

# Drop Cabin column
df.drop('Cabin', axis=1, inplace=True)

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"\nDuplicates found: {duplicates}")

# ============================================================================
# 4. FEATURE ENGINEERING
# ============================================================================
print("\n4. FEATURE ENGINEERING")
print("-"*80)

# Family size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print(f"✓ Created 'FamilySize' feature (SibSp + Parch + 1)")

# Is alone
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
print(f"✓ Created 'IsAlone' binary feature")

# Age groups
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 35, 60, 100], 
                         labels=['Child', 'Teenager', 'Adult', 'Middle-aged', 'Senior'])
print(f"✓ Created 'AgeGroup' categorical feature")

# Fare groups
df['FareGroup'] = pd.qcut(df['Fare'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])
print(f"✓ Created 'FareGroup' categorical feature")

# Title extraction from name
df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
print(f"✓ Extracted 'Title' from Name")

# Simplify titles
title_mapping = {
    'Mr': 'Mr', 'Miss': 'Miss', 'Mrs': 'Mrs', 'Master': 'Master',
    'Dr': 'Rare', 'Rev': 'Rare', 'Col': 'Rare', 'Major': 'Rare', 
    'Mlle': 'Miss', 'Mme': 'Mrs', 'Don': 'Rare', 'Dona': 'Rare',
    'Lady': 'Rare', 'Countess': 'Rare', 'Jonkheer': 'Rare', 'Sir': 'Rare',
    'Capt': 'Rare', 'Ms': 'Miss'
}
df['Title'] = df['Title'].map(title_mapping)
df['Title'].fillna('Rare', inplace=True)
print(f"  Titles mapped to: {df['Title'].unique().tolist()}")

# ============================================================================
# 5. STATISTICAL ANALYSIS
# ============================================================================
print("\n5. STATISTICAL ANALYSIS")
print("-"*80)

print("\nSurvival Rate:")
survival_rate = df['Survived'].mean() * 100
print(f"  Overall: {survival_rate:.2f}%")

print("\nSurvival by Gender:")
gender_survival = df.groupby('Sex')['Survived'].agg(['mean', 'count'])
gender_survival.columns = ['Survival Rate', 'Count']
gender_survival['Survival Rate'] = (gender_survival['Survival Rate'] * 100).round(2)
print(gender_survival)

print("\nSurvival by Class:")
class_survival = df.groupby('Pclass')['Survived'].agg(['mean', 'count'])
class_survival.columns = ['Survival Rate', 'Count']
class_survival['Survival Rate'] = (class_survival['Survival Rate'] * 100).round(2)
print(class_survival)

print("\nSurvival by Embarkation Port:")
embark_survival = df.groupby('Embarked')['Survived'].agg(['mean', 'count'])
embark_survival.columns = ['Survival Rate', 'Count']
embark_survival['Survival Rate'] = (embark_survival['Survival Rate'] * 100).round(2)
print(embark_survival)

print("\nAge Statistics by Survival:")
age_stats = df.groupby('Survived')['Age'].describe()
print(age_stats)

print("\nFare Statistics by Survival:")
fare_stats = df.groupby('Survived')['Fare'].describe()
print(fare_stats)

# Correlation analysis
print("\nCorrelation with Survival (numerical features):")
numerical_cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'FamilySize', 'IsAlone', 'Has_Cabin']
correlation = df[numerical_cols].corr()['Survived'].sort_values(ascending=False)
print(correlation)

# ============================================================================
# 6. VISUALIZATIONS
# ============================================================================
print("\n6. CREATING VISUALIZATIONS")
print("-"*80)

# Create figure directory
import os
os.makedirs('/home/claude/figures', exist_ok=True)

# 1. Survival Distribution
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=df, x='Survived', palette='Set2')
plt.title('Survival Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Survived (0 = No, 1 = Yes)', fontsize=12)
plt.ylabel('Count', fontsize=12)
for container in ax.containers:
    ax.bar_label(container)
plt.tight_layout()
plt.savefig('/home/claude/figures/01_survival_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 01_survival_distribution.png")
plt.close()

# 2. Survival by Gender
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=df, x='Sex', hue='Survived', palette='Set1')
plt.title('Survival by Gender', fontsize=16, fontweight='bold')
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(title='Survived', labels=['No', 'Yes'])
for container in ax.containers:
    ax.bar_label(container)
plt.tight_layout()
plt.savefig('/home/claude/figures/02_survival_by_gender.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 02_survival_by_gender.png")
plt.close()

# 3. Survival by Passenger Class
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=df, x='Pclass', hue='Survived', palette='viridis')
plt.title('Survival by Passenger Class', fontsize=16, fontweight='bold')
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(title='Survived', labels=['No', 'Yes'])
for container in ax.containers:
    ax.bar_label(container)
plt.tight_layout()
plt.savefig('/home/claude/figures/03_survival_by_class.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 03_survival_by_class.png")
plt.close()

# 4. Age Distribution
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sns.histplot(data=df[df['Survived']==0], x='Age', bins=30, kde=True, color='red', 
             alpha=0.6, ax=axes[0], label='Did not survive')
axes[0].set_title('Age Distribution - Did Not Survive', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Age', fontsize=12)
axes[0].set_ylabel('Frequency', fontsize=12)

sns.histplot(data=df[df['Survived']==1], x='Age', bins=30, kde=True, color='green', 
             alpha=0.6, ax=axes[1], label='Survived')
axes[1].set_title('Age Distribution - Survived', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Age', fontsize=12)
axes[1].set_ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.savefig('/home/claude/figures/04_age_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 04_age_distribution.png")
plt.close()

# 5. Fare Distribution
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Pclass', y='Fare', hue='Survived', palette='coolwarm')
plt.title('Fare Distribution by Class and Survival', fontsize=16, fontweight='bold')
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Fare', fontsize=12)
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.tight_layout()
plt.savefig('/home/claude/figures/05_fare_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 05_fare_distribution.png")
plt.close()

# 6. Correlation Heatmap
plt.figure(figsize=(12, 10))
corr_matrix = df[numerical_cols].corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, mask=mask, fmt='.2f')
plt.title('Correlation Heatmap', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('/home/claude/figures/06_correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 06_correlation_heatmap.png")
plt.close()

# 7. Survival by Embarkation Port
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=df, x='Embarked', hue='Survived', palette='Set3')
plt.title('Survival by Embarkation Port', fontsize=16, fontweight='bold')
plt.xlabel('Embarkation Port (C=Cherbourg, Q=Queenstown, S=Southampton)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(title='Survived', labels=['No', 'Yes'])
for container in ax.containers:
    ax.bar_label(container)
plt.tight_layout()
plt.savefig('/home/claude/figures/07_survival_by_embarkation.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 07_survival_by_embarkation.png")
plt.close()

# 8. Family Size Impact
plt.figure(figsize=(12, 6))
family_survival = df.groupby('FamilySize')['Survived'].mean().reset_index()
ax = sns.barplot(data=family_survival, x='FamilySize', y='Survived', palette='magma')
plt.title('Survival Rate by Family Size', fontsize=16, fontweight='bold')
plt.xlabel('Family Size', fontsize=12)
plt.ylabel('Survival Rate', fontsize=12)
plt.axhline(y=survival_rate/100, color='red', linestyle='--', label=f'Overall Avg: {survival_rate:.1f}%')
plt.legend()
for container in ax.containers:
    ax.bar_label(container, fmt='%.2f')
plt.tight_layout()
plt.savefig('/home/claude/figures/08_survival_by_family_size.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 08_survival_by_family_size.png")
plt.close()

# 9. Survival by Title
plt.figure(figsize=(12, 6))
title_survival = df.groupby('Title')['Survived'].agg(['mean', 'count']).reset_index()
title_survival = title_survival.sort_values('mean', ascending=False)
ax = sns.barplot(data=title_survival, x='Title', y='mean', palette='rocket')
plt.title('Survival Rate by Title', fontsize=16, fontweight='bold')
plt.xlabel('Title', fontsize=12)
plt.ylabel('Survival Rate', fontsize=12)
for i, (title, survival_rate_val, count) in enumerate(title_survival.values):
    ax.text(i, survival_rate_val + 0.02, f'{survival_rate_val:.2f}\n(n={count})', 
            ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.savefig('/home/claude/figures/09_survival_by_title.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 09_survival_by_title.png")
plt.close()

# 10. Multi-variable analysis: Class, Gender, and Survival
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
for i, pclass in enumerate([1, 2, 3]):
    class_data = df[df['Pclass'] == pclass]
    ax = sns.countplot(data=class_data, x='Sex', hue='Survived', palette='Spectral', ax=axes[i])
    axes[i].set_title(f'Class {pclass} - Survival by Gender', fontsize=12, fontweight='bold')
    axes[i].set_xlabel('Gender', fontsize=10)
    axes[i].set_ylabel('Count', fontsize=10)
    axes[i].legend(title='Survived', labels=['No', 'Yes'])
    for container in ax.containers:
        ax.bar_label(container)
plt.tight_layout()
plt.savefig('/home/claude/figures/10_class_gender_survival.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 10_class_gender_survival.png")
plt.close()

# ============================================================================
# 7. KEY INSIGHTS & SUMMARY
# ============================================================================
print("\n7. KEY INSIGHTS")
print("-"*80)

print("\n📊 SURVIVAL STATISTICS:")
print(f"   • Overall survival rate: {survival_rate:.2f}%")
print(f"   • Total passengers: {len(df)}")
print(f"   • Survivors: {df['Survived'].sum()}")
print(f"   • Non-survivors: {len(df) - df['Survived'].sum()}")

print("\n👥 DEMOGRAPHIC INSIGHTS:")
female_survival = df[df['Sex']=='female']['Survived'].mean() * 100
male_survival = df[df['Sex']=='male']['Survived'].mean() * 100
print(f"   • Female survival rate: {female_survival:.2f}%")
print(f"   • Male survival rate: {male_survival:.2f}%")
print(f"   • Gender survival difference: {abs(female_survival - male_survival):.2f}%")

print("\n🎫 CLASS-BASED INSIGHTS:")
for pclass in [1, 2, 3]:
    class_surv = df[df['Pclass']==pclass]['Survived'].mean() * 100
    print(f"   • Class {pclass} survival rate: {class_surv:.2f}%")

print("\n👨‍👩‍👧‍👦 FAMILY INSIGHTS:")
alone_survival = df[df['IsAlone']==1]['Survived'].mean() * 100
with_family_survival = df[df['IsAlone']==0]['Survived'].mean() * 100
print(f"   • Alone passengers survival: {alone_survival:.2f}%")
print(f"   • With family survival: {with_family_survival:.2f}%")

print("\n🚢 EMBARKATION INSIGHTS:")
for port in df['Embarked'].unique():
    if pd.notna(port):
        port_surv = df[df['Embarked']==port]['Survived'].mean() * 100
        port_name = {'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'}[port]
        print(f"   • {port_name} ({port}): {port_surv:.2f}%")

print("\n🔍 CORRELATION INSIGHTS:")
top_positive = correlation[correlation > 0].iloc[1:4]
top_negative = correlation[correlation < 0].iloc[:3]
print("   Positive correlations with survival:")
for feature, corr in top_positive.items():
    print(f"      • {feature}: {corr:.3f}")
print("   Negative correlations with survival:")
for feature, corr in top_negative.items():
    print(f"      • {feature}: {corr:.3f}")

# ============================================================================
# 8. SAVE CLEANED DATA
# ============================================================================
print("\n8. SAVING CLEANED DATA")
print("-"*80)

# Save to CSV
df.to_csv('/home/claude/titanic_cleaned.csv', index=False)
print("✓ Saved cleaned dataset: titanic_cleaned.csv")

# Create summary statistics file
summary_stats = df.describe(include='all').T
summary_stats.to_csv('/home/claude/titanic_summary_statistics.csv')
print("✓ Saved summary statistics: titanic_summary_statistics.csv")

print("\n" + "="*80)
print("ANALYSIS COMPLETE!")
print("="*80)
print(f"\nTotal files generated:")
print(f"  • 1 Python script (titanic_eda.py)")
print(f"  • 2 CSV files (cleaned data + summary statistics)")
print(f"  • 10 visualization images")
print("\n✓ All files saved successfully!")
