# CCQR

## Prerequisites

Firstly, you'll need to have a MySQL Database installed and running.  You'll need a username, a password, a name for the database, and the host information for the database (localhost by default).

## Installation & Configuration

Clone down the repository.

```bash
git clone https://github.com/notoriouslogank/ccqr.git
```

Create a file called constants.py and add the following information:

```bash
HOST='<ip address>'
USER='<username>'
PASSWD='<passwd>'
DATABASE='<database>'
```

Install dependancies:

```bash
pip install -r requirements.txt
```

Run dbsetup.py:

```bash
python3 dbsetup.py
```

Once configuration is done (no output if successful), you can go ahead and run main.py:

```bash
python3 main.py
```

## Usage

COMING SOON!
