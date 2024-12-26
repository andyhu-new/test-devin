import pandas as pd

def verify_excel_output(filename: str) -> None:
    """Verify that the Excel file contains all required columns, correct quarter values, and pivot tables."""
    required_columns = [
        "Type", "Title + Description", "Description + PTG", 
        "Desc + Status Comments + PTG", "Description + Status Comments",
        "Status Comments + PTG", "Target Year", "Tags", "State", "Start Date",
        "Stakeholders", "SOX In-Scope", "So What?", "Secondary SVPs",
        "Secondary Owners", "Second Level Category", "Requirements", "PR/FAQ",
        "Project Type", "Risks", "Dependencies", "Priority", "Primary SVP",
        "Primary Benefits", "Parent Items (Related)", "Need By Date",
        "Modified By", "LT Members", "Internal ID", "Goal Origin ID",
        "Goal Origin", "Goal Measurements", "Followers", "First Level Category",
        "Finance Owners", "Draft", "Design Review State", "Created By",
        "Countries", "Contributors", "Child Items (Related)", "Attachments",
        "Additional Details", "Row Number", "ID", "Team", "Goal Set", "Title",
        "Status", "Orig Due Date", "Date", "Completion Date",
        "Status Comments", "Path to Green", "Modified", "Created", "Owners",
        "Description"
    ]
    
    try:
        df = pd.read_excel(filename)
        print(f'Number of columns in output: {len(df.columns)}')
        print('\nColumns present in output:')
        
        # Check if all required columns are present
        missing_columns = []
        for col in required_columns:
            if col in df.columns:
                print(f'✓ {col}')
            else:
                missing_columns.append(col)
                print(f'✗ {col} - MISSING')
        
        if missing_columns:
            print(f'\nERROR: Missing {len(missing_columns)} required columns!')
            return False
            
        # Verify Quarter column values
        if 'Quarter' in df.columns and 'Date' in df.columns:
            print('\nVerifying Quarter values:')
            for date, quarter in zip(df['Date'], df['Quarter']):
                if pd.notna(date) and date != "":
                    print(f'Date: {date} -> Quarter: {quarter}')
            
        # Verify pivot tables exist
        wb = pd.ExcelFile(filename)
        pivot_tables_ok = True
        
        # Check Goal Summary sheet
        if 'Goal Summary' in wb.sheet_names:
            print('\nGoal Summary sheet found!')
            goal_summary = pd.read_excel(filename, sheet_name='Goal Summary')
            if all(col in goal_summary.columns for col in ['Goal Set', 'Team']):
                print('✓ Goal Summary configuration verified')
            else:
                print('✗ Goal Summary missing required columns')
                pivot_tables_ok = False
        else:
            print('\nWARNING: Goal Summary sheet not found!')
            pivot_tables_ok = False
            
        # Check Count by Quarter sheet
        if 'Count by Quarter' in wb.sheet_names:
            print('\nCount by Quarter sheet found!')
            count_by_quarter = pd.read_excel(filename, sheet_name='Count by Quarter')
            if all(col in count_by_quarter.columns for col in ['Goal Set', 'Team', 'Status']):
                print('✓ Count by Quarter configuration verified')
            else:
                print('✗ Count by Quarter missing required columns')
                pivot_tables_ok = False
        else:
            print('\nWARNING: Count by Quarter sheet not found!')
            pivot_tables_ok = False
            
        if pivot_tables_ok:
            print('\nAll pivot tables created successfully!')
            
        print('\nSUCCESS: All required columns are present!')
        return True
            
    except Exception as e:
        print(f'Error reading Excel file: {str(e)}')
        return False

if __name__ == '__main__':
    verify_excel_output('test_output.xlsx')
