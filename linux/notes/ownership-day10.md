muhammad_hanzala@MUHAMMAD-HANZLA:/$ cd ~
muhammad_hanzala@MUHAMMAD-HANZLA:~$ ls
Cloud.pem                  cloud-portfolio  my-key.pem   opt                                              practice       snap                test
Cloud.pem:Zone.Identifier  image.jpg        myscript.sh  permissions-game                                 projects       system_report.txt   weather.py
Key.pem                    key.pem          newkey.pem   pexels-eberhardgross-443446.jpg:Zone.Identifier  server_config  terraform-projects
muhammad_hanzala@MUHAMMAD-HANZLA:~$ cd ~/projects/devops
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops$ ls
README.md  docker  k8s  linux  networking  python
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops$ cd linux
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux$ cd labs
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs$ sudo chgrp devopsgroup file3.txt
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs$ ls
'file with spaces.txt'   file1.txt   file2.txt   file3.txt   permissions-day8.md   script.sh   testdir
muhammad_hanzala@MUHAMMAD-HANZLA:~/projects/devops/linux/labs$ ls -l
total 12
-rw-r--r-- 1 muhammad_hanzala muhammad_hanzala   21 Sep 22 14:22 'file with spaces.txt'
-rwxr-xr-x 1 muhammad_hanzala muhammad_hanzala    0 Sep 23 10:25  file1.txt
-rw-r--r-- 1 muhammad_hanzala muhammad_hanzala    0 Sep 23 10:25  file2.txt
-rw------- 1 muhammad_hanzala devopsgroup         0 Sep 23 10:25  file3.txt
-rw-r--r-- 1 muhammad_hanzala muhammad_hanzala  543 Sep 23 10:33  permissions-day8.md
-rwxr-xr-x 1 muhammad_hanzala muhammad_hanzala    0 Sep 22 14:02  script.sh
drwx------ 2 muhammad_hanzala muhammad_hanzala 4096 Sep 23 10:25  testdir
