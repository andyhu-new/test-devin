import pandas as pd

def verify_goal_summary(filename):
    """Verify Goal Summary pivot table configuration."""
    print("=== Goal Summary Sheet Configuration ===")
    try:
        df = pd.read_excel(filename, sheet_name='Goal Summary')
        print("\nVerifying Goal Summary sheet:")
        print(f"✓ Sheet exists")
        
        # Verify structure
        required_index = {'Goal Set', 'Team'}
        required_status = {'Completed', 'In Progress', 'Not Started'}
        
        present_cols = set(df.columns)
        index_cols = required_index & present_cols
        status_cols = required_status & present_cols
        
        print("\nVerifying table structure:")
        print(f"✓ Index columns present: {index_cols}")
        print(f"✓ Status columns present: {status_cols}")
        print(f"✓ Total column present: {'Total' in present_cols}")
        
        # Verify data aggregation
        print("\nVerifying data aggregation:")
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        print(f"✓ Count columns (should be Status + Total): {list(numeric_cols)}")
        
        all_requirements_met = (
            len(index_cols) == len(required_index) and
            len(status_cols) > 0 and
            'Total' in present_cols
        )
        
        if all_requirements_met:
            print("\n✓ Goal Summary table meets all requirements!")
        else:
            print("\n✗ Goal Summary table is missing some requirements")
            
        print("\nFirst few rows of Goal Summary:")
        print(df.head())
        return all_requirements_met
    except Exception as e:
        print(f"✗ Error verifying Goal Summary: {e}")
        return False

def verify_count_by_quarter(filename):
    """Verify Count by Quarter pivot table configuration."""
    print("\n=== Count by Quarter Sheet Configuration ===")
    try:
        df = pd.read_excel(filename, sheet_name='Count by Quarter')
        print("\nVerifying Count by Quarter sheet:")
        print(f"✓ Sheet exists")
        
        # Verify required columns
        required_cols = {'Goal Set', 'Team', 'Status'}
        present_cols = set(df.columns)
        index_cols = required_cols & present_cols
        
        print("\nVerifying table structure:")
        print(f"✓ Index columns present: {index_cols}")
        
        # Verify quarter columns exist
        quarter_cols = [col for col in df.columns if col.startswith('Q')]
        print(f"✓ Quarter columns: {quarter_cols}")
        print(f"✓ Total column present: {'Total' in present_cols}")
        
        # Verify data aggregation
        print("\nVerifying data aggregation:")
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        print(f"✓ Count columns (should be Quarters + Total): {list(numeric_cols)}")
        
        # Verify row structure (Team, Status grouping)
        team_status_pairs = df.groupby(['Team', 'Status']).size()
        print("\nVerifying Team-Status grouping structure:")
        print(team_status_pairs.head())
        
        all_requirements_met = (
            len(index_cols) == len(required_cols) and
            len(quarter_cols) > 0 and
            'Total' in present_cols
        )
        
        if all_requirements_met:
            print("\n✓ Count by Quarter table meets all requirements!")
        else:
            print("\n✗ Count by Quarter table is missing some requirements")
            
        print("\nFirst few rows of Count by Quarter:")
        print(df.head())
        return all_requirements_met
    except Exception as e:
        print(f"✗ Error verifying Count by Quarter: {e}")
        return False

def main():
    filename = 'test_output.xlsx'
    success = True
    
    print(f"\nVerifying pivot tables in {filename}\n")
    
    if not verify_goal_summary(filename):
        success = False
    
    if not verify_count_by_quarter(filename):
        success = False
    
    if success:
        print("\n✓ All pivot table verifications passed successfully!")
    else:
        print("\n✗ Some verifications failed. Please check the output above.")

if __name__ == '__main__':
    main()
