import pandas as pd

# Create test DataFrame with meaningful data for pivot table analysis
df = pd.DataFrame({
    'Type': ['Project', 'Initiative', 'Project', 'Initiative', 'Project', 
             'Project', 'Initiative', 'Project', 'Initiative', 'Project'],
    'Status': ['In Progress', 'Completed', 'In Progress', 'Not Started', 'Completed',
               'In Progress', 'Completed', 'Not Started', 'In Progress', 'Completed'],
    'Title': [f'Sample Title {i}' for i in range(1, 11)],
    'Description': [f'Desc {i}' for i in range(1, 11)],
    'Date': [
        '2024-02-15',  # Q1 current year
        '2024-02-20',  # Q1 current year
        '2024-05-20',  # Q2 current year
        '2024-05-25',  # Q2 current year
        '2024-08-10',  # Q3 current year
        '2024-08-15',  # Q3 current year
        '2024-11-25',  # Q4 current year
        '2024-11-30',  # Q4 current year
        '2025-02-07',  # Q1'25 future year
        '2025-02-10',  # Q1'25 future year
    ],
    'Primary SVP': ['SVP1', 'SVP2', 'SVP1', 'SVP2', 'SVP3',
                    'SVP1', 'SVP2', 'SVP3', 'SVP1', 'SVP2'],
    'Team': ['Team A', 'Team B', 'Team A', 'Team B', 'Team C',
             'Team A', 'Team B', 'Team C', 'Team A', 'Team B'],
    'Goal Set': ['Set 1', 'Set 2', 'Set 1', 'Set 2', 'Set 1',
                 'Set 2', 'Set 1', 'Set 2', 'Set 1', 'Set 2'],
    'ID': [f'ID_{i:03d}' for i in range(1, 11)]
})

# Save to Excel file
df.to_excel('test_input.xlsx', index=False)
print("Test input file 'test_input.xlsx' has been created successfully.")
