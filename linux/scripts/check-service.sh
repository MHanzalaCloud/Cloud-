#!/bin/bash
if systemctl is-active --quiet ssh; then
    echo "SSH service is running."
else
    echo "SSH service is NOT running."
fi
