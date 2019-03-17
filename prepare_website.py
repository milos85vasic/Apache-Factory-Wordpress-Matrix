from configuration import *
from Setup.Tools.commands import *
from Setup.Tools.configuration import *

import sys


def prepare():
    url = sys.argv[2]
    account = sys.argv[1]
    print("Preparing Wordpress installation: " + account + ", " + url)
    steps = [
        concatenate(
            mkdir(content_dir_name),
            cd(content_dir_name),
            wget(download_url),
            extract(download_url)
            #,rm(downloaded_file)
        )
    ]

    run(steps)


if __name__ == '__main__':
    prepare()
