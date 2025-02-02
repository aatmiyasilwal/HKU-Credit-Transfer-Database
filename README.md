# HKU Credit Transfer Database

### Overview
---
<p>
This project is designed to streamline the process for outgoing exchange students from the University of Hong Kong (HKU) by providing a unified querying system for credit transfer data. Using Selenium, multiple scrapers have been developed to gather course-related information from various publicly available HKU resources. The data is then consolidated into a consistent format in CSV files, enabling students to easily access and query the information they need.
</p>


### Getting Started
---
Prerequisites
To run this project, you will need:

* Python 3.x (I currently use Python 3.12.8)
* Selenium
* PyPDF2
* Camelot
* Pandas
* time
* A compatible web driver (e.g., Safari, Chrome) -- (I used Safari)

### Installation
---
* Clone the repository:
`git clone https://github.com/yourusername/hku-credit-transfer-scraper.git`
`cd hku-credit-transfer-scraper`

* Install the required dependencies:

`pip install -r requirements.txt`

* Ensure you have the appropriate web driver installed and accessible in your system's PATH.

### Usage
---
1. Run the scrapers to collect data.
2. The scraped data will be saved in CSV format in the data/ directory.

### Future-To-Dos
---
1. Develop the querying system that allows students to search through the compiled data.

### Contribution
---
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

### License
---
This project is licensed under the MIT License. See the LICENSE file for more details.

### Contact
---
For any questions or feedback, please reach out to aatmiyas@connect.hku.hk.

# Disclaimer
This project serves as a tool to assist students in their search for credit transfer information. The final decision regarding course equivalencies and credit transfers rests with the home faculty of the student. Always consult with your faculty for official guidance.
