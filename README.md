# e-commerce - api
>Step-by-step setup tutorial of the api.
>
>The tutorial assumes that the user's OS is UNIX based, **if not make the appropriate changes and select the correct OS in the documentation**. 
>
>_If running on Windows remember to enable Hyper-V and virtual environments._ 

#### Pre Requiments
* [Docker](https://docs.docker.com/engine/install/debian/)
> create docker group, _**you'll probably have to reboot after this**_.
```shell script
sudo groupadd docker
sudo usermod -aG docker $USER
```
* [Docker Compose](https://docs.docker.com/compose/install/)

#### Git clone
>[Clone the project](git@github.com:pcarvalho-dev/e-commerce.git) and go to the chosen directory, for example:
```shell script
git clone git@github.com:pcarvalho-dev/e-commerce.git
cd ~/e-commerce
```

#### GitHub's registry login

> See how to generate a GitHub token: * [Personal access token with access to GitHub packages](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

```shell script
echo <your-personal-access-token> | docker login ghcr.io --username <your-username> --password-stdin
```

#### Pycharm Integration
>It's possible to run your container and debug with it using PyCharm.

* Build, Execution, Deployment
>To enable docker in PyCharm go to: File>Settings>Build,Execution,Deployment>Docker
> ![Enable Docker](static/documentation/enable_docker.png)
>Click in the **+** icon and use the default settings

* Project Interpreter
>We need to create a remote python interpreter, basically the python interpreter running inside our container.
>
>Go to File>Settings>Project: e-commerce>Python Interpreter
>
>Add a configuration clicking in the ![setting icon](static/documentation/setting_icon.png) icon and clicking on "Add" and configure it like so: ![Docker Compose Config](static/documentation/docker_compose_config.png)

* Run/Debug Configurations
>The final step in the setup is to configure the Run/Debug configuration, **create one using the Remote Interpreter**. ![Run/Debug Config](static/documentation/run_debug_config.png)

#### VScode Integration

> Init containers

```bash
docker-compose up
```

> Change DEBUG_INTEGRATION in .env to DEBUG_INTEGRATION=vscode

> Press f5

#### Deploy
>First deploy
```shell script
docker-compose up --build
```
>Regular Deploy
```shell script
docker-compose up
 ```
>Once the project is up and running just debug the application by clicking in the debug icon ![debug icon](static/documentation/pycharm_debug_icon.png)
>
>>You ready to go!

* Redeploy restoring all databases
```shell script
python3 init.py
```

#### Migrations and DB
>To make a migration on the database use:
```shell script
docker-compose exec api flask db migrate -m"<your message>"
```
>if there's a conflict with the migration heads, run:
```shell script
python3 db-merge.py
``` 

>If you wish to update the db dupms, use:
```shell script
bash db-dump
```


