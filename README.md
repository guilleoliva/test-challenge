
## Testing QA Automation - Pet store
### Pre-requisites
- Install Python 3.10: https://www.python.org/downloads/release/python-3100/
- Install Poetry: https://python-poetry.org/docs/
- On Windows if you need Microsoft Visual C++ 14.0 https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170
- Google Chrome pre-installed 


### Installing dependencies and activate poetry environment 
#### (RECOMMENDED)
 ```
 $ poetry install
 $ poetry shell
 ```

#### (ALTERNATIVE) through Virtualenv
If you are struggling with poetry you can prepare your dependencies using virtualenv
 ```
 $ python3 -m pip install --user virtualenv
 $ virtualenv aureum-venv
 $ source ./aureum-venv/bin/activate
 $ python3 -m pip install -r requirements.txt
 ```

### Local tests execution:
Execute the following command, replacing <TAG> by any scenario tags you would like to execute, the environment by default is dev but if you want to specify it, you can use the env parameter inside the command line (default: dev), browser is set to chrome by default. 

This framework also allows the user to run in headless mode to run as headless run your command with the parameter "-D headless_browser"
```
behavex -t <TAG> -D browser=chrome -D env=<qa or dev>

Example: behavex -t SMOKE -D headless_browser
```

### Report
After running your features/scenarios, you have available inside the folder /output an HTML file called "report.html" there you have all the evidences, steps and, screenshots (only in case of failures).

