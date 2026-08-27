import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

base_path = "/"
if len(sys.argv) > 0:
    base_path = sys.argv[0]

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main() -> None:
    print("Deleting docs directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(
        base_path,
        dir_path_content,
        template_path,
        dir_path_public,
    )


main()
