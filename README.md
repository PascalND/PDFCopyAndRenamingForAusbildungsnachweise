# PDF Copy and Renaming for Training Records 📚

> Automate the organization of your IHK training records by creating weekly PDF copies with proper dates and calendar week numbers

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://choosealicense.com/licenses/apache-2.0/)

## 🎯 Overview

This Python script automates the process of creating weekly training record PDFs for IHK apprenticeships. It takes a template PDF and creates copies for each week, automatically updating dates and calendar week numbers in both the filename and the PDF form fields.

## 📑 Table of Contents

- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **Automated PDF Processing:** Creates copies of a template PDF for each week
- **Smart Date Management:** Automatically calculates correct date ranges for each week
- **Calendar Week Integration:** Includes calendar week numbers in filenames
- **PDF Form Field Updates:** Automatically updates dates within the PDF form fields
- **Batch Processing:** Processes entire months or year at once
- **Work Week Focus:** Creates records for Monday through Friday only

## 🔧 Requirements

- Python 3.x
- PyPDF2 library
- Template PDF file for training records

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/PascalND/PDFCopyAndRenamingForAusbildungsnachweise.git
   cd PDFCopyAndRenamingForAusbildungsnachweise
   ```

2. **Install required library**
   ```bash
   pip install PyPDF2
   ```

## 📖 Usage Guide

### Configuration

1. **Set up directories in the script:**
   ```python
   source_folder = r"Source/Directory"      # Directory containing the template PDF
   destination_folder = r"Destination/Directory"  # Directory for the generated PDFs
   ```

2. **Prepare your template:**
   - Place a single PDF template in the source folder
   - Ensure the PDF has form fields named:
     - "Ausbildungswoche vom" (Training week from)
     - "bis" (until)
     - "Ausbildungsjahr" (Training year)

### Running the Script

1. **Configure the date range:**
   - Adjust the year and months in the script as needed:
   ```python
   # Set the year and date format in these lines:
   start_of_week = datetime.strptime(f'01.{start_month}.2024', '%d.%m.%Y')  # Change 2024 to desired year
   end_date = datetime.strptime(f'31.{end_month}.2024', '%d.%m.%Y')        # Change 2024 to desired year
   
   # At the bottom of the script, adjust the months (1-12) as needed:
   copy_and_rename_pdfs(1, 12)  # Processes January through December
   ```

2. **Example Configurations:**
   ```python
   # For full year 2024:
   start_of_week = datetime.strptime(f'01.{start_month}.2024', '%d.%m.%Y')
   end_date = datetime.strptime(f'31.{end_month}.2024', '%d.%m.%Y')
   copy_and_rename_pdfs(1, 12)

   # For first quarter 2025:
   start_of_week = datetime.strptime(f'01.{start_month}.2025', '%d.%m.%Y')
   end_date = datetime.strptime(f'31.{end_month}.2025', '%d.%m.%Y')
   copy_and_rename_pdfs(1, 3)
   ```

3. **Execute the script**
   - Run the script from your IDE or command line

### Output Format

The script generates PDFs with the following naming pattern:
```
KW[week-number] DD.MM.YYYY - DD.MM.YYYY.pdf
```
Example: `KW01 01.01.2024 - 05.01.2024.pdf`

### Example Directory Structure

```bash
Project/
├── Source/
│   └── template.pdf
└── Destination/
    ├── KW01 01.01.2024 - 05.01.2024.pdf
    ├── KW02 08.01.2024 - 12.01.2024.pdf
    └── ...
```

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

*Made with ❤️ by PascalND*
