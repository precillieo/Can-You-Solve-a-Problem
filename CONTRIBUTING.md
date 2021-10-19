To start contributing you need to [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on your machine.


* The first step is to search for an issue with the label goodfirstissue (they are generally beginner friendly).

* After that, the second step is to read the issue description and try to understand the problem in order to solve it.

* After realizing that you are able to resolve that issue, the third step is to signal with a message that you will take the issue and.

*Fork the repository by clicking the Fork button.

* After the fork is done, the fourth step is to clone the remote repository (forked) to your machine in the terminal with the command:
git clone git@github.com:YOUR-USER-NAME/NAME-REPO.git 

obs: switch YOU-USER-NAME and NAME-REPO to your GitHub username and the name of the repository you want to clone.

* Go to the directory where you cloned the repository (with command line in terminal window) and create a new branch with the command:
git checkout -b add-NAME-BRANCH

obs: switch NAME-BRANCH to name of your branch

* Make the necessary changes to resolve the issue, save the files and send them to stage area with the command:
git add FILENAME

obs: switch FILENAME to the name of the file you changed or use git add . to add all files you changed.

* Commit with the command:
git commit -m "MESSAGE"

obs: switch MESSAGE to a short identification

* Make a push with command
git push origin add-NAME-BRANCH

* Go to the (forked) directory on GitHub and click Compare and Pull Request. Make sure there are no conflicts and make your first Pull Resquest!

For more information read this article [Making An Open Source Contribution on Github](https://link.medium.com/W6Ma8PcDRab).
To guide you through the process or complete this [Git and GitHub Crash Course](https://youtu.be/SWYqp7iY_Tc) if you are an absolute beginner.
