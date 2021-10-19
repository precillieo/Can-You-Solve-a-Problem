To start contributing you need to [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on your machine.


## First step

The first step is to search for an issue with the label goodfirstissue (they are generally beginner friendly). 
After that you need read the issue description and try to understand the problem in order to solve it. After realizing that you are able to resolve that issue, you need to send a signal with a message that will pick up the issue.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

## Second step

Fork the repository by clicking the Fork button. 

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

After the fork is done, the next step is to clone the remote repository (forked) to your machine. Go to Code bottom, copy the path and write in the terminal the command:

```
git clone git@github.com:YOUR-USER-NAME/NAME-REPO.git 
```

obs: switch YOU-USER-NAME and NAME-REPO to your GitHub username and the name of the repository you want to clone.

Go to the directory where you cloned the repository (with command line in terminal window) and create a new branch with the command:


```
git checkout -b add-NAME-BRANCH
```

obs: switch NAME-BRANCH to name of your branch

## Third step

Make the necessary changes to resolve the issue, save the files and send them to stage area with the command:

```
git add FILENAME
```

obs: switch FILENAME to the name of the file you changed or use 
```
git add . 
```

to add all files you changed. Commit with the command:

```
git commit -m "MESSAGE"
```

obs: switch MESSAGE to a short identification

Make a push with command

```
git push origin add-NAME-BRANCH
```

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />


Go to the (forked) directory on GitHub and click Compare and Pull Request. Make sure there are no conflicts and make your first Pull Resquest!

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />
For more information read this article [Making An Open Source Contribution on Github](https://link.medium.com/W6Ma8PcDRab)
To guide you through the process or complete this [Git and GitHub Crash Course](https://youtu.be/SWYqp7iY_Tc) if you are an absolute beginner
