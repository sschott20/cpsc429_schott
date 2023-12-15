# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EqualOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EqualOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEqualOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def EqualOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # EqualOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def EqualOptionsStart(builder):
    builder.StartObject(0)

def Start(builder):
    EqualOptionsStart(builder)

def EqualOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return EqualOptionsEnd(builder)


class EqualOptionsT(object):

    # EqualOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        equalOptions = EqualOptions()
        equalOptions.Init(buf, pos)
        return cls.InitFromObj(equalOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, equalOptions):
        x = EqualOptionsT()
        x._UnPack(equalOptions)
        return x

    # EqualOptionsT
    def _UnPack(self, equalOptions):
        if equalOptions is None:
            return

    # EqualOptionsT
    def Pack(self, builder):
        EqualOptionsStart(builder)
        equalOptions = EqualOptionsEnd(builder)
        return equalOptions
