from github import Github
import os

# authentication through token
g = Github('GITHUB_TOKEN')

# owner of the GitHub account (replace with your own username)
owner = "YOUR_GITHUB_USERNAME"

# text of the license to add
with open('LICENSE', 'r') as f:
    license_text = f.read()

# loop through all the user's repositories and add the license
for repo in g.get_user(owner).get_repos():
    try:
        contents = repo.get_contents("")
        license_present = False
        for content_file in contents:
            if content_file.path.lower() == "license" or content_file.path.lower() == "license.md":
                license_present = True
                break
        if not license_present:
            repo.create_file("LICENSE", "Added license", license_text)
            print(f"License added to repository {repo.name}")
        else:
            print(f"The repository {repo.name} already has a license")
    except Exception as e:
        print(
            f"Error adding license to repository {repo.name}: {e}")
