# pandabuy legit check
![](images/gui.png)

Legit Check is a simple program for searching data in text files, JSON files, and VCF files. It allows the user to select a file, specify search criteria, and then search through the chosen files for matching data.

## How to Use the Program

### 1. Select TXT File

- Click the "Select TXT File" button to choose the text file you want to search.
- After selecting the file, its path will be displayed below the button.

### 2. Choose Search Criteria

- Choose one of the available search criteria from the "Search Options" dropdown menu:
  - **Phone Number**: Search by phone number.
  - **Name and Surname**: Search by name and surname.
  - **JSON File**: Search information in a JSON file.
  - **VCF File**: Search information in a VCF file.

### 3. Enter Search Data

- Depending on the chosen criteria, enter the appropriate search data:
  - For **Phone Number** or **Name and Surname**: Enter the phone number or name and surname in the text field.
  - For **JSON File** or **VCF File**: Leave the text field empty.

### 4. Submit Search

- After entering the search data, click the "Submit" button to start the search.

### 5. Displaying Results

- After the search is complete, the results will be displayed in a new window.
- If no matching records are found, a message indicating no results will be displayed.

## System Requirements

- Python 3.x
- Tkinter (installed with Python)

## Running the Program

1. Download the repository with the source code of the Legit Check application.
2. Run the program by executing the `LegitCheckApp.py` file in the terminal or Python environment.

```bash
python LegitCheckApp.py
