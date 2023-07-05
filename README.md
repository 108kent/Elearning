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
https://gist.github.com/ericpkatz/19614dd090e6408f3eef746ddc49e6d6
