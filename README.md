# Twitter Popularity
#### By [fornesarturo](https://github.com/fornesarturo) and [miguel-mzbi](https://github.com/miguel-mzbi)

## Dependencies

* **Ubuntu-based linux distribution**
    * Or knowledge to adapt these commands to your distribution.
* Python 3.5.2+ with at least the virtualenv module installed.

All necessary commands from scratch:

```bash
# Install Python 3.x interpreter.
sudo apt install python3
# Install Python package manager.
sudo apt install python3-pip
# Install virtualenv Python module, globally.
sudo -H pip install virtualenv
# Non-global installation.
pip install virtualenv
```

## Usage

### Using our pre-populated database

Install Redis:

```bash
sudo apt install redis-server
```

In case it doesn't come included, install redis-tools, this contains the *command line interface* (CLI):

```bash
sudo apt install redis-tools
```

Once you have Redis installed check by running the following commands:

```bash
redis-server
redis-cli
```

Then to copy our DB file, *dump.rdb*, first stop the service, then copy the file to the correct location, finally start again the service:

```bash
# Stop the service.
sudo service redis-server stop
# Assuming you're in this repository's directory.
# Copy the .rdb file.
sudo cp ./dump.rdb /var/lib/redis/dump.rdb

# Restart the service.
sudo service redis-server start
```

After this run the bash script env_setup.sh to create and enter, or later on just enter, our specific *Virtual Environment* (virtualenv) created from the *requirements.txt* file.

```bash
# The dot is needed to set the target directory as this one.
. ./env_setup.sh
```

#### Now to Run it

Run *UserEvaluation.py* with the Python interpreter inside the *Virtual Environment* as such:

```bash
# Make sure your terminal session is in the tweet environment
# Something like:
# (tweet) user@PC#: $
python UserEvaluation.py
```