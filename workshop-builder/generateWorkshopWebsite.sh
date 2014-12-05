#!/bin/bash
set -e

genDir=`mktemp -d -t workshop-galen.XXXXXXX`

builderDir=`pwd`


cd ..
projectDir=`pwd`
git tag -n99 > $genDir/git-tags


function takeTagDescription() {
    shift
    echo $@
}

cat ${genDir}/git-tags | cut -d '"' -f 2 | while read tagInfo; do
    tagName=`echo "$tagInfo" | awk '{print $1;}'`
    tagDescription=`takeTagDescription $tagInfo`

    git checkout $tagName
    versionFolder=${genDir}/${tagName}
    mkdir ${versionFolder}
    cp -r website ${versionFolder}/website
    cp -r galen-tests ${versionFolder}/galen-tests
    echo "Copied website and test code for version $tagName"

    
done

git checkout master

cd ${builderDir}

mkdir ${genDir}/overview
galen test . -D"workshop.all.versions=${genDir}"
cp -r ${builderDir}/template/* ${genDir}/.
rm ${genDir}/index.tpl.html

echo "Everything is in: ${genDir}"
