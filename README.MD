# Repository for CIDM 5310 
## Business Intelligence and Decision Support Systems 

### Summer 2021

## Git

__Initialize__
`git init`

__Git ignore__
do not track list in gitignore

__Git Add__
Add files for tracking

`git add -A`
`git init` # to reinitialize 
-- `A` next to file name mean added but not commited

__Git Commit__
Commit recent tracked changes 
-- `-m` means to add message 

__setup up Remote __
`git remote add origin https://github.com/osatooh/CIDM5310.git`




__push to remote__
push recent commit to remote
`git push -u origin master`
-- u means upstream

## Encountered Error: error when trying to push to remote 
--  remote option was try to connect to old git hub repo
I had to use set url option  below 
`  git remote set-url origin https://github.com/osatooh/CIDM5310.git `
### error message:  ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/osatooh/C6330Dev.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
