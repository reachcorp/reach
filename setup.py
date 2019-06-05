import git
import os

repo_pull_failed = []

path_to_reach = ""

def dl_module_from_github(module_name, repo_url=".", directory_yml = ""):
    global path_to_reach
    print ("### Get module " + module_name)
    if repo_url == ".":
        print("(module existant) -> git pull ...")
        try:
            git.cmd.Git(".").pull("--rebase")
            path_to_reach = os.getcwd()
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
        #create link to reach ".env" file:
        try:
            reach_env = os.path.join(path_to_reach, "docker", "compose", ".env")
            if directory_yml == "":
                dest_env = os.path.join(module_name, "docker", ".env")
            else:
                dest_env = os.path.join(module_name, directory_yml, ".env")
            os.symlink(reach_env, dest_env)
        except:
            # le lien existe déjà, on ne fait rien
            pass

### GET ALL MODULES FROM GITHUB
# start with 'reach' ...
dl_module_from_github("reach")
# ... then others
dl_module_from_github("housthon", "https://github.com/reachcorp/housthon.git")
dl_module_from_github("comparathon", "https://github.com/reachcorp/comparathon.git")
dl_module_from_github("scrapython", "https://github.com/reachcorp/scrapython.git")
dl_module_from_github("twitthon", "https://github.com/reachcorp/twitthon.git")
dl_module_from_github("nerdetecthon", "https://github.com/reachcorp/nerdetecthon.git", "src/main/docker")
dl_module_from_github("colissithon", "https://github.com/reachcorp/colissithon.git")
dl_module_from_github("googlethon", "https://github.com/reachcorp/googlethon.git")
dl_module_from_github("geotrouvethon", "https://github.com/reachcorp/geotrouvethon.git")
dl_module_from_github("travelthon", "https://github.com/reachcorp/travelthon.git")

if len(repo_pull_failed) > 0:
    print("#############################################")
    print("La mise a jour des modules suivants a echouee : ")
    for repo_name in repo_pull_failed:
        print(" - " + repo_name)
else:
    print("#############################################")
    print("Mise a jour effectuee avec succes !")
