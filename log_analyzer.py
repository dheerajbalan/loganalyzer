import re
from collections import defaultdict
import argparse


def get_arguments():
    parse = argparse.ArgumentParser()
    parse.add_argument("-lf", "--log-file", dest="logfile", help="Enter your log file path")
    return parse.parse_args()


def parse_log_line(line):
    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] "(?P<request>.*?)" (?P<status>\d{3}) (?P<size>\d+|-) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"'
    )
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return None


def analyze_logs(log_file):
    requests_per_ip = defaultdict(int)
    requested_pages = defaultdict(int)
    error_404_count = 0

    with open(log_file, 'r') as f:
        for line in f:
            if not line.strip():
                continue  # Skip empty lines
            log_entry = parse_log_line(line)
            if log_entry:
                ip = log_entry['ip']
                status = log_entry['status']
                request = log_entry['request']
                url = request.split()[1]

                requests_per_ip[ip] += 1
                requested_pages[url] += 1
                if status == '404':
                    error_404_count += 1
            else:
                print(f"Warning: Line did not match pattern: {line.strip()}")

    return requests_per_ip, requested_pages, error_404_count


def generate_report(log_file):
    requests_per_ip, requested_pages, error_404_count = analyze_logs(log_file)

    report = []
    report.append(f"Total number of 404 errors: {error_404_count}")
    report.append("\nTop 10 requested pages:")
    for page, count in sorted(requested_pages.items(), key=lambda x: x[1], reverse=True)[:10]:
        report.append(f"{page}: {count} requests")

    report.append("\nTop 10 IP addresses with most requests:")
    for ip, count in sorted(requests_per_ip.items(), key=lambda x: x[1], reverse=True)[:10]:
        report.append(f"{ip}: {count} requests")

    return "\n".join(report)


if __name__ == "__main__":
    args = get_arguments()
    log_file = args.logfile
    report = generate_report(log_file)
    print("\n")
    print(f"======RESULTS:{log_file}====== \n")
    print(report)
