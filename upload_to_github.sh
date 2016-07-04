#!/usr/bin/env bash
source srpm
git tag ${CIRCLE_PROJECT_REPONAME}-${srpm_version}
git push --tags
github-release release -u ${CIRCLE_PROJECT_USERNAME} -r ${CIRCLE_PROJECT_REPONAME} --tag ${CIRCLE_PROJECT_REPONAME}-${srpm_version} --description "CircleCI ${CIRCLE_PROJECT_REPONAME} ${CIRCLE_BUILD_NUM} - ${CIRCLE_BUILD_URL}"
github-release upload -u ${CIRCLE_PROJECT_USERNAME} -r ${CIRCLE_PROJECT_REPONAME} --tag ${CIRCLE_PROJECT_REPONAME}-${srpm_version} --file ${srpm_filename} --name $(basename ${srpm_filename})
