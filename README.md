# IPC Debugger Project

This project runs locally using Python.

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

Dependencies: Flask and Gunicorn (for web dashboard). Install with `pip install -r requirements.txt`.

## Usage

Run the main script to start the IPC simulation:

```bash\npython main.py\n```\n\n**Web Dashboard:**\n```bash\npython app.py\n```\nOpen http://localhost:5001 in browser (run `python main.py` first for logs).\n\nThis will:
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
`logs.json`: Generated log file (JSON lines).

## Requirements\n\n- Python 3.6+\n- Flask, Gunicorn (pip install -r requirements.txt)\n- Standard library modules

## License

MIT License