#!/usr/bin/env python3
"""
EstateFlow Startup Script
Run this to start the Flask application
"""
import os
import sys
import subprocess

def main():
    print("\n" + "=" * 50)
    print("   EstateFlow - Real Estate Platform")
    print("=" * 50 + "\n")

    # Get the directory of this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    # Check if venv exists, create if not
    venv_path = os.path.join(base_dir, 'venv')
    if not os.path.exists(venv_path):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, '-m', 'venv', venv_path])
        print()

    # Install dependencies
    print("Installing dependencies...")
    if sys.platform == 'win32':
        pip_exe = os.path.join(venv_path, 'Scripts', 'pip.exe')
    else:
        pip_exe = os.path.join(venv_path, 'bin', 'pip')

    subprocess.check_call([pip_exe, 'install', '-q', '-r', 'requirements.txt'])
    print()

    # Print startup info
    print("=" * 50)
    print("Starting EstateFlow...")
    print("=" * 50)
    print()
    print("🌐 Website URL: http://localhost:5000")
    print("🔐 Admin URL:   http://localhost:5000/admin/login")
    print("👤 Username:    admin")
    print("🔑 Password:    admin123")
    print()
    print("Press Ctrl+C to stop the server")
    print()

    # Run the Flask app
    if sys.platform == 'win32':
        python_exe = os.path.join(venv_path, 'Scripts', 'python.exe')
    else:
        python_exe = os.path.join(venv_path, 'bin', 'python')

    subprocess.call([python_exe, 'app.py'])

if __name__ == '__main__':
    main()
