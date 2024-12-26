# Excel Processor

A Python script to process Excel files and create pivot tables.

## Features
- Processes Excel files with required columns
- Creates two pivot tables in separate sheets:
  1. Goal Summary:
     - Filters: Goal Set
     - Rows: Team
     - Columns: Status
     - Values: Count of ID
  2. Count by Quarter:
     - Filters: Goal Set
     - Rows: Team, Status
     - Columns: Quarter
     - Values: Count of ID
- Supports filtering and data aggregation
