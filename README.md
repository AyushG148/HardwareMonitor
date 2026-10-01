# HardwareMonitor

A Python-based hardware monitoring tool that displays real-time CPU, RAM, and GPU statistics.

## Features

* CPU usage monitoring
* RAM usage monitoring
* CPU temperature monitoring
* GPU usage monitoring
* GPU temperature monitoring
* Supports NVIDIA and Intel GPUs through LibreHardwareMonitor

## Technologies Used

* Python
* psutil
* pythonnet
* LibreHardwareMonitor

## How to Run

1. to setup virtual environment

1) Open terminal
2) type ---> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
3) type ---> .\.venv\Scripts\Activate.ps1

2. Run the program:

```powershell
python main.py
```

The program continuously displays hardware statistics in the terminal.

## Example Output

```text
Cpu Usage = 42.9%
Ram Usage = 54.8%
Cpu Temperature = 61.0°C
NVIDIA GeForce MX150 usage = 0.0%
NVIDIA GeForce MX150 Temperature = 57.0°C
```
