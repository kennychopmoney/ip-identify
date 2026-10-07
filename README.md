# URL to IP lookup tool

This project contains a small Python tool that converts a URL or hostname into one or more IP addresses.

## What it does

The script accepts a URL such as `https://example.com` or a hostname like `example.com`, extracts the host, and resolves it using the system DNS. It returns the IP addresses associated with that hostname.

## Files

- `url_to_ip.py` — the command-line tool
- `README.md` — usage instructions and GitHub publishing steps
- `.gitignore` — ignores local Python cache files

## Run the tool

From the project folder, run:

```bash
python url_to_ip.py https://example.com
```

Example output:

```text
Hostname: example.com
IP addresses:
93.184.216.34
```

You can also pass a hostname without a URL scheme, including a path or port:

```bash
python url_to_ip.py example.com
python url_to_ip.py example.com/path
python url_to_ip.py example.com:8080
```

## PowerShell alternative

If you want to do the same lookup directly in PowerShell, run:

```powershell
$url = 'https://example.com/path'
$uri = [System.Uri]$url
[System.Net.Dns]::GetHostAddresses($uri.DnsSafeHost) |
    Select-Object -ExpandProperty IPAddressToString
```

This works for the hostname part of the URL only.

## Initialize and commit locally

This folder is ready to become a Git repository. In PowerShell, run:

```powershell
Set-Location 'C:\Users\HomePC\Desktop\ip identify'
git init
git add .
git commit -m "Create URL to IP tool"
```

## Push to GitHub

1. Create a new empty repository on GitHub.
2. Do not initialize it with a README file because this project already includes one.
3. Connect the local repository to GitHub:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

If GitHub asks for authentication, use your GitHub username and a personal access token instead of a password.

## Notes

- DNS can return multiple results for the same hostname.
- The results can differ by network, region, or time.
- This tool uses the local machine's DNS resolver and should work on Windows, Linux, and macOS.
