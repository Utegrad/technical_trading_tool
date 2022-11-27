#######
Project
#######

Automations for tracking stock quotes, calculating technical indicators, and generating alerts as specific indicators
occur.

************
Installation
************

Python Elements
===============

- Create a python virtual env
- pip install packages from `requirements/local.txt` for local development
- pip install packages from `requirements.txt` for production installation
- create a PostgreSQL database and connection string

***********
Development
***********

Stages
======
Plan for stages of development

- Start of CLI
- Upsert the ticker list in database
- Import historical quote data
- calculate technical markers on historical data
- Codify trading strategy
- Test trading strategy against historical data against baseline from SPY or QQQ
