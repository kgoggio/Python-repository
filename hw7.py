#Kyle Goggio
# colaborator: Thomas Staszel

class Volume:
    def __init__(self,starting_volume=0):
        if starting_volume <= 0:
            self.current_vol = 0
        elif starting_volume >= 11:
            self.current_vol = 11
        else:
            self.current_vol = starting_volume

    def __repr__(self):
        self.strval = 'Volume({})'.format(str(self.current_vol))
        return self.strval

        #how do i do this one?

    def set(self, new_volume_lvl=0):
        if new_volume_lvl > 11:
            self.current_vol = 11
        elif new_volume_lvl < 0:
            self.current_vol = 0
        else:
            self.current_vol = new_volume_lvl

    def get(self) -> object:
        return self.current_vol



    def up(self, positive_delta_v):
        if (self.current_vol + positive_delta_v) > 11:
            self.current_vol = 11
        elif self.current_vol + positive_delta_v < 0:
            self.current_vol =0
        else:
            self.current_vol += positive_delta_v


    def down(self,negative_delta_v):
        if self.current_vol - negative_delta_v < 0:
            self.current_vol = 0
        else:
            self.current_vol -= negative_delta_v
    def __eq__(self,other):
        if self.current_vol == other.current_vol:
            return True
        else:
            return False

def partyVolume(txt_file_name):
    with open(txt_file_name) as txt_file:
        s_vol= eval(txt_file.readline())
        if s_vol < 0:
            current_vol = Volume(0)
        elif s_vol > 11:
            current_vol = Volume(11)
        else:
            current_vol = Volume(s_vol)
        lines = txt_file.readlines()
        for line in lines:
            if 'U' in line:
                positive_delta_v = eval(line.strip('U').strip('\n'))
                Volume.up(current_vol, positive_delta_v)
            elif 'D' in line:
                negative_delta_v = eval(line.strip('D').strip('\n'))
                Volume.down(current_vol,negative_delta_v)
        ##for line in txt_file:
            #
        #if line1 <= 0:
            #start_vol = 0
        #elif line1 <11:
            #start_vol = 11
        #else:
            #start_vol = line1
    return current_vol






if __name__=='__main__':
    import doctest
    print(doctest.testfile('hw7TEST.py'))
