# URL License Adder GitHub
URL License Adder GitHub is a Python program that adds a license to all the repositories owned by a specified user on GitHub. It uses the PyGithub library to authenticate the user with a personal access token and to interact with the GitHub API.

## Installation
To use URL License Adder GitHub, you need to have Python 3 installed on your system. The program also requires the PyGithub library to be installed. You can install it by running the following command in your terminal or command prompt:
```shell
pip install -r requirements.txt
```

## Usage
To use URL License Adder GitHub, you need to provide a personal access token from GitHub in the program. Replace 'GITHUB_TOKEN' in the code with your own token. You also need to provide the name of the user whose repositories you want to add a license to by replacing 'YOUR_GITHUB_USERNAME' with the user's name.

Once you have made these changes, you can run the program by navigating to the directory where the program is stored and running the following command:
```shell
$ $ python3 url_license_adder.py
```
This will add the specified license to all the repositories owned by the specified user. If a repository already has a license, the program will skip that repository and move on to the next one.

After running the program, you can check the repositories on GitHub to see if the license has been added.
