# IPC Debugger Project

This project simulates **Multiprocessing IPC** using Python's `multiprocessing.Queue`, logs messages/delays, detects issues, and provides web/GUI dashboards for monitoring and threat analysis.

## ✨ Features (Enhanced)
- **Multi-Sender IPC Simulation**: 2 senders (P1, P2) → 1 receiver, shared queue.
- **Live Logging**: JSONL to `logs.json` with timestamps, delays.
- **Web Dashboard**: Flask on port 5001 - Live table, auto-highlights (high delay >1s yellow, suspicious keywords red), analysis summary/alerts.
- **Threat Analysis**: Keywords ("hack", "attack", etc.), high delay warnings.
- **GUI Viewer**: Tkinter app to load/analyze logs.
- **Console Debugger**: `python debugger.py`.

## 🚀 Quick Start
1. **Install deps**:
   ```
   pip install -r requirements.txt
   ```
2. **Start Dashboard** (already running):
   ```
   python app.py
   ```
   Open [http://127.0.0.1:5001](http://127.0.0.1:5001)
3. **Run Simulation** (generates logs):
   ```
   python main.py
   ```
   - Clears logs, runs 15s, prints sent/received.
   - Refresh dashboard → see table/analysis!
4. **GUI**:
   ```
   python -c "from gui import launch_gui; launch_gui()"
   ```
5. **Console Analysis**:
   ```
   python debugger.py  # Wait, add if __name__ call in debugger.py
   ```

## Demo Flow
1. `python main.py` → logs populate.
2. Dashboard auto-updates table (colors for issues).
3. Click "Analyze Logs" → see summary, warnings (high delays), alerts (keywords).
4. GUI: Load logs, run analysis popup.

## Files
- `main.py`: Multi-IPC simulation.
- `ipc.py`: sender/receiver logic.
- `logger.py`: JSONL logging.
- `debugger.py`: Analysis engine (console/JSON).
- `app.py`: Flask dashboard (:5001).
- `templates/index.html`, `static/script.js`: UI + live JS.
- `gui.py`: Tkinter GUI.
- `analyzer.py`: Legacy, deprecated.
- `logs.json`: Auto-generated.

## Production
```
gunicorn app:app -b 0.0.0.0:5001  # Procfile ready
```

## License
MIT

