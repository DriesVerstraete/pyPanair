from pyPanair.postprocess import ffmf_converter

if __name__ == '__main__':
    print("converting ffmf to a csv file")
    ffmf_converter.write_ffmf()
    print("success!")
