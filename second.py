from bs4 import BeautifulSoup
import requests
import time
print("Put some Known skills")
knowm_skill=input('>')
print(f'Filtring jobs based on {knowm_skill}')
def find_jobs():
    html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text
    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    # print(soup)
    jobs = soup.find_all('div', class_='srp-listing clearfix')

    for index, job in enumerate(jobs):
            job_experience = job.find('div',class_='srp-exp').text
            if  job_experience in job_experience:
                    
                    company_name = job.find('div',class_='srp-job-heading').text
                    skills = job.find('div',class_='srp-keyskills').text.replace(' ',',')
                    company_loaction=job.find('div',class_='srp-loc').text
                    more_info = job.find('a')['href']  
                    if knowm_skill in skills:    
                        with open(f'C:\\Users\\user\\Desktop\\Pyhon\\bs4\\post\\{index}.txt','w') as f:
                            f.write(f'company name: {company_name.strip()}\n')
                            f.write(f'Skills required: {skills.strip()}\n')
                            f.write(f'Location: {company_loaction}\n\n')
                            f.write(f'More info: {more_info}')
                        print(f'File Saved: {index}')
            else:
                print("No jobs found")

if __name__ == '__main__':
      while True:
            find_jobs()
            time_wait = 10
            print(f'Time wait {time_wait} Minutes...')
            time.sleep(time_wait*60)