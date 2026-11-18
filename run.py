# -*- encoding: utf-8 -*-

"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from api import app, db


def listen_port():
    """Port for the local dev server.

    macOS AirPlay Receiver binds port 5000, which is Flask's default.
    Set PORT in the environment or in .env to use a free port.
    """
    raw = os.environ.get('PORT', '').strip()
    if not raw:
        return 5000

    try:
        port = int(raw)
    except ValueError:
        raise SystemExit('PORT must be an integer, got %r.' % (raw,))

    if port < 1 or port > 65535:
        raise SystemExit('PORT must be between 1 and 65535, got %s.' % (port,))

    return port


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=listen_port())
