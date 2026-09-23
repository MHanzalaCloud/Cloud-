# File Permissions - Day 8

## Permission Format
- Owner | Group | Others
- r = 4, w = 2, x = 1

## Examples I saw today
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/notes$ ls -l
total 8
-rw-r--r-- 1 muhammad_hanzala muhammad_hanzala   0 Sep 22 14:02 notes.txt
-rw-r--r-- 1 muhammad_hanzala muhammad_hanzala 167 Sep 23 10:21 permissions-day8.md
-rw-r--r-- 1 muhammad_hanzala muhammad_hanzala 374 Sep 23 10:11 week1-summary.md

muhammad_hanzala@MUHAMMAD-HANZLA:/$ ls -l /etc/passwd
-rw-r--r-- 1 root root 1492 Apr 18 10:27 /etc/passwd
muhammad_hanzala@MUHAMMAD-HANZLA:/$ ls -l /usr/bin/ls
-rwxr-xr-x 1 root root 142312 Jun 22  2025 /usr/bin/ls
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ chmod 600 a.txt
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ chmod 755 b.txt
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ chmod 620 c.txt
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ chmod 700 mydir
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ ls -l
total 4
-rw------- 1 muhammad_hanzala muhammad_hanzala    0 Sep 23 12:30 a.txt
-rwxr-xr-x 1 muhammad_hanzala muhammad_hanzala    0 Sep 23 12:30 b.txt
-rw--w---- 1 muhammad_hanzala muhammad_hanzala    0 Sep 23 12:30 c.txt
drwx------ 2 muhammad_hanzala muhammad_hanzala 4096 Sep 23 12:30 mydir
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ chmod u+s b.txt
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ chmod +t mydir
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ ls -l
total 4
-rw------- 1 muhammad_hanzala muhammad_hanzala    0 Sep 23 12:30 a.txt
-rwsr-xr-x 1 muhammad_hanzala muhammad_hanzala    0 Sep 23 12:30 b.txt
-rw--w---- 1 muhammad_hanzala muhammad_hanzala    0 Sep 23 12:30 c.txt
drwx-----T 2 muhammad_hanzala muhammad_hanzala 4096 Sep 23 12:30 mydir
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ ls -ld mydir
drwx-----T 2 muhammad_hanzala muhammad_hanzala 4096 Sep 23 12:30 mydir
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ chwon root:root a.txt
Command 'chwon' not found, did you mean:
  command 'chown' from deb coreutils (9.4-3ubuntu6.2)
  command 'chcon' from deb coreutils (9.4-3ubuntu6.2)
Try: sudo apt install <deb name>
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ sudo chwon root:root a.txt
[sudo] password for muhammad_hanzala:
sudo: chwon: command not found
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ sudo chown root:root a.txt
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ ls -l a.txt
-rw------- 1 root root 0 Sep 23 12:30 a.txt
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ sudo chown muhammad_hanzala:muhammad_hanzala a.txt
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs/permission-practice$ ls -l a.txt
-rw------- 1 muhammad_hanzala muhammad_hanzala 0 Sep 23 12:30 a.txt
