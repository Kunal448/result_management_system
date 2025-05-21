import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_gsheets import GSheetsConnection

def page4():
    url = "https://docs.google.com/spreadsheets/d/1Bd7iDW_uNA-ttIMYgtsFBs7fFlx-Yzq9DEMCdPNKFxg/edit?usp=sharing"
    conn = st.connection("gsheets", type = GSheetsConnection)
    
    data = conn.read(worksheet="Sheet1", ttl=3)
    df = pd.DataFrame(data)
    
    st.title("Analyze Result")
    '''st.write("Distribution of Marks on Subjects")
    
    
    subjects = ['English', 'Hindi', 'Maths', 'SS', 'Science']
    
    
    fig, axs = plt.subplots(len(subjects), 1, figsize=(8, len(subjects) * 4))

    for i, subject in enumerate(subjects):
        ax = axs[i]
        sns.boxplot(x=df[subject], ax=ax)
        ax.set_title(f"Box Plot of {subject} Marks")
        ax.set_xlabel("Marks")

    # Adjust layout and display
    plt.tight_layout()
    st.pyplot(fig)
    
    
    
    st.title("Result Breakdown: Pass/Fail (Pie Chart)")

    # Count the occurrences of Pass and Fail
    result_counts = df['Result'].value_counts()
    
    # Create a pie chart
    fig, ax = plt.subplots(figsize=(6, 6))
    result_counts.plot(
        kind='pie',
        labels=result_counts.index,
        autopct='%1.1f%%',
        colors=['green', 'red'],
        startangle=90,
        ax=ax
    )
    ax.set_title("Pass/Fail Distribution")
    ax.set_ylabel('')  # Hides the y-axis label for the pie chart
    
    # Display the plot
    st.pyplot(fig)'''
    
    
    
    
    st.title("Top Performers in Each Subject (Horizontal Stacked Chart)")

    # Select top N performers
    top_n = st.slider("Select number of top performers to display:", min_value=1, max_value=10, value=5)
    
    # Filter the top N performers
    top_performers = df.nlargest(top_n, ['English', 'Hindi', 'Maths', 'SS', 'Science'])
    
    # Select only the numerical columns (subjects)
    subject_columns = ['English', 'Hindi', 'Maths', 'SS', 'Science']
    top_performers_data = top_performers[subject_columns]
    
    # Create a horizontal stacked bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    top_performers_data.set_index(top_performers['Name']).plot(
        kind='barh',
        stacked=True,
        ax=ax,
        colormap='tab20c'
    )
    ax.set_title(f"Top {top_n} Performers in Each Subject")
    ax.set_xlabel("Total Marks")
    ax.set_ylabel("Student Names")
    plt.tight_layout()
    
    # Display the plot
    st.pyplot(fig)
    
    
    
    
    
    
    
    st.title("Grade Distribution (Bar Chart)")

    # Count the occurrences of each grade
    grade_counts = df['Grade'].value_counts()
    
    # Create a bar chart
    fig, ax = plt.subplots(figsize=(8, 6))
    grade_counts.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title("Grade Distribution")
    ax.set_xlabel("Grade")
    ax.set_ylabel("Count")
    ax.set_xticklabels(grade_counts.index, rotation=0)
    
    # Display the plot
    st.pyplot(fig)
    
    
    
    
    
    
    
    
    st.title("Average Scores of Each Subject (Bar Chart)")

    # Calculate average scores for each subject
    subject_columns = ['English', 'Hindi', 'Maths', 'SS', 'Science']
    average_scores = df[subject_columns].mean()
    
    # Create bar chart
    fig, ax = plt.subplots(figsize=(8, 6))
    average_scores.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title("Average Scores of Each Subject")
    ax.set_xlabel("Subjects")
    ax.set_ylabel("Average Marks")
    ax.set_xticklabels(average_scores.index, rotation=45)
    
    # Display the plot
    st.pyplot(fig)
    
    
    
    
    
    
    
    st.title("Density Plot for Percentage Distribution")

    # Create density plot for the percentage column
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.kdeplot(df['Percentage'], fill=True, color='skyblue', alpha=0.3, ax=ax)
    
    ax.set_title("Density Plot of Percentages Distribution")
    ax.set_xlabel("Percentage")
    ax.set_ylabel("Density")
    
    # Display the plot
    st.pyplot(fig)
    
    
    
    
    
    st.title("Stacked Bar Chart - Marks Distribution by Subjects")

    # Extract subjects and names
    subject_columns = ['English', 'Hindi', 'Maths', 'SS', 'Science']
    names = df['Name']
    
    # Create stacked bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot each subject as a stacked bar
    bottom_values = [0] * len(names)  # Initialize bottom values for stacking
    for subject in subject_columns:
        ax.bar(names, df[subject], label=subject, bottom=bottom_values)
        bottom_values = [i + j for i, j in zip(bottom_values, df[subject])]
    
    # Customize chart
    ax.set_title("Marks Distribution Across Subjects")
    ax.set_xlabel("Students")
    ax.set_ylabel("Marks")
    ax.legend(title="Subjects")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Display the plot
    st.pyplot(fig)