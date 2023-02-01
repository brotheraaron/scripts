import os
import csv
import ssl
import errno
import socket
import argparse
import webbrowser
import pandas as pd
from typing import Any, Dict
from datetime import datetime
from colorama import Fore, Back, Style
from os.path import exists as file_exists



CONNECTION_TIMEOUT = 5.0


class SSLConnectionFailed(Exception):
    pass


class UnknownSSLFailure(Exception):
    pass


class LookupFailed(Exception):
    pass


def print_f(original_stdout, file_name, idx) -> Any:
    time_stamp = int(datetime.now().timestamp())
    header_list = ["Date Cert Expires", "Domain", "Days Till Cert Expires"]
    HTMLBody = "<body bgcolor=black>"

    if not file_exists(file_name):
        with open(file_name, 'a', newline='') as f:
            header_list.insert(0,'Line:')
            original_stdout.insert(0,idx)
            f.write(HTMLBody)
            file_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(header_list)
            file_writer.writerow(original_stdout)

    else:
        with open(file_name, 'a+', newline='') as f:
            original_stdout.insert(0,idx)
            file_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(original_stdout)



def get_ssl_expiry(domain: str) -> Any:
# def get_cert_expiration_date(domain: str) -> Any
    try:
        # Creates a socket and will timeout after 5 seconds
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(CONNECTION_TIMEOUT)

        # Load the system’s trusted CA certificates, enable certificate validation and hostname checking, and try to choose reasonably secure protocol and cipher settings.
        context: ssl.SSLContext = ssl.create_default_context()

        # Wrap an existing Python socket sock and return an instance of SSLContext.sslsocket_class (default SSLSocket).
        # The returned SSL socket is tied to the context, its settings and certificates.
        ssl_sock: ssl.SSLSocket = context.wrap_socket(sock, server_hostname=domain)
        ssl_sock.settimeout(CONNECTION_TIMEOUT)
        
        # Creates socket connection to domain name on port 443
        ssl_sock.connect((domain, 443))

        # Get's the public cert from the remote host, on success getpeercert() returns a dictionary.
        cert_dict: Dict[str, Any] = ssl_sock.getpeercert()

        # Closes our socket and frees up the resource.
        ssl_sock.close()

        # Returns all the values associated with the key "notAfter"
        return cert_dict["notAfter"]
    except socket.gaierror:
        raise LookupFailed
    except socket.error as e:
        if e.errno == errno.ECONNREFUSED:
            # connection to port 443 was refused
            raise SSLConnectionFailed
        raise UnknownSSLFailure


def results():
    default_expire_dates_csv = "expire_dates.csv"
    default_html_file = "check_certs_results.html"

    if file_exists(default_expire_dates_csv):
        os.remove(default_expire_dates_csv) 

    # Initiate empty list
    domains = []

    # Default file name in current working directory:
    default_domains_file = "domains.txt"

    parser = argparse.ArgumentParser()

    # add the --file argument
    parser.add_argument("--file", help="The file to be processed", default=default_domains_file)

    # parse the arguments
    args = parser.parse_args()

    # get the name of the running program
    program_name = parser.prog

    # Tests if file passed to --file exists.
    # If yes, save the file name to the variable file_location.
    # This will also test if the default file exists.
    if file_exists(args.file):
        file_location = args.file
    # If no file name, or file name doesn't exist, or default file doesn't exist, throw this error:
    else:
        parser.error(f"{args.file} not found or doesn't exist.\
            \nPlease do one of the following:\
            \n1. Provide a file to be processed using the --file argument\
            \n2. Create a file named {default_domains_file} in the same directory as {program_name}")


    # Opens file domains.txt and reads it line by line
    with open(file_location) as f:
        for l in f.readlines():
            if l.strip() and not l.strip().startswith("#"):
                domain = l.strip()

                # Try to pass the domain read from domains.txt to get_ssl_expiry() and convert it to a string then append get_ssl_expiry's output to list domains.
                try:
                    domains.append((domain, str(get_ssl_expiry(domain))))
                # If try fails throw an error and appened the list with the thrown error.
                except Exception as e:
                    domains.append((domain, type(e).__name__))

    headings = ["Date Cert Expires", "Domain", "Days Till Cert Expires"]
    print("| {:^30} | {:^17} | {:^25} |".format(*headings))

    i = 0
    for domain, date_str in sorted(domains, key=lambda x: x[1]):
        i = i + 1
        # given date in the format "Mar 14 23:59:59 2023 GMT"
        # parse the given date using the datetime.strptime() method
        date = datetime.strptime(date_str, "%b %d %H:%M:%S %Y %Z")

        # get the current date and time using the datetime.now() method
        now = datetime.now()

        # calculate the difference between the given date and the current date and time using the datetime.timedelta() method
        diff = date - now

        # calculate the number of seconds in the difference
        seconds = diff.total_seconds()

        # divide the number of seconds by the number of seconds in a day, hour, and second using the divmod() function
        days, seconds = divmod(seconds, 24 * 60 * 60)
        hours, seconds = divmod(seconds, 60 * 60)

        # format the number of days, and hours
        cert_expires_in_days_hours = f"{int(days)} days, and {int(hours)} hours"

        headings = [date_str, domain, cert_expires_in_days_hours]
        print("| {:^30} | {:^17} | {:^25} |".format(*headings))
        
        send_to_csv = [date_str, domain, cert_expires_in_days_hours]
        print_f(send_to_csv, file_name=default_expire_dates_csv, idx=i)
        df = pd.read_csv(default_expire_dates_csv)

        th_props = [
            ('font-family', 'times new roman'),
            ('font-size', '32'),
            ('text-align', 'left'),
            ('font-weight', 'bold'),
            ('color', 'white'),
            ("width", "350"),
            ('background-color', "black")
        ]

        td_props = [
            ('font-size', '24px'),
            ("font-family" , 'Helvetica'),
            # ("margin" , "200"),
            # ("border-collapse" , "collapse"),
            # ("border" , "1px solid #eee"),
            # ("border-bottom" , "4px solid black"),
            ("border-top" , "4px solid white"),
            ('text-align', 'right'),
            ('background-color', "black"),
            ('color', 'white'),
        ]


        # Set table styles
        styles = [
            dict(selector="th", props=th_props),
            dict(selector="td", props=td_props),
        ]
        

        s=df.style.set_table_styles(styles).hide(axis="index").to_html(default_html_file)

    
    webbrowser.open('file://' + os.path.realpath(default_html_file))






if __name__ == "__main__":

    results()
