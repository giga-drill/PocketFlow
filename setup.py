import os
import subprocess
import sys
import platform

def main():
    """Set up the virtual environment and install dependencies."""
    print("=" * 50)
    print("PG-GPT Setup Utility")
    print("=" * 50)
    
    # Determine the operating system
    os_name = platform.system()
    print(f"Detected operating system: {os_name}")
    
    # Check if Python is installed
    try:
        python_version = subprocess.check_output(
            [sys.executable, "--version"], 
            universal_newlines=True
        ).strip()
        print(f"Using Python: {python_version}")
    except Exception as e:
        print(f"Error checking Python version: {e}")
        print("Please ensure Python 3.7+ is installed and in your PATH.")
        return 1
    
    # Create virtual environment
    venv_dir = "venv"
    if os.path.exists(venv_dir):
        print(f"Virtual environment '{venv_dir}' already exists.")
        recreate = input("Do you want to recreate it? (y/n): ").lower() == 'y'
        if recreate:
            try:
                if os_name == "Windows":
                    os.system(f"rmdir /s /q {venv_dir}")
                else:
                    os.system(f"rm -rf {venv_dir}")
                print(f"Deleted existing '{venv_dir}' directory.")
            except Exception as e:
                print(f"Error removing existing virtual environment: {e}")
                return 1
        else:
            print("Using existing virtual environment.")
    
    if not os.path.exists(venv_dir):
        print(f"Creating virtual environment in '{venv_dir}'...")
        try:
            subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
            print("Virtual environment created successfully.")
        except Exception as e:
            print(f"Error creating virtual environment: {e}")
            return 1
    
    # Determine activation script path
    if os_name == "Windows":
        activate_script = os.path.join(venv_dir, "Scripts", "activate")
        python_path = os.path.join(venv_dir, "Scripts", "python")
        pip_path = os.path.join(venv_dir, "Scripts", "pip")
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")
        python_path = os.path.join(venv_dir, "bin", "python")
        pip_path = os.path.join(venv_dir, "bin", "pip")
    
    # Install dependencies
    print("Installing dependencies...")
    try:
        if os_name == "Windows":
            subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])
        else:
            os.system(f"source {activate_script} && pip install -r requirements.txt")
        print("Dependencies installed successfully.")
    except Exception as e:
        print(f"Error installing dependencies: {e}")
        return 1
    
    # Create data directory if it doesn't exist
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created '{data_dir}' directory for essays.")
    
    # Print activation instructions
    print("\n" + "=" * 50)
    print("Setup complete!")
    print("=" * 50)
    print("\nTo activate the virtual environment:")
    
    if os_name == "Windows":
        print(f"Run: {venv_dir}\\Scripts\\activate")
    else:
        print(f"Run: source {venv_dir}/bin/activate")
    
    print("\nThen set your OpenAI API key:")
    if os_name == "Windows":
        print("set OPENAI_API_KEY=your_api_key_here")
    else:
        print("export OPENAI_API_KEY=your_api_key_here")
    
    print("\nFinally, run the application:")
    print("python main.py")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 