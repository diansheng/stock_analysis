# stock_analysis

# set up

0. install python, pip and virtualenv in sequence. It varies across OS.
1. create virtualenv by `virtualenv env_name`
2. download the package, unzip and save in env_name. your folder structure should be like this.
    ```
    env_name
      |--bin
      |--lib
      |--include
      |--stock_analysis
        |--src
        |--data
        |--req.txt
        |--README.md
      |--pip-selfcheck.json
    ```
3. activate env by `cd env_name; source bin/activate`
4. install required packages by `pip install -r stock_analysis/req.txt`
5. that's it
