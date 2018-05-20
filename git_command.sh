# prepare   
    git config --global user.name "Your Name"
    git config --global user.email "email@example.com"
    ssh-keygen -t rsa -C "youremail@example.com"

# file operate
    #可以添加一个或多个
    git add <file1> <file2>...

    #添加所有修改的和新添加的
    git add .
    #另一种写法
    git add -A

    #添加指定目录
    git add <dirname>

    #由暂存区恢复到工作区（发现提交错了，退回一步）
    git reset HEAD <file> 

    #恢复上一次add提交的所有file
    git reset HEAD

    #撤销修改操作，恢复到修改之前的，撤销add后位于工作区下进行的
    git checkout -- <file>
    
    #回退到上一个commit节点， 代码也发生了改变，变成上一次的
    git reset –hard commit_id    
    
    #回退到上一个commit节点， 代码变更保留，再提交可以直接commit
    git reset commit_id
    
    #撤销某一次commit(撤销会当做一次新的提交，之前commit仍在版本控制里)
    git revert HEAD
    git revert HEAD^ 
    git revert commit-id

    #删除文件,并将文件放入暂存区
    git rm <file1> <file2>
    #改文件名，并将修改后的文件放入暂存区
    git mv <file-original> <file-rename>

    #提交暂存区的所有文件(后面的message不可缺少)
    git commit -m <message>
    #提交暂存区的指定文件
    git commit <file1> <file2> -m <message>

#git branch operate
    # 列出所有本地分支
    git branch

    #列出所有远程分支
    git branch -r

    #列出所有本地分支和远程分支
    git branch -a

    # 新建一个分支，并切换到该分支
    git checkout -b [branch]

    #切换到指定分支，并更新工作区
    git checkout [branch-name]

    #从远程分支检出指定分支
    git clone -b <branchname> <master>

    # 合并指定分支到当前分支（主分支合并自定义分支）
    git merge [branch]
    #pick 指定分支的某一次提交到当前分支
    git cherry-pick <commit id>

    # 删除分支
    git branch -d [branch-name]

    #删除远程分支
    git push origin --delete [branch-name]
    git branch -dr [remote/branch]

    # 显示有变更的文件
    git status

    #显示当前分支的版本历史
    git log
    
git diff  filepath 工作区与暂存区比较

git diff HEAD filepath 工作区与HEAD ( 当前工作分支) 比较

git diff --staged 或 --cached  filepath 暂存区与HEAD比较

git diff branchName filepath  当前分支的文件与branchName 分支的文件进行比较

git diff commitId filepath 与某一次提交进行比较

git remote -v  查看当前远程仓库地址

git remote rm origin   删除当前连接的远程仓库
git remote add origin [url]  添加新的远程仓库地址
