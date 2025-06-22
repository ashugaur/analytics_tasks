# %% File search query

## Run
if __name__ == "__main__":
    ## Dependencies
    from analytics_tasks.utils import fakedatagenerator as fdg

    ## Project folder
    # at_dir = Path("C:/my_disk/____tmp/analytics_tasks") # Triggered dueing build

    generator = fdg.FakeDataGenerator()

    # Generate files with custom parameters
    generator.generate_all_files(
        xlsx_count=4,  # Number of Excel files (.xlsx)
        txt_count=3,  # Number of text files
        sql_count=2,  # Number of SQL files
        py_count=2,  # Number of Python files
        pptx_count=3,  # Number of PowerPoint files
        pdf_count=2,  # Number of PDF files
        max_rows=50,  # Maximum rows for Excel files
        max_lines=30,  # Maximum lines for text/SQL/Python files
        max_slides=8,  # Maximum slides for PowerPoint files
        max_pages=4,  # Maximum pages for PDF files
        output_dir=at_dir / "fake_data",  # Output directory
    )
