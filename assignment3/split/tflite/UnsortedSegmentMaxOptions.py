# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UnsortedSegmentMaxOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UnsortedSegmentMaxOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUnsortedSegmentMaxOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def UnsortedSegmentMaxOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # UnsortedSegmentMaxOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def UnsortedSegmentMaxOptionsStart(builder):
    builder.StartObject(0)

def Start(builder):
    UnsortedSegmentMaxOptionsStart(builder)

def UnsortedSegmentMaxOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return UnsortedSegmentMaxOptionsEnd(builder)


class UnsortedSegmentMaxOptionsT(object):

    # UnsortedSegmentMaxOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        unsortedSegmentMaxOptions = UnsortedSegmentMaxOptions()
        unsortedSegmentMaxOptions.Init(buf, pos)
        return cls.InitFromObj(unsortedSegmentMaxOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, unsortedSegmentMaxOptions):
        x = UnsortedSegmentMaxOptionsT()
        x._UnPack(unsortedSegmentMaxOptions)
        return x

    # UnsortedSegmentMaxOptionsT
    def _UnPack(self, unsortedSegmentMaxOptions):
        if unsortedSegmentMaxOptions is None:
            return

    # UnsortedSegmentMaxOptionsT
    def Pack(self, builder):
        UnsortedSegmentMaxOptionsStart(builder)
        unsortedSegmentMaxOptions = UnsortedSegmentMaxOptionsEnd(builder)
        return unsortedSegmentMaxOptions
