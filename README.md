# Elearning

# how to install PostgreSQL

## 1 check your PostgreSQL version
postgres –version　

## 2 if the version is older than 9, pls update 
amazon-linux-extras

## 3 install newer virsion
$ sudo amazon-linux-extras install postgresql11  
$ sudo yum install postgresql-server  
$ sudo yum install postgresql-devel  
$ sudo su -   
  #postgresql-setup initdb  
  #systemctl start postgresql.service  
  #exit  

## 4 edit conf file
basically you can follow that Youtube video↓

https://gist.github.com/ericpkatz/19614dd090e6408f3eef746ddc49e6d6  
https://www.youtube.com/watch?v=elQvh6bNv3M
* Unlike that youtube video, you cannot not find "vim /var/lib/pgsql9/data/pg_hba.conf", when you updated. You can instead edit "vim /var/lib/pgsql/data/pg_hba.conf"
* you don't need to modify Use md5 auth
