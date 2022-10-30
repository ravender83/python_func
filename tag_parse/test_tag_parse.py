import unittest
import tag_parse


class test(unittest.TestCase):
	
	def test_tag_parse(self):
		self.assertTrue(tag_parse.tag_parse('I0.0', 'iI'))
		self.assertTrue(tag_parse.tag_parse('I99999.0', 'iI'))
		self.assertTrue(tag_parse.tag_parse('I0.7', 'iI'))
		self.assertTrue(tag_parse.tag_parse('I99999.7', 'iI'))
		self.assertTrue(tag_parse.tag_parse('i0.0', 'iI'))
		self.assertTrue(tag_parse.tag_parse('i99999.0', 'iI'))
		self.assertTrue(tag_parse.tag_parse('i0.7', 'iI'))
		self.assertTrue(tag_parse.tag_parse('i99999.7', 'iI'))
		self.assertTrue(tag_parse.tag_parse('Q0.0', 'qQ'))
		self.assertTrue(tag_parse.tag_parse('Q99999.0', 'qQ'))
		self.assertTrue(tag_parse.tag_parse('q0.7', 'qQ'))
		self.assertTrue(tag_parse.tag_parse('q99999.7', 'qQ'))
		self.assertTrue(tag_parse.tag_parse('q0.0', 'qQ'))
		self.assertTrue(tag_parse.tag_parse('q99999.0', 'qQ'))
		self.assertTrue(tag_parse.tag_parse('q0.7', 'qQ'))
		self.assertTrue(tag_parse.tag_parse('q99999.7', 'qQ'))		
		self.assertFalse(tag_parse.tag_parse('Ii0.0', 'iIqQ'))
		self.assertFalse(tag_parse.tag_parse('I 0.0', 'iIqQ'))
		self.assertFalse(tag_parse.tag_parse('I0.8', 'iIqQ'))
		


if __name__ == '__main__':
	unittest.main()
