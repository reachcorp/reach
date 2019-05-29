import git
import os

repo_pull_failed = []


def dl_module_from_github(module_name, repo_url="."):
    print ("### Get module " + module_name)
    if repo_url == ".":
        print("(module existant) -> git pull ...")
        try:
            git.cmd.Git(".").pull("--rebase")
            print("succes")
        except:
            repo_pull_failed.append(module_name)
            print("!!! pull failed !!!")
        return
    if not os.path.exists(module_name):
        print("(nouveau module) -> git clone ...")
        git.Repo.clone_from(repo_url, module_name)
        print("succes")
    else:
        print("(module existant) -> git pull ...")
        try:
            git.cmd.Git(module_name).pull("--rebase")
            print("succes")
        except:
            repo_pull_failed.append(module_name)
            print("!!! pull failed !!!")


### GET ALL MODULES FROM GITHUB
# start with 'reach' ...
dl_module_from_github("reach")
# ... then others
dl_module_from_github("housthon", "https://github.com/reachcorp/housthon.git")
dl_module_from_github("comparathon", "https://github.com/reachcorp/comparathon.git")
dl_module_from_github("scrapython", "https://github.com/reachcorp/scrapython.git")
dl_module_from_github("twitthon", "https://github.com/reachcorp/twitthon.git")
dl_module_from_github("NERdetecthon", "https://github.com/reachcorp/NERdetecthon.git")
dl_module_from_github("colissithon", "https://github.com/reachcorp/colissithon.git")
dl_module_from_github("googlethon", "https://github.com/reachcorp/googlethon.git")
dl_module_from_github("geotrouvethon", "https://github.com/reachcorp/geotrouvethon.git")
dl_module_from_github("travelthon", "https://github.com/reachcorp/travelthon.git")

if len(repo_pull_failed) > 0:
    print("#############################################")
    print("La mise a jour des modules suivants a echouee : ")
    for repo_name in repo_pull_failed:
        print(" - " + repo_name)
