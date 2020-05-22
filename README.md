### How to PR to this repo
1. Fork this repo to your github account by clicking on the fork icon in this repo.
2. Clone the forked repo from terminal/git bash
```
git clone https://github.com/your github username/Learn.git
```
3. Checkout to new branch
```
git checkout -b your-name/your-branch-name
```
4. If you are a first year and learning Python, then go to [Juniors - 1st Year] folder and Create a folder in your name and add files(article) to it. 
If you are not a first year, Create a folder(in the root) in your name and add files(article) to it
5. Add and commit the changes
```
git add .
git commit -m "Your message here"
```
6. Push your branch to remote
```
git push origin your-name/your-branch-name
```
7. If link was shown in the last step, click on it and create a PR. Else, open the repo manually in browser and create a PR


## To sync your local repo with this repo
1. Add upstream url to url repo. (This comand is only once for a repo)
```
git remote add upstream https://github.com/Team-Tomato/Learn.git
```
2. Fetch the changes from oringinal repo.
```
git fetch upstream
```
3. Update the local repo(Master branch).
```
git checkout master
git merge upstream/master
```
