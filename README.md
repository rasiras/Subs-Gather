# Subs-Gather

A simple Python script for finding subdomains of a given domain.

Usage
```

python subs.py <domain> [--save]
```

Parameters
<domain>: The domain to find subdomains of.
--save: Optional flag to save the subdomains to a file.

**Examples**

```
python subs.py example.com
```
This command will print the subdomains of example.com to the console.

```
python subs.py example.com --save
```
This command will save the subdomains of example.com to a file called "subdomains.txt" in the current directory.

**Dependencies**

- Amass
- Assetfinder
- Subfinder

Note
-This is a simple implementation for educational purposes and for limited usage, it can also be used as a part of bug bounty or penetration testing
-Using this script with malicious intent is strictly prohibited, Use this tool only for educational and legal purposes.

Author
Rasi
