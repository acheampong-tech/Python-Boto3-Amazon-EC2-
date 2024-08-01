# Python-Boto3-Amazon-EC2
Automating AWS EC2 Management with Python and Boto3

AUTHOMATING WITH PYTHON


# update distro

sudo apt-get update && sudo apt-get upgrade

# install python

verify python, install python, install pip, pandas 

sudo apt-get install python3-pandas

sudo apt-get install python3-sympy

python3 -m pip install boto3

sudo apt update

#  Ensure python3-venv is installed 
sudo apt install python3-venv       >>>>>>>>>>>>>>>>Replace myenv with the directory name you want for your virtual environment.

#  Create a virtual environment 

python3 -m venv myenv                        


#  Activate the virtual environment 
source myenv/bin/activate
pip install boto3                           >>>>>>>>>>>>>>>>Install boto3 if it wasnt
python3 create_ec2_instance.py

# install aws
sudo apt install curl unzip -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
aws configure

# create programatic access keys
AWS_ACCESS_KEY_ID='your-access-key-id'

AWS_SECRET_ACCESS_KEY='your-secret-access-key'

