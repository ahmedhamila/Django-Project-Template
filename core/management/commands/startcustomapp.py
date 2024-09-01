import os
import shutil

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a new Django app with a custom structure"

    def add_arguments(self, parser):
        parser.add_argument("app_name", type=str, help="Name of the new app")
        parser.add_argument(
            "--src", action="store_true", help="Create the app inside the src directory"
        )

    def handle(self, *args, **kwargs):
        app_name = kwargs["app_name"]
        src_flag = kwargs["src"]
        template_dir = os.path.join(os.getcwd(), "app_template")

        # Determine the destination directory
        if src_flag:
            destination_dir = os.path.join(os.getcwd(), "src", app_name)
        else:
            destination_dir = os.path.join(os.getcwd(), app_name)

        if os.path.exists(destination_dir):
            self.stdout.write(self.style.ERROR(f'App directory "{app_name}" already exists!'))
            return

        shutil.copytree(template_dir, destination_dir)
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created new app "{app_name}" with custom structure')
        )
