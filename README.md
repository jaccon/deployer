# Deployer Script
## The easy way to deploy any application without need install any software addictional

The Deployer script is a best way to deploy any application to production environment using only Python and SSH

### Configuration
First you need to open file deployer.config.json and put your informations like this:

~~~~
{
"configurations": [
    {
    "host": "your-server-name",
    "ssh_port": "ssh-tcp-port",
    "deploy_dir": "/deploy-folder/",
    "deploy_dist": "dist-folder",
    "prod_dist": "/production-folder",
    "tasks": [
        {
        "title": "Task Description 1",
        "command": "ssh -p 22 root@your-server-name 'your shell command inside ..... ' ",
        "local": "local",
        "status": "enabled"
        },
        {
        "title": "Task Description 2",
        "command": "ssh -p 22 root@your-server-name 'your shell command inside ..... ' ",
        "local": "local",
        "status": "enabled"
        }
    ]
    }
    ]
}
~~~~

### Running script

To running the script is very easy, just need insert the command in shell:

~~~~
python deployer.py
~~~~

### Demo

[![](http://img.youtube.com/vi/9Vma9xSXlQM/0.jpg)](http://www.youtube.com/watch?v=9Vma9xSXlQM "")


Just fun!