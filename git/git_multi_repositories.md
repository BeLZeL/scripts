#================================#
# Git with multiple repositories #
#================================#



#------------------------------------------------------------------------------
# Checkout all repositories

# Conf
URL=gogs@gogs:user
list_of_repositories=$(ssh gogs@gogs "list.sh")
dir=/backups/all_gits/

# Script
cd $dir
for r in $list_of_repositories
do
    echo "Checkout $r"
    git clone -n $URL/$r --depth 1 $dir/$r
done


#------------------------------------------------------------------------------
# Checkout just a file

# Conf
URL=gogs@gogs:user
list_of_repositories=$(ssh gogs@gogs "list.sh")
dir=/backups/gits/
#file=conanfile.py
file=.gitmodules

# Script
cd $dir
for r in $list_of_repositories
do
    git clone -n $URL/$r --depth 1 $dir/$r
    cd $dir/$r
    git checkout HEAD $file
    cd $dir
    cat $dir/$r/$file > ${dir}/${r}_${file}
    rm -fr $dir/$r
done
find $dir -name "*${file}" -size 0 | xargs rm



#------------------------------------------------------------------------------
# List of branches

# Conf
URL=gogs@gogs:user
list_of_repositories=$(ssh gogs@gogs "list.sh")
dir=/backups/gits/

# Script
cd $dir
for r in $list_of_repositories
do
    git clone -n $URL/$r --depth 1 $dir/$r
    cd $dir/$r
    git ls-remote --heads 2>/dev/null | sed 's|.*refs/heads/||g' | grep -v master > ${dir}/${r}_branches
    cd $dir
    rm -fr $dir/$r
done
find $dir -name "*_branches" -size 0 | xargs rm



#------------------------------------------------------------------------------
# List of branches (merged or not)

# Conf
URL=gogs@gogs:user
list_of_repositories=$(ssh gogs@gogs "list.sh")
dir=/backups/gits/

# Script
cd $dir
for r in $list_of_repositories
do
    git clone -n $URL/$r $dir/$r
    cd $dir/$r
    git branch -r --merged origin/master | grep -v "origin/master" > ${dir}/${r}_yes_merged
    git branch -r --no-merged origin/master                        > ${dir}/${r}_no_merged
    cd $dir
    rm -fr $dir/$r
done
find $dir -name "*_merged" -size 0 | xargs rm



#------------------------------------------------------------------------------
# Update all repositories

# Conf
URL=gogs@gogs:user
list_of_repositories=$(ssh gogs@gogs "list.sh")
dir=/backups/all_gits/

# Script
for subdir in $list_of_repositories
do
    cd $dir/${subdir}
    echo "Update ${subdir%.git}"
    git pull --rebase
done
