# EWB Phishing URL Awareness Checker

## 1. Introduction

Nowadays, we use website links for online shopping, banking, social media, college work, and many other activities. However, not every link shared through a message, email, or website is trustworthy. Some links may be created to trick users into visiting fake websites and sharing personal information.

Phishing is a common online threat where attackers try to deceive people into revealing sensitive information, such as login credentials or financial details. Sometimes, a suspicious link may look similar to a genuine website, making it difficult for a user to identify the risk just by looking at it.

The **EWB Phishing URL Awareness Checker** is a small Python project developed to help users learn about some warning signs that can appear in suspicious URLs. The program takes a URL as input, examines its text, and displays any selected warning signs it finds.

This project is intended for learning and awareness. It does not claim to detect every phishing link or guarantee that a website is safe.

## 2. Project Objectives

The main objectives of this project are:

- To understand how URLs are structured and parsed in Python.
- To identify selected warning signs that may appear in suspicious links.
- To provide a simple command-line interface for checking URLs.
- To display clear messages that help users understand the findings.
- To practise Python concepts such as functions, loops, conditional statements, exception handling, and regular expressions.
- To encourage users to think carefully before opening unexpected links.

## 3. Project Overview

The program accepts a URL from the user and checks it against a set of predefined conditions. If one or more warning signs are found, the program displays them individually and provides a summary of the number of warnings.

The user can inspect multiple URLs during one session. When the user types `quit`, the program exits.

One important point is that the program only examines the text entered by the user. It does not open the website, send a request to the internet, or download any website content.

## 4. Warning Signs Checked by the Program

The checker looks for six selected warning signs.

### 4.1 Presence of an `@` Symbol

The `@` symbol can sometimes be used in a URL in a way that makes the address confusing. For example, a URL containing `example.com@sample.invalid` may mislead a person who does not carefully check the actual hostname.

The checker reports the presence of this symbol so the user can inspect the address more carefully.

### 4.2 Unusually Long URL

Some URLs contain many characters, parameters, or nested-looking text. A long URL is not automatically malicious, but it can be harder to read and understand.

In this project, a URL longer than 100 characters triggers a warning.

### 4.3 IP Address as the Hostname

Websites commonly use domain names, although some legitimate services can also be accessed through IP addresses. A link that uses an IP address instead of a familiar domain may deserve additional attention.

The checker looks for a hostname formatted like an IPv4 address.

### 4.4 Many Hostname Segments

A hostname containing several segments or subdomains can sometimes make a URL look more complicated or confusing.

This program reports a warning when the hostname contains five or more segments. This is only a simple rule, because legitimate websites can also use multiple subdomains.

### 4.5 Punycode Marker

Internationalised domain names may use a representation called Punycode. Hostname labels beginning with `xn--` can indicate this representation.

The checker flags the `xn--` marker so the user can examine the hostname more closely. Punycode itself is not proof that a domain is malicious.

### 4.6 Use of HTTP

HTTP does not provide the transport encryption associated with HTTPS. For that reason, the program reports URLs that use HTTP.

However, HTTPS alone does not prove that a website is legitimate. A malicious website can also use HTTPS, so users should consider other signs before trusting a link.

## 5. Technologies Used

The project uses Python 3 and its built-in libraries.

- **Python 3:** Used to implement the URL checking logic and command-line interface.
- **`urllib.parse`:** Used to parse the URL and identify information such as the hostname and scheme.
- **`re`:** Used for pattern matching when checking whether a hostname resembles an IPv4 address.
- **Nano:** Used to create and edit project files in the Kali Linux terminal.

No third-party Python packages are required.

## 6. How the Program Works

The program follows these basic steps:

1. It displays the project title and a short explanation.
2. It asks the user to enter a URL.
3. It checks whether the user entered `quit`. If so, the program exits.
4. It handles empty input and attempts to parse the URL text.
5. It checks the URL against the six warning conditions.
6. It displays each warning that was detected.
7. It prints a summary of the result.
8. It returns to the input prompt so another URL can be checked.

The program also handles selected malformed inputs instead of stopping unexpectedly.

## 7. How to Run the Project

### Requirements

You need:

- Python 3 installed on your system.
- A terminal or command-line interface.
- The project files downloaded or cloned onto your computer.

### Running on Kali Linux

Open a terminal and move to the project directory:

```bash
cd ~/phishing-url-awareness
```

Start the program:

```bash
python3 phishing_checker.py
```

Enter a sample URL when prompted. To stop the program, type:

```text
quit
```

No installation of additional Python packages is needed.

## 8. Example Execution

### Example: URL using an IP address and HTTP

**Input:**

```text
http://192.0.2.10/account
```

**Example output:**

```text
Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

Summary: 2 warning(s) detected.

Never enter passwords from unexpected links.
```

The output shows that the program detected two warning signs in the supplied text.

The address used in this example belongs to a documentation and testing range. It is included as a sample rather than as a real website to investigate.

## 9. Testing and Validation

Testing was performed by entering different sample URLs and checking whether the program displayed the expected warning messages.

The five main test cases are documented in `tests/test_samples.md`.

| Test case | Purpose | Expected result |
|---|---|---|
| 1 | A URL with no listed warning signs | Safety disclaimer and no-warning summary |
| 2 | An IP address used with HTTP | Two warnings |
| 3 | A URL containing `@` and using HTTP | Two warnings |
| 4 | A hostname with many segments | One warning |
| 5 | A hostname containing `xn--` | One warning |

The first two tests and the remaining three tests were run, and their observed output matched the expected results.

These tests confirm that the selected conditions work for the examples used. They do not establish that the program can identify every phishing URL.

## 10. Improvements Included

A few improvements were added to make the program easier to use.

- **Repeated URL checking:** The user can check multiple URLs without restarting the program each time.
- **Quit command:** Typing `quit` provides a simple way to exit.
- **Warning summary:** The program counts the warning messages returned for each URL.
- **Empty-input handling:** The program displays a message when the user submits an empty input.
- **Malformed-input handling:** Selected URL parsing errors are handled with a helpful message.
- **Clear output:** Each warning appears separately so that the user can understand the result.

## 11. Limitations

This is a basic educational project, and it has several limitations.

- It checks only six predefined warning signs.
- A suspicious URL may not contain any of these signs.
- A legitimate URL may trigger one or more warnings.
- The program does not visit websites or check their current reputation.
- It does not verify domain ownership, website content, or certificate details.
- It cannot determine with certainty whether a URL is malicious.
- The absence of warnings does not mean that a URL is safe.

For these reasons, the output should be treated as an awareness aid rather than a final security decision.

## 12. Ethical Use and Safety

This project is intended for educational use and phishing awareness. Users should avoid opening unexpected links or entering passwords and financial information on websites they have not verified.

The program does not send the entered URL to an external service. It processes the text locally within the Python application.

Users should remember that careful inspection, independent verification, and good security practices are still important even when a URL does not trigger a warning.

## 13. Future Improvements

The project could be extended in several ways in the future:

- Add more URL validation and edge-case tests.
- Improve handling of unusual or malformed hostname formats.
- Allow users to save test results to a local report.
- Add a graphical user interface for users who prefer not to use a terminal.
- Add an optional reputation-checking feature using a trusted external service, with clear user consent and appropriate privacy precautions.

Any future reputation-checking feature would need additional design and testing. It is not included in the current version.

## 14. Project Structure

```text
phishing-url-awareness/
├── phishing_checker.py
├── README.md
├── requirements.txt
├── tests/
│   └── test_samples.md
└── screenshots/
    └── sample_run.png
```

## 15. Conclusion

The EWB Phishing URL Awareness Checker demonstrates how basic Python programming can be used to examine URL text for selected warning signs. Through this project, I practised URL parsing, pattern matching, conditional logic, loops, exception handling, and testing.

The project also highlights an important lesson in cybersecurity: a URL should not be trusted simply because it looks normal or does not trigger a warning. Users should always check links carefully and follow safe browsing practices.

## Author

**Name:** Naresh Kalyan

**Project:** EWB Phishing URL Awareness Checker

**Date:** 28th October 2026
