from .utils import *
from .tsv import TSV

class Application(TSV):
    def __init__(self, argv):
        if 'applicationId' in argv:
            self.applicationId = argv['applicationId']
        if 'applicationType' in argv:
            self.applicationType = argv['applicationType']
        if ''
