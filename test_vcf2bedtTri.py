__author__ = 'xiuchengquek'


import unittest

from vcf2bedTri import snpOnly, vcfToTri





class vcf2bedtri(unittest.TestCase):

    def setUp(self):
        self.vcf_string =  '1\t100\t.\tt\tc\t100\tPASS\tAC;;;;;\tGT;;;;\n'
        self.insertion = '1\t100\t.\tt\tca\t100\tPASS\tAC;;;;;\tGT;;;;\n'
        self.bed_string = '1\t99\t101\t1_100_._t_c_PASS_snp\t0\t+'




    def test_vcf_to_bed(self):
        snpObj = snpOnly('input', 'outpput')
        self.assertEqual(snpObj.vcf_to_bed(self.vcf_string), self.bed_string)
        self.assertIsNone(snpObj.vcf_to_bed(self.insertion))





















