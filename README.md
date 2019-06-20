Repository with a demo of the game of mastermind a game of the eighties

To start the project you must have Docker installed and execute the following instructions

Requirementes
* [Docker](https://www.docker.com/) - Build, Share, and Run Any App, Anywhere

### Installation

```sh
$ git clone git@github.com:pollitosabroson/master_mind.git
$ cd master_mind/docker/dev
$ docker-compose build --no-cache
```
Execute project.
```sh
$ docker exec -it python_master_mind bash
$ python master_mind.py
```
