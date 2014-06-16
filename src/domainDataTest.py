'''
Created on Jun 14, 2014

@author: nelsoncs
'''
import unittest
import src.domainData
import src.parse

class TestDomainData(unittest.TestCase):


    def setUp(self):
        self.dd = src.domainData.DomainData("domain_track.conf")
        self.assertIsInstance( self.dd, src.domainData.DomainData  )

    def tearDown(self):
        pass

    def test_checkUrl(self):
        self.assertTrue(self.dd.checkUrl("dogs.com"), "dogs.com fail")
        self.assertFalse(self.dd.checkUrl("dogs.c"), "dogs.c fail")
        self.assertFalse(self.dd.checkUrl("dogs"), "dogs fail")
        self.assertFalse(self.dd.checkUrl(""), "empty url fail")
        
        for domain in self.dd.config.fileBuffer:
            self.assertTrue(self.dd.checkUrl(domain), "")
        
    def test__parseConfiguredData(self):
        #self.assert ( self.dd._parseConfiguredData(self.dd.config))
        pass  


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()