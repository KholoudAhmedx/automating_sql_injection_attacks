# SQL Injection Automation Scripts for PortSwigger Labs
This repository contains Python scripts to automate SQL injection attacks on PortSwigger SQLi Labs. The scripts leverage SQL injection techniques to test and extract data by exploiting vulnerabilities in sample applications provided by PortSwigger.
These labs are designed for educational purposes to improve skills in detecting and exploiting SQL injection vulnerabilities.

# Table of Contents
- Features
- Prerequisites
- Setup
- Usage
- References
- Notes

# Features
- Automates SQL injection attacks on PortSwigger's labs
- Supports common SQLi techniques, including:
  - Blind SQL injection
  - Error-based SQL injection
  - Boolean-based SQL injection
  - Customizable payloads for different lab challenges
  - Output of extracted data in a readable format

# Prerequisites
- **Python 3.7+**: Ensure you have Python 3 installed on your machine.
- **Requests Library**: The scripts use the requests library for HTTP interactions. You can install it with:
  ```
  pip install requests
  ```
- Access to **PortSwigger SQLi Labs**: A valid account and access to PortSwigger Labs is necessary to run the scripts effectively. Make sure you have a valid URL for the SQLi challenges you want to attack.
# Setup
1. Clone the repository
```
git clone https://github.com/yourusername/port_swigger_sqli_automation.git
cd port_swigger_sqli_automation
```
2. Configure Lab Details: </br>
Open the main script file (e.g., `sqli_automation.py`). </br>
Specify the target URL and lab-specific parameters, such as the vulnerable endpoint or any required cookies (e.g., session tokens) for authentication.

# Usage
To start using the scripts, follow these steps:

1. Run the Main Script: </br>

```
python3 <script_name.py> <url>
```
**For Example**
```
python3 sqli_lab_12.py "https://0ac9008403d9975e808c67630012004b.web-security-academy.net/"
```
2. Specify Target and Payloads:</br>
Modify the target URL directly through command-line arguments.
The script will send SQL injection payloads and analyze responses to determine if the injection was successful.
3. Monitor Output: </br>
The script outputs results directly to the terminal. For example, it might display whether each payload was successful and any extracted data.

# References
- **Web Security Academy - SQL Injection (Long Version) By Rana Khalil**</br>
  - <a href="https://www.youtube.com/watch?v=1nJgupaUPEQ&list=PLuyTk2_mYISLaZC4fVqDuW_hOk0dd5rlf">Web Security Academy - SQL Injection (Long Version) By Rana Khalil</a> on YouTube offers an in-depth, long-form series on SQL injection attacks.</br>
  Her tutorials provided detailed explanations and practical demonstrations that were essential in helping build and refine these automation scripts.

# Notes
- Lab Naming Convention</br>
  Each script in this repository is named according to the corresponding lab number from PortSwigger’s SQL Injection labs. For instance, `sql_lab_12.py` refers to Lab #12 in the PortSwigger SQL Injection section. This naming convention helps to identify and match the script with the specific lab it automates.

- PortSwigger Lab Reference</br>
  You can find the full list of PortSwigger SQL Injection labs and their order <a href="https://portswigger.net/web-security/all-labs#sql-injection">here</a>.
