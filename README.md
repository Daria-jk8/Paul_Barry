# :star: Paul Barry
Head First Python: A Brain-Friendly Guide 2nd Edition, 2017

Test your skills - practice: :fire: :thumbsup: :clap:
---
-  --> Magnets: experimental code, for frequency calculation, template, database
-  --> Sharpen a pencil
-  --> An exercise

| Chapter | CONTENTS | Specification/description | note:pushpin:, attention:warning: |
|:-:| --- | --- | --- |            
| 1 | `Basics. Let's start quickly` |  import datetime, random, time, sys, os; if/elif/else; time.sleep(), random.randint(from, to); for with [list], "str", range(...); | p.74 bottles of beer :beers:   |
| 2 | `Lists. Working with ordered data` | OOP; Python has 4 built-in data structures: list, tuple, dict, set; mutable/immutable; len(); .append(); .remove(); .pop(); .extend(); .insert(); ' '.join([start:stop:step]) | everything is an object; p. 108 looks like a copy but not a copy|
| 3 | `Structuring. Working with co-structuring` | for k, v in  .items(); setdefault; .union(); .difference(), .intersection(); import pprint | key:value;  setdefault = if/not in; p.173 dict containing dict |
| 4 | `Reuse. Functions and modules` | bool: True/False; annotation -> ... type hints; import setup; PIP, PyPI; py.test  | def; PEP 8 is a set of guidelines, not rules. Do not blindly obey them, just take into account; -> set; p. 222 def-arguments are passed by value, by reference. Pytest|
| 5_web | `Create a web application. Return to the real world`  | pip install flask; :bell:@.route('/'); Jinja2; HTTP 100-500; import Flask, render_template, request, redirect | p.234(scheme); :eyes: 🤯 FLASK_p.239; if __name__ == ‘__main__’; PythonAnywhere |
| 6_web | `Storage and processing of data. Save data`  | open('.txt')/with open('.txt') as ...; import escape; .split() | p.296 req.form/ req.remote_addr /req.user_agent; Form data, Remote_addr, User_agent, Results; View LOG|
| 7_web | `Wicker database. Setting up DB-API in Python`  | DB-API, MySQL, MariaDB  | :rotating_light:  :scream: :x:| 
| 8 | `A little about the classes. Behavior and State Abstraction`  | OOP+functional+procedural; self; magical methods «__ _init_ __» 🔮 | p.368 info about classes; behavior - function, state - variables, :small_orange_diamond: objects have common behavior but not state; when an object is created, the values of all arguments passed to the class get into the method «__ _init_ __» 🔮 |
| 9_web | `Context control protocol. Connection to instructions with ` |  import mysql.connector; class UseDatabase: def __ _init_ __ (self):, def __ _enter_ __ (self):, def __ _exit_ __ (self):; | |
| 10 | `Decorative functions. Packaging functions` | import Flask, session; secret_key; *args, **kwargs; from functools import wraps; :bell:@wraps; | DRY_DIE; **kwargs`keyword arguments`; |
| 11_web | `Handling exceptions. What to do if something goes wrong`  | try: except:; import sys; raise;  | p. 463 - all Exception(tree); Silence doesn't mean ignore; None=null|
| 11 3/4 | `A little about the rich stream. Waiting processing ` | from threading import Thread; :bell:@copy_current_request_context  | p.507 @ |
| 12 | `Extended iterations. Crazy Cycles`  | import csv; csv.reader(data); csv.DictReader(data); line.strip().split(','); yield | Comma-Separated Values; pretty-printing; generators: list, dict, sets |
| A | `Installation. Installing Python` |  brew install python3 | :white_check_mark: |
| B | `Righton be de. Web Application Deployment`   |  PythonAnywhere | :negative_squared_cross_mark: |
| C | `Top 10 topics we didn't cover. There is always something to learn`  |  venv/virtualenv; :bell: @staticmethod: @classmethod: @property:; __ slots __:; sorted; multiprocessing:; asyncio:; async/await   | `async` can be used before for, with, and def, `await` can be used before (almost) any other code. |
| C | | from turtle import * ; py.test, doctest:, unittest:,   | turtle :diamond_shape_with_a_dot_inside:|
| D | `Top 10 projects we didn't watch. Additional tools, libraries and modules`  | «ipython», «ptpython»; IDLE: Eclipse, PyCharm, WingWare, Jupyter Notebook | data science: bokeh, matplotlib/seaborn, numpy, scipy, pandas, scikit-learn; Django; Scraping web data: Beautiful Soup, Scrapy |
| E | `Join.Community Python`  | import this; BDFL: Benevolent Dictator for Life, PSF: The Python Software Foundation, PyCon, PyLadies | Come for the language, stay for the community |


