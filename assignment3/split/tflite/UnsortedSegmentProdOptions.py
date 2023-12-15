# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UnsortedSegmentProdOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UnsortedSegmentProdOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUnsortedSegmentProdOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def UnsortedSegmentProdOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # UnsortedSegmentProdOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def UnsortedSegmentProdOptionsStart(builder):
    builder.StartObject(0)

def Start(builder):
    UnsortedSegmentProdOptionsStart(builder)

def UnsortedSegmentProdOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return UnsortedSegmentProdOptionsEnd(builder)


class UnsortedSegmentProdOptionsT(object):

    # UnsortedSegmentProdOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        unsortedSegmentProdOptions = UnsortedSegmentProdOptions()
        unsortedSegmentProdOptions.Init(buf, pos)
        return cls.InitFromObj(unsortedSegmentProdOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, unsortedSegmentProdOptions):
        x = UnsortedSegmentProdOptionsT()
        x._UnPack(unsortedSegmentProdOptions)
        return x

    # UnsortedSegmentProdOptionsT
    def _UnPack(self, unsortedSegmentProdOptions):
        if unsortedSegmentProdOptions is None:
            return

    # UnsortedSegmentProdOptionsT
    def Pack(self, builder):
        UnsortedSegmentProdOptionsStart(builder)
        unsortedSegmentProdOptions = UnsortedSegmentProdOptionsEnd(builder)
        return unsortedSegmentProdOptions
