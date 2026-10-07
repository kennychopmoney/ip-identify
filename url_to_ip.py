#!/usr/bin/env python3
"""Resolve a URL or hostname to one or more IP addresses."""

import argparse
import socket
import sys
from urllib.parse import urlparse, urlsplit


def resolve_host(raw_value: str):
    value = raw_value.strip()
    if not value:
        raise ValueError("A URL or hostname is required.")

    if "://" in value:
        host = urlparse(value).hostname
    else:
        host = urlsplit(f"//{value}").hostname

    if not host:
        host = value.split("/")[0].split(":")[0].strip("[]")

    if not host:
        raise ValueError(f"Could not extract a hostname from: {raw_value}")

    return host


def get_ip_addresses(host: str):
    try:
        infos = socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)
    except socket.gaierror as exc:
        raise ValueError(f"DNS lookup failed for {host}: {exc}") from exc

    addresses = sorted({entry[4][0] for entry in infos})
    return addresses


def main():
    parser = argparse.ArgumentParser(
        description="Resolve a URL or hostname to one or more IP addresses."
    )
    parser.add_argument(
        "target",
        help="URL or hostname to resolve, for example https://example.com or example.com",
    )
    args = parser.parse_args()

    try:
        host = resolve_host(args.target)
        addresses = get_ip_addresses(host)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Hostname: {host}")
    if not addresses:
        print("No IP addresses found.")
        return 1

    print("IP addresses:")
    for address in addresses:
        print(address)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
