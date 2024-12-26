import pandas as pd
from datetime import datetime, timedelta

# Get current date and dates for testing
now = datetime.now()
two_weeks_ago = now - timedelta(weeks=2)
four_weeks_ago = now - timedelta(weeks=4)

# Create test DataFrame with meaningful data for pivot table and markdown analysis
df = pd.DataFrame({
    'Type': ['Project'] * 15,
    'Status': ['Completed', 'Red', 'Yellow', 'Green',  # Include only some statuses
               'Red', 'Yellow', 'Green', 'Completed',
               'Red', 'Yellow', 'Green', 'Green',
               'Red', 'Yellow', 'Green'],  # No DNM, Completed Late, or Cancelled
    'Title': [f'Sample Goal {i}' for i in range(1, 16)],
    'Description': [f'Description for goal {i}' for i in range(1, 16)],
    'Date': [now.strftime('%Y-%m-%d')] * 15,
    'Modified': [
        # Recent modifications (within 3 weeks)
        now.strftime('%Y-%m-%d'),           # Completed
        now.strftime('%Y-%m-%d'),           # Completed Late
        two_weeks_ago.strftime('%Y-%m-%d'), # DNM
        two_weeks_ago.strftime('%Y-%m-%d'), # Cancelled
        now.strftime('%Y-%m-%d'),           # Red
        now.strftime('%Y-%m-%d'),           # Yellow
        now.strftime('%Y-%m-%d'),           # Green
        # Old modifications (over 3 weeks ago)
        four_weeks_ago.strftime('%Y-%m-%d'), # Completed
        four_weeks_ago.strftime('%Y-%m-%d'), # Completed Late
        four_weeks_ago.strftime('%Y-%m-%d'), # DNM
        four_weeks_ago.strftime('%Y-%m-%d'), # Cancelled
        now.strftime('%Y-%m-%d'),            # Red
        now.strftime('%Y-%m-%d'),            # Yellow
        now.strftime('%Y-%m-%d'),            # Green
        now.strftime('%Y-%m-%d'),            # Green
    ],
    'Created': [
        now.strftime('%Y-%m-%d')] * 13 + [
        two_weeks_ago.strftime('%Y-%m-%d'),  # Green (recent)
        four_weeks_ago.strftime('%Y-%m-%d'), # Green (old)
    ],
    'Team': ['Team A', 'Team B', 'Team A', 'Team B', 'Team A',
             'Team B', 'Team A', 'Team B', 'Team A', 'Team B',
             'Team A', 'Team B', 'Team A', 'Team B', 'Team A'],
    'Goal Set': ['LT'] * 15,
    'ID': [f'ID_{i:03d}' for i in range(1, 16)],
    'Status Comments': [f'Latest status update for goal {i}' for i in range(1, 16)],
    'Path to Green': [f'Path to green for goal {i}' if i % 2 == 0 else None for i in range(1, 16)],
    'Modified By': ['User A', 'User B'] * 7 + ['User A'],
    'Orig Due Date': [(now + timedelta(days=30)).strftime('%Y-%m-%d')] * 15,
    'Owners': ['Owner A, Owner B'] * 15
})

# Save to Excel file
df.to_excel('test_input.xlsx', index=False)
print("Test input file 'test_input.xlsx' has been created successfully.")
