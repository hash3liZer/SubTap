import sys
import os
import re
import argparse

class ENUMERATION:

    def __init__(self, prs):
        self.domain = prs.domain
        self.collect_subdomain = prs.c_subdomains
        self.skip_wordlists    = prs.sk_wordlist
        self.custom_wordlists  = prs.custom_wordlists

    def engage(self):
        return

class PARSER:

    def __init__(self, prs):
        self.domain = self.vald_domain(prs.domain)
        self.collect_subdomain = prs.c_subdomains
        self.skip_wordlists    = prs.sk_wordlist
        self.custom_wordlists  = self.vald_custom_wordlists(prs.cust_wordlist)

    def vald_domain(self, _value):
        ### Check if domain is provided or not. Domain is required
        ### WORK HERE ###
        return _value

    # --custom-wordlists "C:\\wordlists.txt,D:\\wordlist2.txt"
    def cust_wordlist(self, _value):
        # string method split()
        # os.path.isfile
        return _value

def main():
    parser = argparse.ArgumentParser()

    # Add arguments here
    parser.add_argument('-d', '--domain', dest="domain", type=str, default="", help="Top level domain to target")
    parser.add_argument('--collect-subdomains', dest="c_subdomains", default=False, action="store_true", help="Will store subdomain locally in a file for next enumeration")
    parser.add_argument('--skip-wordlist', dest="sk_wordlist", default=False, action="store_true", help="Will skip the wordlist on demand.")
    parser.add_argument('--custom-wordlists', dest="cust_wordlist", type=str, default="", help="Custom wordlists provided by user")

    parser = parser.parse_args()
    parser = PARSER(parser)

    ## STEP 1
    enum   = ENUMERATION(parser)
    enum.engage()

if __name__ == "__main__":
    main()
