import unittest
from convert import convert


class TestConvert(unittest.TestCase):
    def testEmptyJsonParse(self):
        generated = convert.parse(convert._load_json_files("./jsonSamples/minimal.json")[0])

    def testGlossaryJsonParse(self):
        generated = convert.parse(convert._load_json_files("./jsonSamples/Glossary.json")[0])

        generated = convert.generate("Test", ["cs"], generated)
        for f in generated:
            print "".join(f["content"])