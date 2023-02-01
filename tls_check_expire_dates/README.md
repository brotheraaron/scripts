# Cert Checker

This project takes a list of domains in the `domains.txt` file, checks the public certs on those domains and prints a report to the screen and saves the output to a file named after the domain.


## Example output if code runs successfully:
| Expired date                          | Domain                                | Cert expires in               | <br />
| Jan 30 08:19:31 2023 GMT              | www.google.com                | 47 days, and 13 hours         |

## TODO:
o create a `--single` flag to pass only 1 domain for a quick lookup. 
