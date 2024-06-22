# Streamlit Survey Application

## Overview

The Streamlit Survey application is designed to create and manage surveys using Streamlit and Google Sheets. This app allows users to fill out surveys and view results directly within the Streamlit interface, leveraging Google Sheets for data storage and management.

## Features

Survey Creation and Submission: Users can take the survey directly from the app.
Results Display: View survey results in real-time.
Google Sheets Integration: Read and write survey data to a Google Sheet.
Streamlit Components: Utilizes Streamlit's interactive widgets and layout options.

## Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

## Requirements

- `Python` 3.8 or higher
- `streamlit`
- `gspread`
- `gspread-pandas`
- `gspread-dataframe`
- `gspread-formatting`
- `pandas`
- `duckdb`
- `sql-metadata`
- `validators`

## Usage

1. Clone the Repository:

```bash
git clone https://github.com/MehdiSlr/Streamlit-Survey.git
cd Streamlit-Survey
```

2. Create API Key in google cloud console and give access in your Google Sheet.

3. Create `secrets.toml` file in `.streamlit` directory in the root of the project based on the API Key json file you created in google cloud console.:

```toml
[secrets]

[connections.gsheets]
spreadsheet = "YOUR_SPREADSHEET_URL"
worksheet = "YOUR_WORKSHEET_GID"
type= "service_account"
project_id = "YOUR_PROJECT_ID"
private_key_id = "YOUR_PRIVATE_KEY_ID"
private_key = "YOUR_PRIVATE_KEY"
client_email = "YOUR_CLIENT_EMAIL"
client_id = "YOUR_CLIENT_ID"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/streamlit-gsheets%40api-class-423418.iam.gserviceaccount.com"
universe_domain = "googleapis.com"
```

4. Run the Application:

```bash
streamlit run main.py
```

## Main Scripts

- `main.py`: The entry point of the application. It includes the main layout and navigation buttons for taking the survey and viewing results.
- `Public_Sheet_Example.py`: Example script demonstrating how to connect to a public Google Sheet and read data using GSheetsConnection.

## Google Sheets Connection

In the `Public_Sheet_Example.py`, the connection to Google Sheets is established using a public URL:

```python
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/your_sheet_id/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(df)
```

## Survey Navigation

The main.py script uses Streamlit's button components to navigate between different pages:

```python
col1, col2 = st.columns(2)

with col1:
    if st.button("Take the Survey", use_container_width=True, type="primary"):
        st.switch_page("pages/Survey.py")

with col2:
    if st.button("See Survey Results", use_container_width=True):
        st.switch_page("pages/Result.py")
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Acknowledgements

- Using [Streamlit](https://streamlit.io) API, gspread, gspread-pandas, gspread-dataframe, gspread-formatting, pandas, duckdb, sql-metadata, and validators.
- Using [Google Sheets](https://docs.google.com/spreadsheets/) API.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

This project was created by [Mehdi Slr](https://github.com/MehdiSlr).