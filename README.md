# DNS-Change
Change Airtel DNS to auto and static on boot for pi-hole on raspberry pi

## Installation

# Python
```
sudo apt install python
```

# Python-Selenium
```
pip install selenium
```

# Chromium and Chrome-driver
```
sudo apt install chromium-browser chromium-chromedriver
```

# Add the python script at startup
```
//Copy file to /bin

sudo cp /path/to file/file /bin

#Open crontab

sudo crontab -e

#In crontab file add

@reboot sleep 60 && python3 /bin/DNSWebScript.py &
