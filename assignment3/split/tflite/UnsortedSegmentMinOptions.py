# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UnsortedSegmentMinOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UnsortedSegmentMinOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUnsortedSegmentMinOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def UnsortedSegmentMinOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # UnsortedSegmentMinOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def UnsortedSegmentMinOptionsStart(builder):
    builder.StartObject(0)

def Start(builder):
    UnsortedSegmentMinOptionsStart(builder)

def UnsortedSegmentMinOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return UnsortedSegmentMinOptionsEnd(builder)


class UnsortedSegmentMinOptionsT(object):

    # UnsortedSegmentMinOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        unsortedSegmentMinOptions = UnsortedSegmentMinOptions()
        unsortedSegmentMinOptions.Init(buf, pos)
        return cls.InitFromObj(unsortedSegmentMinOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, unsortedSegmentMinOptions):
        x = UnsortedSegmentMinOptionsT()
        x._UnPack(unsortedSegmentMinOptions)
        return x

    # UnsortedSegmentMinOptionsT
    def _UnPack(self, unsortedSegmentMinOptions):
        if unsortedSegmentMinOptions is None:
            return

    # UnsortedSegmentMinOptionsT
    def Pack(self, builder):
        UnsortedSegmentMinOptionsStart(builder)
        unsortedSegmentMinOptions = UnsortedSegmentMinOptionsEnd(builder)
        return unsortedSegmentMinOptions
