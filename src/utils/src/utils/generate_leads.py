import pandas as pd
import re
import selenium

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from time import sleep
from time import time
from random import randint
from fun_with_words.array_string_manipulation.src.urlify import urlify


# region Helper Functions
def clean_titles(title):
    title = str(title.split(" "))


# endregion


def generate_jobs(location, title, num_jobs=25):
    """Collect job data from LinkedIn using Beautiful Soup and Selenium"""
    # region Instantiating Selenium Driver
    # A note on the url: '&f_E=2%2C3' is the parameter for selecting entry and associate level jobs
    url = (
        "https://www.linkedin.com/jobs/search/?f_TPR=r604800&f_E=2%2C3"
        f"&keywords={urlify(title)}&location={urlify(location)}&sortBy=DD"
    )

    # Use selenium to open up new chrome window to generated url.
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    driver = webdriver.Chrome(
        options=options, executable_path="C:/bin/chromedriver.exe"
    )
    driver.get(url)
    sleep(3)
    action = ActionChains(driver)

    # Continue to fetch more jobs
    i = 2
    while i <= num_jobs / 25:
        driver.find_element_by_xpath("/html/body/main/div/section/button").click()
        i += 1
        sleep(5)

    # endregion

    # region Use Beautiful soup to parse webpage and find all job postings
    src = driver.page_source
    html = BeautifulSoup(src, "lxml")
    jobs = html.find("ul", class_="jobs-search__results-list")
    jobs.prettify()
    jobs = jobs.find_all("li")
    print(jobs)

    print(
        "\n____________________\n____________________\n",
        "\n____________________\n____________________\n"
        f"Currently scraping {len(jobs)} {title} jobs located in {location}.",
    )
    # endregion

    # region instantiate and fill columns for panda data store
    links, companies, locations, titles, posted, description, industries, seniority = (
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    )

    # Iterate through jobs, appending data to respective columns
    for job in jobs:
        print(job)
        link = job.a["href"]
        # id = re.findall(r'(?!-)([0-9]*)(?=\?)', id)[0]
        links.append(link)

        company = job.find("img")["alt"]
        companies.append(company)

        location = job.find("span", class_="job-result-card__location").text
        locations.append(location)

        title = job.find("span", class_="screen-reader-text").text
        titles.append(title)

        # print(job.time['datetime'])
        # date = job.select_one('time')['datetime']
        # posted.append(date)

    # Loop through jobs and click on them to grab description & seniority
    for i in range(1, len(links) + 1):
        """NOT CURRENTLY FUNCTIONAL"""
        try:
            print("Gobbledy Gook")
            xpath = f"html/body/main/div/section/ul/li[{i}]/img"
            driver.find_element_by_xpath(xpath).click()
            sleep(3)

            desc_path = "/html/body/main/section/div[2]/section[2]/div"
            desc = driver.find_element_by_xpath(desc_path).text
            print(desc)
            description.append(desc)
        except:
            print("Something went seriously awry")
        finally:
            sleep(3)
            print(
                "\n____________\n\n links: ",
                link,
                "\n____________\n\n companies: ",
                companies,
                "\n____________\n\n locations: ",
                locations,
                "\n____________\n\n jobs: ",
                titles,
                "\n____________\n\n descriptions: ",
                description,
                "\n____________\n",
            )

    driver.quit()
    # endregion

    # region create Pandas dataframe and append columns to df.
    print(
        "link length: ",
        len(links),
        "\n comp length: ",
        len(companies),
        "\n loc length: ",
        len(locations),
        "\n job length: ",
        len(titles),
        "\n desc length: ",
        len(description),
    )

    job_data = pd.DataFrame(
        {
            "Link": links,
            "Company": companies,
            "Location": locations,
            "Job Title": titles,
            # 'Date Posted': posted,
            "Description": description,
        }
    )
    job_data["Description"] = job_data["Description"].replace("\n", " ")

    print(job_data)
    # endregion


generate_jobs("New York", "Data Analyst")
