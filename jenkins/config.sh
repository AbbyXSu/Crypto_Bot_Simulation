#! /bin/bash
# write out playbook, inventory
# with roles
# ssh keys generated from jenkins machine for jenkins user (ssh-keygen)
# sudo su - jenkins, install ansible on this machine for jenkins
# jenkins runs playbook
# make sure ~/.local/bin exists and is on your PATH
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
# install ansible with pip
pip3 install --user ansible
cd ansible
ansible-playbook -i inventory playbook.yaml