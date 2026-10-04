"""
run.py
======
Application entry point for Handwritten Digit Recognition Flask Server.
Binds to 0.0.0.0 so both localhost and 127.0.0.1 resolve smoothly on Windows.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    port = app.config.get("PORT", 5000)
    print(f"\n=======================================================")
    print(f"  Starting Handwritten Digit Recognition API Server")
    print(f"  Local URL:    http://127.0.0.1:{port}")
    print(f"  Network URL:  http://localhost:{port}")
    print(f"=======================================================\n")
    app.run(host="0.0.0.0", port=port, debug=False)
