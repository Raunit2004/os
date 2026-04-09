# IPC Debugger

A Python-based Inter-Process Communication (IPC) debugger that simulates message passing between processes using multiprocessing queues. It includes logging, message delay analysis, and basic threat detection.

## Features

- **Multiprocessing IPC Simulation**: Demonstrates communication between multiple sender processes and a receiver process using Python's multiprocessing Queue.
- **Message Logging**: Logs all messages with timestamps and delays.
- **Message Loss Detection**: Detects potential message loss or out-of-order delivery.
- **Threat Analysis**: Scans logs for suspicious keywords like "hack", "attack", "malware".
- **GUI Dashboard**: Simple Tkinter-based GUI for monitoring (optional).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ipc-debugger.git
   cd ipc-debugger
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

   Note: This project uses only Python standard library modules, so no external dependencies are required.

## Usage

Run the main script to start the IPC simulation:

```bash
python main.py
```

This will:
- Start two sender processes sending messages to a shared queue.
- Start a receiver process that reads messages and logs them.
- Run for 10 seconds, then terminate processes.
- Analyze the logs for suspicious activity.

### Output

The program will print received messages with delays and any detected message loss errors. At the end, it performs a threat analysis on the logs.

### GUI (Optional)

To launch the GUI dashboard:

```python
from gui import launch_gui
launch_gui()
```

## Files

- `main.py`: Entry point that starts the multiprocessing simulation.
- `ipc.py`: Contains sender and receiver functions for IPC.
- `logger.py`: Handles logging messages to a file.
- `analyzer.py`: Analyzes logs for suspicious activity.
- `debugger.py`: Wrapper for analysis.
- `gui.py`: Simple Tkinter GUI.
- `logs.txt`: Generated log file (ignored in git).

## Requirements

- Python 3.6+
- Standard library modules: multiprocessing, time, random, datetime, tkinter

## License

MIT License