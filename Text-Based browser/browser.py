import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore


class Browser:
    commands = {"exit", "back"}
    tags = ["p", 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']

    def __init__(self):
        self.history = list()
        self.is_run = True
        self.files = set()
        self.path_to_file = "" if len(sys.argv) != 2 else sys.argv[1]

    @staticmethod
    def check_url(site: str):
        url = site if site.startswith("https://") else "https://" + site
        return url

    @staticmethod
    def create_dir(dir_name):
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

    def do_command(self, command):
        if command == "exit":
            self.is_run = False
        elif command == "back":
            if len(self.history) > 1:
                self.history.pop()
                data = self.read_data_from_file(self.history[-1])
                print(data)

    @staticmethod
    def get_data_by_url(url):
        url = Browser.check_url(url)
        req = requests.get(url)
        req.encoding = 'utf-8'
        return req.text

    def read_data_from_file(self, file_name):
        path = self.path_to_file + "/" + file_name + ".txt"
        data = open(path, "r").read()
        return data

    @staticmethod
    def clean_html_data(html_data):
        some = BeautifulSoup(html_data, "html.parser")
        clean_data = "\n".join(
            [Fore.BLUE + line.get_text().strip() + Fore.RESET
             for line in some.find_all(Browser.tags)]
        )
        return clean_data

    def write_data_in_file(self, site, data):
        Browser.create_dir(self.path_to_file)
        file_name = ".".join(site.split(".")[:-1])

        self.history.append(file_name)
        self.files.add(file_name)

        file_path = self.path_to_file + "/" + file_name + ".txt"
        with open(file_path, "w") as file:
            file.write(data)

    def run(self):
        while self.is_run:
            site = input()

            if site in Browser.commands:
                self.do_command(site)
                continue
            if site not in self.files and site.count(".") == 0:
                print("Error: Incorrect URL\n")
                continue
            if site in self.files:
                print(self.read_data_from_file(site))
                continue

            url_data = Browser.get_data_by_url(site)
            data = Browser.clean_html_data(url_data)
            print(data)

            if len(sys.argv) == 2 and site not in self.files:
                self.write_data_in_file(site, data)


if __name__ == "__main__":
    browser = Browser()
    browser.run()
