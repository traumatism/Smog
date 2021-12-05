from smog.abstract.command import CommandBase
from smog.logger import Logger

class Run(CommandBase):

    command = "run"
    description = "Run the selected module"
    aliases = ["execute", "start"]

    _arguments = {"-t", "--threads", "-d", "--debug-threads"}

    def init_arguments(self):
        self.parser.add_argument("-t", "--threads", type=int, default=5, help="Number of threads to run.", metavar="<value>")
        self.parser.add_argument("-d", "--debug-threads", action="store_true", help="Debug threads.")

    def execute(self):
        if self.shell.selected_module is None:
            return Logger.warn("No module selected.")

        self.shell.selected_module(
            self.database, self.arguments.threads, self.arguments.debug_threads
        ).execute()

        Logger.success("Done.")
