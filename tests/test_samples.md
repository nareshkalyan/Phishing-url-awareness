# Test Samples — EWB Phishing URL Awareness Checker

## 1. Testing Objective

The objective is to verify that the program identifies selected URL warning signs and displays the correct result and warning summary.

The checker analyzes URL text only. It does not open URLs or send network requests.

## 2. Test Cases and Results

### Test Case 1: URL with No Listed Warning Signs

**Input:**
`https://www.example.com/login`

**Expected result:**
- No listed warning signs found.
- The program displays a disclaimer that this does not prove safety.
- Summary: No listed warning signs detected.

**Observed result:** Passed.

### Test Case 2: IP Address and HTTP

**Input:**
`http://192.0.2.10/account`

**Expected result:**
- Uses an IP address instead of a familiar domain.
- Uses HTTP.
- Summary: 2 warning(s) detected.

**Observed result:** Passed. Both warnings and the correct summary were displayed.

### Test Case 3: URL Containing an At Symbol

**Input:**
`http://example.com@sample.invalid/login`

**Expected result:**
- Contains an `@` symbol warning.
- Uses HTTP warning.
- Summary: 2 warning(s) detected.

**Observed result:** Passed. The @ symbol and HTTP warnings appeared, with a summary of 2 warnings.

### Test Case 4: Hostname with Many Segments

**Input:**
`https://a.b.c.d.e.example.invalid/path`

**Expected result:**
- Contains many hostname segments/subdomains warning.
- Summary: 1 warning(s) detected.

**Observed result:** Observed result: Passed. The hostname-segments warning appeared, with a summary of 1 warning.

### Test Case 5: Punycode-Style Hostname

**Input:**
`https://xn--example.invalid/`

**Expected result:**
- Contains a punycode-style hostname warning.
- Summary: 1 warning(s) detected.

**Observed result:** Observed result: Passed. The punycode-style hostname warning appeared, with a summary of 1 warning.

## 3. Testing Summary

| Test case | Purpose | Status |
|---|---|---|
| 1 | No listed warning signs | Passed |
| 2 | IP address and HTTP | Passed |
| 3 | At symbol | Passed |
| 4 | Many hostname segments | Passed |
| 5 | Punycode marker | Passed |

## 4. Limitations

These tests cover selected warning signs only. The checker cannot guarantee that a URL is safe or malicious. A URL with no listed warning signs may still be dangerous.
