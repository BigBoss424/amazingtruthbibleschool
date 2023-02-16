#! /bin/bash
# The purpose of this install script is to install the LAMP stack on the server for this website, and
# for future websites. 

#Install Apache2 
echo "Installing Apache2..."
sudo apt install apache2

#Install MySQL
echo "Installing MySQL..."
sudo apt install mysql 

#Install PHP
echo "Installing PHP..."
sudo apt install php8.2

#Installing Required PHP Modules
echo "Installing PHP Modules..."
sudo apt install 