# Cert Checker

This project takes a list of domains in the `domains.txt` file, checks the public certs on those domains and prints a report to the screen and saves the output to a file named after the domain.


## Example output if code runs successfully:
| Expired date                          | Domain                                | Cert expires in               |
| Jan 30 08:19:31 2023 GMT              | www.google.com                | 47 days, and 13 hours         |

## TODO:
o Write all the domains to 1 file instead of individual ones.

o Format the text better.

o create a `--single` flag to pass only 1 domain for a quick lookup.
