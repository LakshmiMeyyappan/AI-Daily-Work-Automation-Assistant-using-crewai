AI Daily Work Assistant Automation Project

Overview
********

This project is an AI-powered daily work assistant that automatically analyzes a user’s daily development activity and generates:

A human-readable end-of-day work summary

Suggested tasks for the next working session

A saved daily report file

Optional voice output for task guidance

The system uses an agent-based AI workflow and works locally using Python.

Features
********

Automatically analyzes daily coding activity

Generates end-of-day work reports

Suggests next-day tasks

Supports personalized reports per user

Runs locally using a batch file

No code changes required for new users

System Requirements
********************

Windows OS

Python 3.11 (required)

Internet connection (for LLM calls)

Python Version

This project is tested and supported only with:

Python 3.11.x

Do not use Python 3.12, 3.13, or 3.14.

Setup Instructions
******************

Step 1: Create and Activate Virtual Environment

Open PowerShell in the project folder and run:

py -3.11 -m venv automation_env
automation_env\Scripts\activate

Step 2: Install Required Libraries

Run the following command after activating the virtual environment:

pip install crewai groq pyttsx3 openai>=1.83.0,<1.90.0 litellm<1.60.0 python-dotenv requests

Step 3: Update Configuration Files (Required)

Before running the project, you must edit the following files:

groq_apikey.txt

Open the file and replace the placeholder text with your own Groq API key:

YOUR_GROQ_API_KEY_HERE

git_username.txt

Open the file and replace the placeholder text with your own GitHub username:

YOUR_GITHUB_USERNAME_HERE


Save both files after editing.

These files are user-specific and must be updated by each person running the project.

Running the Project
********************

Option 1: Using Batch File (Recommended)

Double-click the following file:

run_app.bat


This will:

Activate the virtual environment

Run the AI assistant automatically

Generate a daily report

Option 2: Using Command Line

After activating the virtual environment, run:

python main.py

Output
******

Daily reports are saved inside the reports folder

Each report is generated based on the user’s own activity

The output is personalized for the user whose API key and GitHub username are provided

Important Notes
****************

Do not upload real API keys to public repositories

Each user must use their own Groq API key and GitHub username

The collectors folder is not required to be uploaded

No code changes are needed to run this project

Known Information
*****************

You may see LiteLLM warning logs related to optional proxy features.
These warnings do not affect the final output or report generation and can be safely ignored.

Project Usage

This project is intended for:

Personal productivity tracking

Mentor or evaluator demonstration

AI agent workflow learning

Automation project portfolios

Author

Lakshmi Meyyappan