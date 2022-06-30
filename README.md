# Avaaz Engineering Exercise

Thanks for your interest in joining Avaaz! We are thrilled that you considered working with us.

Your task is to build a small application that allows a user to search data using several filters:
- Date range (after, before, and between)
- Title (text search, case-insensitive, full or partial matches)
- URL (full or partial matches)

The following things are provided in this repository:
- The destination database table (see `database/initdb.d/setup.sql`)
- A bare bones Flask app (see `app/server.py`)

**We recommend you spend a maximum of two hours on it, and don't worry if you didn’t cover all of the requirements.**

## Instructions

- Use Python and Flask for your application
- The application ingests JSON source data (see the input folder)
- The application stores valid data and normalized datetimes in the provided database
- The application allows searching the data through an API endpoint (using the filters described above)

Submit your solution by sending a zipped file via email to your Avaaz recruiting contact (you can reply to your existing email thread).
