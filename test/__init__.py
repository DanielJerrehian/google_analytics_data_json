import unittest
from dotenv import load_dotenv


def startTestRun(self):
    load_dotenv(".env")

unittest.result.TestResult.startTestRun = startTestRun