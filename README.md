# Avaaz Engineering Exercise

Thanks for your interest in joining Avaaz! We're thrilled that you'd consider working with us. The next step in your interview process is to complete this exercise. The exercise should take no more than an hour to complete.

## Instructions

Your task is to build a solution that allows a user to search data using several filters:

- Date range (after, before, and between)
- Title (text search, case-insensitive, full or partial matches)
- URL (full or partial matches)

Using Flask, create a solution that:

- Ingests JSON source data (see the `input` folder)
- Stores valid data and normalized datetimes in the provided database
- Queries the data (using the filters described above)
- Outputs the results

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

Fork this repo and submit a pull request with your solution.
