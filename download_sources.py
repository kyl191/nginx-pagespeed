#!/usr/bin/python3
import os
import re
import requests


def download_file(url):
    out_file = os.path.join("SOURCES", url.rsplit("/")[-1])
    r = requests.get(url, stream=True)
    print("Downloading {} to {}".format(url, out_file))
    with open(out_file, "wb") as out:
        for chunk in r.iter_content(chunk_size=None):
            if chunk:
                out.write(chunk)


spec = "{}.spec".format(os.environ['CIRCLE_PROJECT_REPONAME'])
with open(spec, 'r') as f:
    for line in f.readlines():
        if line.startswith("Version:"):
            NGINX_VERSION = re.search("([0-9.])+", line).group()
        if line.startswith("%define nps_version"):
            NPS_VERSION = re.search("([0-9.])+", line).group()

ngx_files = [
    "https://nginx.org/download/nginx-{NGINX_VERSION}.tar.gz",
    "https://nginx.org/download/nginx-{NGINX_VERSION}.tar.gz.asc"
]
for f in ngx_files:
    download_file(f.format(NGINX_VERSION=NGINX_VERSION))

nps_files = [
    "https://github.com/pagespeed/ngx_pagespeed/archive/v{NPS_VERSION}-beta.zip",
    "https://dl.google.com/dl/page-speed/psol/{NPS_VERSION}-x64.tar.gz",
    "https://dl.google.com/dl/page-speed/psol/{NPS_VERSION}-ia32.tar.gz"
]
for f in nps_files:
    download_file(f.format(NPS_VERSION=NPS_VERSION))
