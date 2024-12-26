import pandas as pd
from datetime import datetime, timedelta
import sys

def get_status_order():
    """Return the ordered list of status values."""
    return ['Completed', 'Completed Late', 'DNM', 'Cancelled', 'Red', 'Yellow', 'Green', 'New']

def is_standard_status(status):
    """Check if the status is one of the standard statuses."""
    return status in ['Completed', 'Completed Late', 'DNM', 'Cancelled', 'Red', 'Yellow', 'Green']

def is_within_past_weeks(date_str, weeks=3):
    """Check if the given date is within the specified number of weeks from now."""
    if pd.isna(date_str):
        return False
    try:
        date = pd.to_datetime(date_str)
        weeks_ago = datetime.now() - timedelta(weeks=weeks)
        return date >= weeks_ago
    except:
        return False

def should_include_item(row):
    """Determine if an item should be included based on status and date criteria."""
    status = row['Status']
    
    # For Red and Yellow items, always include
    if status in ['Red', 'Yellow']:
        return True
    
    # For Completed, Completed Late, DNM, Cancelled - check Modified date
    if status in ['Completed', 'Completed Late', 'DNM', 'Cancelled']:
        return is_within_past_weeks(row['Modified'])
    
    # For Green items - check Created date
    if status == 'Green':
        return is_within_past_weeks(row['Created'])
    
    # For non-standard statuses - check Created date
    if not is_standard_status(status):
        return is_within_past_weeks(row['Created'])
    
    return False

def format_item(row):
    """Format a single item according to the specified markdown template."""
    markdown = []
    
    # Header line with clickable ID link and bold formatting
    header = f"__ [{row['Status']}] {row['Goal Set']} Goal [{row['ID']}](https://kingpin.amazon.com/#/items/{row['ID']}) \"{row['Title']}\" on {row['Date']}__"
    markdown.append(header)
    
    # Description
    markdown.append(f"{row['Description']}")
    
    # Status Comments
    if pd.notna(row['Status Comments']):
        markdown.append(f"**Status Comments - **{row['Status Comments']}")
    
    # Path to Green (only if not null)
    if pd.notna(row['Path to Green']):
        markdown.append(f"**Path to Green - **{row['Path to Green']}")
    
    # Modified By and Modified date
    if pd.notna(row['Modified By']) and pd.notna(row['Modified']):
        markdown.append(f"**Status Modified By - **{row['Modified By']} at {row['Modified']}")
    
    # Original Due Date
    if pd.notna(row['Orig Due Date']):
        markdown.append(f"**Original Due Date - **{row['Orig Due Date']}")
    
    # Owners
    if pd.notna(row['Owners']):
        markdown.append(f"**Owner(s) - **{row['Owners']}")
    
    # Add empty line after item
    markdown.append("")
    
    return "\n".join(markdown)

def generate_markdown(input_file, output_file):
    """Generate markdown file from Excel data."""
    try:
        # Read Excel file
        df = pd.read_excel(input_file)
        
        # Filter for LT Goal Set
        df = df[df['Goal Set'] == 'LT']
        
        # Initialize markdown content
        markdown_content = []
        
        # Process each status group in specified order
        for status in get_status_order():
            if status == 'New':
                # Group all non-standard statuses
                status_group = df[~df['Status'].apply(is_standard_status)]
            else:
                status_group = df[df['Status'] == status]
            
            # Filter items based on criteria
            status_group = status_group[status_group.apply(should_include_item, axis=1)]
            
            if len(status_group) > 0:
                # Add group header
                display_status = status if status != 'New' else 'New'
                markdown_content.append(f"### {display_status} ({len(status_group)} goals)\n")
                
                # Add items
                for _, row in status_group.iterrows():
                    markdown_content.append(format_item(row))
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(markdown_content))
        
        print(f"Successfully generated markdown file: {output_file}")
        
    except Exception as e:
        print(f"Error generating markdown: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_markdown.py <input_excel_file> <output_markdown_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    generate_markdown(input_file, output_file)
