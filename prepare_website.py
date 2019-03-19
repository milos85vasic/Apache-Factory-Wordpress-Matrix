from configuration import *
from Setup.Tools.commands import *
from Setup.Tools.configuration import *

import sys


def prepare():
    url = sys.argv[2]
    account = sys.argv[1]
    print("Preparing Wordpress installation: " + account + ", " + url)
    service_root = get_home_directory_path(account) + "/" + content_dir_name + "/" + url
    d_dir = service_root + "/" + content_dir_name
    d_file = d_dir + "/" + downloaded_file
    steps = [
        concatenate(
            cd(service_root),
            mkdir(content_dir_name)
        ),
        wget(download_url, destination=d_dir),
        extract(d_file, destination=d_dir),
        rm(d_file)
    ]

    run(steps)


if __name__ == '__main__':
    prepare()
