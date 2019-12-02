import unittest
#import sys
# Append the parent parent dir to syspath to be able to read utils lib
#sys.path.append('..')

from ProgramAlarm import restore_state, format_input


class TestProgramAlarm(unittest.TestCase):

    def test_restore_state(self):
        inputs = { '1,0,0,0,99': '2,0,0,0,99',
                    '2,3,0,3,99': '2,3,0,6,99',
                    '2,4,4,5,99,0':'2,4,4,5,99,9801',
                    '1,1,1,4,99,5,6,0,99':'30,1,1,4,2,5,6,0,99'
                }
        for key in inputs:
           print("================================================")
           print(f"{key} should be restored in {inputs.get(key)}")
           self.assertEqual(','.join([str(x) for x in restore_state(format_input(key))]), inputs.get(key))
