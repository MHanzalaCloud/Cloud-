echo "===System Information==="
echo "Hostname      : $(hostname)"
echo "Current User  : $(whoami)"
echo "Date & Time   : $(date)"
echo "Uptime        : $(uptime -p)"
echo "IP Address    : $(hostname -I)"
echo "Memory Usage  :"
free -h
echo "Disk Usage    :"
df -h /
echo "========================================"
