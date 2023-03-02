#!/bin/bash
# Bump a new release. Handling is the same as with poetry version,
# but also takes care of __init__.py:version, git tag, ...
# Then creating and pushing a new tag so that the release pipeline gets started on GitHub.

if [[ -n "$(git status --porcelain | grep -v ' M CHANGELOG.md')" ]] ; then
  echo "error: git repository is not clean (except of CHANGELOG.md), please commit and/or stash all changes (except of CHANGELOG.md) before running this script."
  exit 1
fi

if [[ $# != 1 ]] ; then
  version_bump="not_implemented"
else
  version_bump=$1
fi

case $version_bump in
  major|minor|patch)
    ;;
  *)
    echo "ERROR: Please provide the version desired bump as 'major', 'minor' or 'patch'" >&2
    exit 1
esac

old_version=`poetry version | sed 's/demo-patrikspiess \(.*\)/\1/'`

poetry version $version_bump

new_version=`poetry version | sed 's/demo-patrikspiess \(.*\)/\1/'`

if [[ -n `grep "## \[$new_version\]" ./CHANGELOG.md` ]] ; then
  echo "New version would be $new_version. Is this ok? [y/N]"
  read ok
else
  echo "ERROR: New version not found in the CHANGELOG.md, please update CHANGELOG.md first."
  ok='N'
fi

case $ok in
  y)
    ;;
  *)
    echo "aborting..."
    git restore pyproject.toml
    exit 1
esac

echo 'Writing new version to "demo_patrikspiess/__init__.py"...'
sed -i "s/$old_version/$new_version/g" demo_patrikspiess/__init__.py

git add pyproject.toml
git add demo_patrikspiess/__init__.py
git add CHANGELOG.md

echo 'Committing version bump...'
git commit -m ":bookmark: Commit version v$new_version"
echo 'Pushing version bump...'
git push


echo 'Create and push tag...'
git tag -a "v$new_version" -m "Version v$new_version"
git push origin "v$new_version"

echo "Done. Version $new_version is now released on GitHub (and soon on PyPi, etc.)."
echo -e "Congratulations!"