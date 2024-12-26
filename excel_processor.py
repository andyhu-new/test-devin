import pandas as pd
import sys
from typing import List
from datetime import datetime
from openpyxl import load_workbook

def get_quarter_str(date_str: str) -> str:
    """Convert date to quarter string with year suffix if not current year."""
    if pd.isna(date_str) or date_str == "":
        return ""
    
    try:
        date = pd.to_datetime(date_str)
        quarter = (date.month - 1) // 3 + 1
        current_year = datetime.now().year
        
        if date.year == current_year:
            return f"Q{quarter}"
        else:
            year_suffix = str(date.year)[-2:]  # Get last 2 digits of year
            return f"Q{quarter}'{year_suffix}"
    except:
        return ""

def ensure_columns(df: pd.DataFrame, required_columns: List[str]) -> pd.DataFrame:
    """Ensure all required columns exist in the DataFrame."""
    # First ensure all required columns exist
    for column in required_columns:
        if column not in df.columns:
            df[column] = ""  # Add empty column if it doesn't exist
    
    # Add Quarter column based on Date column
    df['Quarter'] = df['Date'].apply(get_quarter_str)
    
    # Add Quarter to required columns if not already present
    if 'Quarter' not in required_columns:
        required_columns = required_columns + ['Quarter']
    
    return df[required_columns]  # Reorder columns to match required order

def create_pivot_tables(df: pd.DataFrame, output_file: str) -> None:
    """Create pivot tables in separate sheets for data analysis using pandas."""
    # Create Goal Summary pivot table
    goal_summary = pd.pivot_table(
        df,
        values='ID',
        index=['Team'],
        columns='Status',
        aggfunc='count',
        fill_value=0,
        margins=True,
        margins_name='Total'
    ).reset_index()
    
    # Add Goal Set column for filtering
    unique_goal_sets = df['Goal Set'].unique()
    goal_summary.insert(0, 'Goal Set', '')  # Add empty Goal Set column for filtering
    
    # Create Count by Quarter pivot table
    count_by_quarter = pd.pivot_table(
        df,
        values='ID',
        index=['Team', 'Status'],
        columns='Quarter',
        aggfunc='count',
        fill_value=0,
        margins=True,
        margins_name='Total'
    ).reset_index()
    
    # Add Goal Set column for filtering
    count_by_quarter.insert(0, 'Goal Set', '')  # Add empty Goal Set column for filtering
    
    # Write data and pivot tables to Excel file
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # Write original data
        df.to_excel(writer, sheet_name='Data', index=False)
        
        # Write Goal Summary pivot table
        goal_summary.to_excel(writer, sheet_name='Goal Summary', index=False)
        
        # Write Count by Quarter pivot table
        count_by_quarter.to_excel(writer, sheet_name='Count by Quarter', index=False)
        
        # Get workbook to apply filters
        workbook = writer.book
        
        # Configure Goal Summary sheet with filters
        goal_summary_sheet = workbook['Goal Summary']
        goal_summary_sheet.auto_filter.ref = goal_summary_sheet.dimensions
        
        # Configure Count by Quarter sheet with filters
        count_by_quarter_sheet = workbook['Count by Quarter']
        count_by_quarter_sheet.auto_filter.ref = count_by_quarter_sheet.dimensions

def process_excel(input_file: str, output_file: str) -> None:
    """Process the Excel file and ensure it has all required columns."""
    # Define required columns
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
        # Read the input Excel file
        df = pd.read_excel(input_file)
        
        # Ensure all required columns exist and are in the correct order
        df = ensure_columns(df, required_columns)
        
        # Create pivot tables and write to output file
        create_pivot_tables(df, output_file)
        
        print(f"Successfully processed Excel file and created pivot tables. Output saved to: {output_file}")
        
    except Exception as e:
        print(f"Error processing Excel file: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python excel_processor.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_excel(input_file, output_file)
