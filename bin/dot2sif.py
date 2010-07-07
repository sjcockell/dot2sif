from optparse import OptionParser
import re

def main(inf, outf, ints):
	p = re.compile('^\s+(\w+) -> (\w+) \[label=\"(.+)\"\,')
	fh = open(outf, 'w')
	with open(inf) as f:
	    for line in f.readlines():
			if line.find(' -> ') != -1:
				#node79153 -> node31061 [label="publishe
				m = p.search(line)
				if m:
					if ints:
						fh.write(m.group(1)+'\t'+m.group(3)+'\t'+m.group(2))
					else:
						fh.write(m.group(1)+'\t'+m.group(2))
	fh.close()
				

if __name__ == '__main__':
	parser = OptionParser(usage="Usage: %prog [options] infile.dot outfile.sif", 
		version="%prog 0.1")
	#switch for if interaction types are included in output
	parser.add_option("-i", "--int", dest="interactions",
	                  action='store_true', help="Include interaction types in output", default=False)
	(options, args) = parser.parse_args()
	if len(args) != 2:
		print 'Usage error, you need to define an infile and an outfile'
		parser.print_help()
	else:
		infile = args[0]
		outfile = args[1]
		main(infile, outfile, options.interactions)
