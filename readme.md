# Pomodoro Timer

This is a simple Pomodoro Timer application built using Python and Tkinter. The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.

## Installation

1. Clone the repository or download the code files.
1. Create a new virtual environment. You can name it env or anything you like:

   ```Shell
      python -m venv env
   ```

   ```Shell
      .\env\Scripts\activate
   ```

   ```Shell
      source env/bin/activate
   ```

1. Install the required dependencies by running the following command in your terminal:
   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Open the terminal and navigate to the directory where the code files are located.
2. Run the following command to start the Pomodoro Timer:

   ```shell
   python main.py
   ```

3. The application window will open, displaying the timer and control buttons.
4. Click the "Start" button to start the timer. The timer will count down for 25 minutes, indicating a work session.
5. After 25 minutes, the timer will automatically switch to a 5-minute break session.
6. After every 4 work sessions, a longer break session of 20 minutes will be triggered.
7. You can click the "Reset" button to reset the timer at any time.

## Customization

You can customize the duration of the work session, short break, and long break by modifying the following constants in the code:
````
