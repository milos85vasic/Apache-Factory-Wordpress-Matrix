from configuration import *
from Setup.Tools.commands import *
from Setup.configuration import *
from Setup.Tools.system_configuration import *
from Setup.Tools.configuration import *
from Matrices.configuration import *

import sys


def prepare():
    url = sys.argv[2]
    account = sys.argv[1]
    db_name = get_db_name(account, url)
    print("Preparing Wordpress installation: " + account + ", " + url)
    service_root = get_home_directory_path(account) + "/" + content_dir_name + "/" + url
    d_dir = service_root + "/" + content_dir_name
    d_file = d_dir + "/" + downloaded_file

    mysql_password = "undefined"
    mysql_port = default_port_mysql
    system_configuration = get_system_configuration()

    if account in system_configuration:
        if key_services in system_configuration[account]:
            if key_credentials in system_configuration[account][key_services]:
                if feature_mysql in system_configuration[account][key_services][key_credentials]:
                    mysql_password = system_configuration[account][key_services][key_credentials][feature_mysql]

    if account in system_configuration:
        if key_configuration_port_mysql in system_configuration[account]:
            mysql_port = system_configuration[account][key_configuration_port_mysql]

    mysql_full_path = get_home_directory_path(account) + "/" + mysql + "/"
    init_database = mysql_full_path + mysql_bin_dir + "/mysql --host=127.0.0.1 --port=" + mysql_port + \
                    " --user=root --password=" + mysql_password + " < "

    steps = [
        cp(
            matrices_dir_name + "/" + create_database_matrix_file,
            service_root + "/" + create_database_matrix_file
        ),
        python(
            "Toolkit/" + wipe_script,
            service_root + "/" + create_database_matrix_file,
            service_root + "/" + create_database_sql_file,
            config_matrix_db, db_name
        ),
        init_database + service_root + "/" + create_database_sql_file,
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
