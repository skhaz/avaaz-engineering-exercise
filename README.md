# Avaaz Engineering Exercise

Thanks for your interest in joining Avaaz! We're thrilled that you'd consider working with us. The next step in your interview process is to complete this exercise. You should spend approximately one hour on this - don't worry if you don't complete every requirement.

## Instructions

Your task is to build a solution that allows a user to search data using several filters:

- Date range (after, before, and between)
- Title (text search, case-insensitive, full or partial matches)
- URL (full or partial matches)

Using Flask, create a solution that:

- Ingests JSON source data (see the `input` folder)
- Stores valid data and normalized datetimes in the provided database
- Allows searching the data through an API endpoint (using the filters described above)

Note that we've provided the following:

- The destination database table (see `database/initdb.d/setup.sql`)
- A bare bones Flask app (see `app/server.py`)

## Evaluation criteria

When reviewing your solution, we will test to see if it:

- Can be run by our engineers using Docker
- Solves the challenges laid out in the instructions
- Normalizes the source data, accounting for any variations or bad data
- Validates user inputs, accounting for security and accuracy
- Contains an updated README with instructions for using the solution

### Submitting

To submit your solution, either create a pull request or send a zipped file via email to your Avaaz recruiting contact (you can reply to your existing email thread).
