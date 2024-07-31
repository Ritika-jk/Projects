import requests
from bs4 import BeautifulSoup

def scrape_courses(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  course_containers = soup.find_all('div', {'class': 'course-item'})  # Replace with appropriate class

  courses = []
  for container in course_containers:
    title = container.find('h3').text.strip()
    link = container.find('a')['href']
    courses.append({'title': title, 'link': link})

  return courses

def print_courses(courses):
  for course in courses:
    print(f"{course['title']}: {course['link']}")

if __name__ == '__main__':
  beginner_url = 'https://www.geeksforgeeks.org/python-programming-language/'  # Replace with actual beginner URL
  intermediate_url = 'https://www.geeksforgeeks.org/intermediate-python-programming/'  # Replace with actual intermediate URL
  advanced_url = 'https://www.geeksforgeeks.org/advanced-python-programming/'  # Replace with actual advanced URL

  beginner_courses = scrape_courses(beginner_url)
  intermediate_courses = scrape_courses(intermediate_url)
  advanced_courses = scrape_courses(advanced_url)

  print(" beginner level: https://www.geeksforgeeks.org/python-programming-language-tutorial/")
  print_courses(beginner_courses)
  print("\n intermidiate level: https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/?ref=ghm")
  print_courses(intermediate_courses)
  print("\n advanced level: https://www.geeksforgeeks.org/advanced-python-tutorials/?ref=ghm")
  print_courses(advanced_courses)
