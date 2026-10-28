#!/usr/bin/env python3
"""Loopback-only demo server with intentionally incomplete security headers."""
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"<!doctype html><title>Local Security Lab</title><h1>Local-only practice page</h1>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        # Intentionally incomplete headers for a controlled training exercise.
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print("lab:", fmt % args)

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8765), Handler)
    print("Local lab listening at http://127.0.0.1:8765 (Ctrl+C to stop)")
    server.serve_forever()
