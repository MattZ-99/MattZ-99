import os

user = os.getenv("USER")
token = os.getenv("API_TOKEN")
exclude_lang = os.getenv("EXCLUDE_LANG")
exclude_repo = os.getenv("EXCLUDE_REPO")
top_x_language = 5

template_file = "template.md"
output_file = "README.md"

if not user:
    user = ""

if not token:
    token = ""

if exclude_lang:
    exclude_lang = exclude_lang.split(":")
else:
    exclude_lang = []
for i in range(len(exclude_lang)):
    exclude_lang[i] = exclude_lang[i].lower()

if exclude_repo:
    exclude_repo = exclude_repo.split(":")
else:
    exclude_repo = []
for i in range(len(exclude_repo)):
    exclude_repo[i] = exclude_repo[i].lower()
