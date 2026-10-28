import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check URL text for selected phishing warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["Invalid URL format. Please check the URL."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def main():
    print("=" * 45)
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")
    print("Type 'quit' to exit.")
    print("=" * 45)

    while True:
        raw_url = input("\nEnter a sample URL to inspect: ").strip()

        if raw_url.lower() == "quit":
            print("Exiting Phishing URL Awareness Checker.")
            break

        print("\nResult:")
        findings = inspect_url(raw_url)

        for item in findings:
            print("- " + item)

        if findings == [
            "No listed warning signs found. This does NOT prove safety."
        ]:
            print("\nSummary: No listed warning signs detected.")
        elif findings == ["No URL entered."]:
            print("\nSummary: No URL was provided.")
        elif findings == ["Could not identify a hostname."] or findings == [
            "Invalid URL format. Please check the URL."
        ]:
            print("\nSummary: URL could not be inspected.")
        else:
            print(f"\nSummary: {len(findings)} warning(s) detected.")

        print("\nNever enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
