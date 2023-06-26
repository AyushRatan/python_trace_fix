from bs4 import BeautifulSoup


file_path = "./templates/home.html"
with open(file_path, 'r') as file:
    html_content = file.read()

# parce age related html
parse_label = "age"
parse_type = "input"
soup = BeautifulSoup(html_content, 'html.parser')
soup = soup.prettify()

with open("./templates/modified_home.html","w") as file2:
    file2.write(soup)

with open("./templates/modified_home.html","r") as file3:
    new_html_content = file3.read()

soup2 = BeautifulSoup(new_html_content, "html.parser")

parced_html = soup2.find(parse_type, attrs={'name': parse_label}).find_parent('div')
# parced_html = soup.find(parse_type, attrs={'name': parse_label})

print(f'\n ----- html part realted to {parse_label} -------- \n')
print(parced_html)

with open('parsed_html.txt', 'w') as file:
    file.write(str(parced_html))
