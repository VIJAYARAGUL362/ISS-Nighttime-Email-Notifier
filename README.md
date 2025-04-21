# ISS Nighttime Email Notifier

A Python script that tracks the International Space Station (ISS) and sends an email notification when it's overhead your location during nighttime hours. This project was developed as part of Dr. Angela Yu's "100 Days of Code - The Complete Python Pro Bootcamp" on Udemy (specifically the project for Day XX - *replace XX with the actual day number*).

## Project Description

This script continuously monitors the current position of the International Space Station using the Open Notify API. Simultaneously, it checks if it is currently nighttime at a predefined location using the Sunrise-Sunset API. If the ISS is within a close proximity (approx. +/- 5 degrees latitude and longitude) of your location AND it is dark outside, the script sends an automated email alert.

The goal is to notify you of potential ISS visibility opportunities when you are most likely to be able to see it in the night sky.

## Features

* Automated ISS position tracking via API.
* Checks for local nighttime conditions via API.
* Sends email notification when both conditions are met (ISS near + nighttime).
* Runs continuously, checking periodically (every 60 seconds).

## Requirements

* Python 3.x
* `requests` library (`pip install requests`)
* A Gmail account (or another email account with SMTP access) from which to send the email.
* An App Password for your Gmail account (if you use 2-Factor Authentication) or 'Less secure app access' enabled (less recommended). **Storing your main password directly in the code is insecure.**

## Setup and Configuration

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2.  **Set up a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    # .\venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install requests
    ```

4.  **Configure Script Variables:**
    Open the script file (`main.py` or whatever you named it) and update the following variables:

    * `MY_LAT`: Your location's latitude (e.g., `20.593683` for Kumbakonam).
    * `MY_LONG`: Your location's longitude (e.g., `78.962883` for Kumbakonam).
    * `MY_EMAIL`: The email address you want to send the notifications *from* (and likely *to*).
    * `PASSWORD`: **DO NOT put your actual email password here directly.**
        * **Recommended Secure Method:** Use environment variables. Replace the line with something like:
            ```python
            import os
            PASSWORD = os.environ.get("EMAIL_PASSWORD")
            ```
            You will then need to set an environment variable named `EMAIL_PASSWORD` with your app password or account password before running the script. How to set environment variables depends on your operating system (e.g., `export EMAIL_PASSWORD="your_password"` in bash, or set via system settings).
        * **Less Secure (for testing only, AVOID committing):** If you absolutely must for a quick test, temporarily put your password here, but **make sure this line is removed or commented out before committing and pushing to GitHub.**

    * `body_text`: Customize the content of the notification email.

## How to Run

1.  Ensure you have completed the Setup and Configuration steps.
2.  If using a virtual environment, activate it (`source venv/bin/activate`).
3.  Run the Python script from your terminal:
    ```bash
    python main.py
    ```
4.  The script will run continuously, printing status messages to the console and sending an email when the ISS is overhead during nighttime.

## Notes

* The script checks the ISS position and nighttime status approximately every 60 seconds.
* For continuous operation, you may want to run this script in the background on a server or computer that is always on (e.g., using `nohup` on Linux, `screen`, or a task scheduler).
* Ensure your email account allows sending emails programmatically (you may need to enable "Less secure app access" in Google account settings or use an App Password if you have 2-Factor Authentication enabled - **App Passwords are much more secure than enabling "Less secure app access"**).

## Project Source / Acknowledgement

This project was developed as a practice exercise from:

* **Course:** 100 Days of Code - The Complete Python Pro Bootcamp
* **Instructor:** Dr. Angela Yu
* **Platform:** Udemy
* *https://www.udemy.com/share/103IHM3@VCUlHom1rbmOCPaah5h3KIbBPWgOodWOz0hHPVvD1CXNz8goyDgnxm_H56WJpQ9Oig==/*

This project helped reinforce concepts related to working with APIs, `datetime`, `smtplib`, and building automated scripts.
