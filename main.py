import os
import pygsheets
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Init Google Sheets
gc = pygsheets.authorize(service_file = os.getenv("CREDENTIALS_FILE"))
sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/" + os.getenv("EXAMPLE_GSHEET") + "/edit?usp=sharing")
wks = sh.worksheet_by_title("工作表1")

# Read cell A1 from the first sheet
print(wks.get_value("A1"))

# Read cell A1 background color
print(wks.cell("A1").color)

# Set cell A1 background color to pink
wks.cell("A1").color = (0.871, 0.361, 0.361)