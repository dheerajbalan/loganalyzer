LogAnalyzer

LogAnalyzer is a Python 3 tool designed to analyze web server log files. It extracts valuable insights such as the most requested pages, the IP addresses with the highest number of requests, and the total number of 404 errors.
Features

    Parses web server log files to extract key information.
    Counts requests per IP address.
    Identifies the most requested pages.
    Counts the total number of 404 errors.
    Generates a summary report.

Requirements

    Python 3.6+

Installation

    Clone the repository:

    bash

    git clone https://github.com/yourusername/LogAnalyzer.git
    cd LogAnalyzer

    Install any necessary dependencies (if applicable). In this case, no additional dependencies are required other than Python itself.

Usage

To run the LogAnalyzer tool, use the following command:

bash

python log_analyzer.py -lf <logfile>

Example

Analyze a log file:

bash

python log_analyzer.py -lf logs/access.log

Sample Output

makefile

======RESULTS:logs/access.log====== 

Total number of 404 errors: 15

Top 10 requested pages:
/index.html: 120 requests
/contact.html: 95 requests
/about.html: 90 requests

Top 10 IP addresses with most requests:
192.168.1.1: 50 requests
192.168.1.2: 45 requests
192.168.1.3: 40 requests

Contact

For any inquiries or issues, please contact dheerajbalan7@gmail.com.
