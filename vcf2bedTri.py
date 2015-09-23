#!/usr/bin/env python

import os
import sys
import subprocess
__author__ = 'xiuchengquek'



class vcfToTri:

    def __init__(self, input, output):
        self.input = input
        self.output = output


    def check_mutation_type(self, ref, alt):
        mutation_type = 'snp'
        if len(ref) > len(alt):
            mutation_type = 'del'
        elif len(ref) < len(alt):
            mutation_type = 'ins'
        return mutation_type

    def vcf_to_bed(self, line):
        fields = line.split('\t')
        chr = fields[0]
        pos = int(fields[1])
        snp_id = fields[2]
        ref = fields[3]
        alt = fields[4]
        filter = fields[6]
        mut_type = self.check_mutation_type(ref, alt)

        if mut_type is None:
            return None
        else:
            bed_name = "%s_%i_%s_%s_%s_%s_%s" % (chr, pos, snp_id, ref, alt, filter, mut_type)
            bed_line = [chr, pos - 1, pos + 1, bed_name, 0  ,'+' ]
            bed_line = [ str(x) for x in bed_line]
            return "\t".join(bed_line )
            return None

    def convert(self):
        fh_out = open(self.output, 'w+')
        with open(self.input, 'r') as f:
            for line in f:
                if not line.startswith('#'):
                    bed_line = self.vcf_to_bed(line)
                    fh_out.write("%s\n" % bed_line)



class snpOnly(vcfToTri):
    def check_mutation_type(self, ref, alt):
        if len(ref) == len(alt):
            return 'snp'
        else:
            return None


if __name__ == '__main__':
    input_vcf = sys.argv[1]
    output_bed = sys.argv[2]
    snp_obj = snpOnly(input_vcf, output_bed)
    snp_obj.convert()








