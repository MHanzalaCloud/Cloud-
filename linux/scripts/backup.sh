#!/bin/bash

 SOURCE="$HOME/projects/devops"
 DEST="$HOME/backups"
 DATE=$(date +%Y-%m-%d_%H-%M)

 mkdir -p "$DEST"
 tar -czf "$DEST/devops-backup-$DATE.tar.gz" "$SOURCE"

 echo "Backup completed: $DEST/devops-backup-$DATE.tar.gz"
 ls -lh "$DEST"
