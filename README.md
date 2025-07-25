# HKU Credit Transfer Database
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
[![GitHub Issues](https://img.shields.io/github/issues/aatmiyasilwal/HKU-Credit-Transfer-Database.svg)](https://github.com/aatmiyasilwal/HKU-Credit-Transfer-Database/issues)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

### Overview
---
This project is designed to streamline the process for outgoing exchange students from the University of Hong Kong (HKU) by providing a unified querying system for credit transfer data. Using Selenium, multiple scrapers have been developed to gather course-related information from various publicly available HKU resources. The data is then consolidated into a consistent format in CSV files, enabling students to easily access and query the information they need. Currently, the database contains equivalence information on 25,000+ courses from 150+ universities.

**Live Demo**: [HKU Credit Transfer Database](https://credit-transfer-database.netlify.app/)

### Getting Started
---
#### Prerequisites
To run this project, you will need:
* Python 3.x (currently using Python 3.12.8)
* Selenium
* PyPDF2
* Camelot
* Pandas
* time
* A compatible web driver (e.g., Safari, Chrome) — (I used Safari)

### Installation
---
1. Clone the repository:
   ```bash
   git clone https://github.com/aatmiyasilwal/HKU-Credit-Transfer-Database.git
   cd hku-credit-transfer-scraper
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the appropriate web driver installed and accessible in your system's PATH.

### Usage
---
1. Run the scrapers to collect data.
2. The scraped data will be saved in CSV format in the `backend/` directory, and eventually compiled in the `merged-credit_transfer_database.csv`.
3. To launch the website locally, use:
   ```bash
   python -m http.server <port number>
   ```

### New Updates
---
1. SEO implemented via submission and verification of the domain to Google Search Console.
2. Added up to date data for all faculties.

### Contribution
---
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

### License
---
This project is licensed under the MIT License. See the LICENSE file for more details.

### Contact
---
For any questions or feedback, please reach out to aatmiyas@connect.hku.hk.

### Disclaimer
---
This project is not an official HKU product, and it simply serves as a tool to assist students in their search for credit transfer information. The final decision regarding course equivalencies and credit transfers rests with the home faculty of the student. Always consult with your faculty for official guidance.