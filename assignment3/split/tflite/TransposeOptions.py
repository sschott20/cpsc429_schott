# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TransposeOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TransposeOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTransposeOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def TransposeOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # TransposeOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def TransposeOptionsStart(builder):
    builder.StartObject(0)

def Start(builder):
    TransposeOptionsStart(builder)

def TransposeOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return TransposeOptionsEnd(builder)


class TransposeOptionsT(object):

    # TransposeOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        transposeOptions = TransposeOptions()
        transposeOptions.Init(buf, pos)
        return cls.InitFromObj(transposeOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, transposeOptions):
        x = TransposeOptionsT()
        x._UnPack(transposeOptions)
        return x

    # TransposeOptionsT
    def _UnPack(self, transposeOptions):
        if transposeOptions is None:
            return

    # TransposeOptionsT
    def Pack(self, builder):
        TransposeOptionsStart(builder)
        transposeOptions = TransposeOptionsEnd(builder)
        return transposeOptions
