# AutoSkip

AutoSkip is a tool that automates clicking the "Skip Intro" button or performing similar actions in applications and video players, saving you time and simplifying interaction with interfaces.

## Installation

To install and set up the project, follow these steps:

1. Clone the repository to your computer:
   ```bash
   git clone https://github.com/dishai/autoskip.git
   ```

2. Navigate to the project directory:
   ```bash
   cd autoskip
   ```

3. (Optional, but recommended) Create a virtual environment to isolate dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

4. Install the dependencies listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

5. Install the font:
   The project uses a font, the license for which is included in the `OFL.txt` file. To install the font:
   - Locate the font file in the project directory (`serati.ttf`).
   - On Windows: Double-click the font file and select "Install".
   - On macOS: Double-click the font file and choose "Install Font" in the Font Book application.
   - On Linux: Copy the font file to the `~/.fonts/` directory and update the font cache with the command `fc-cache -fv`.

**Note:** Ensure you have Python 3 and the `pip` package manager installed.

## Running the Project

Depending on your operating system, you can run the project as follows:

- **For Windows:**
  If you want to use the pre-built executable, simply run:
  ```
  AutoSkip.exe
  ```

- **For macOS/Linux or if running from source code:**
  Launch the main script using Python:
  ```bash
  python main.py
  ```
  or, if using Python 3:
  ```bash
  python3 main.py
  ```

**Note:** Before running, ensure all dependencies are installed and the virtual environment is activated (if used).

## Usage Examples

Below are examples of how you can use AutoSkip:

- **Automatically skipping intros in a video player:**
  If you want to skip intros in a specific video player, simply launch the program, and it will automatically click the "Skip" button as soon as it appears.

- **Setting a delay before clicking:**
  If you need to set a delay before the automatic click (e.g., 5 seconds), use the `interval` parameter:
  ```bash
  python main.py
  ```

**Note:** Ensure the target application or window is active while the program is running.

## License

This project is distributed under the license specified in the `LICENSE` file. Please review it for detailed information about rights and restrictions.

## Contact

If you have questions, suggestions, or want to report a bug, you can reach me via Telegram:

- Telegram: @dishacker
