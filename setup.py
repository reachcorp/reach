import os
import git

def dl_module_from_github(module_name, repo_url):
    print ("### Get module "+module_name)
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
            print("!!! pull failed !!!")


### GET ALL MODULES FROM GITHUB
dl_module_from_github("housthon","https://github.com/reachcorp/housthon.git")
dl_module_from_github("comparathon","https://github.com/reachcorp/comparathon.git")
dl_module_from_github("scrapython","https://github.com/reachcorp/scrapython.git")
dl_module_from_github("twitthon","https://github.com/reachcorp/twitthon.git")
dl_module_from_github("NERdetecthon","https://github.com/reachcorp/NERdetecthon.git")
dl_module_from_github("colissithon","https://github.com/reachcorp/colissithon.git")
