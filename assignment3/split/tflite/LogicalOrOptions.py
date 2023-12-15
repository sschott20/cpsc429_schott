# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LogicalOrOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LogicalOrOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsLogicalOrOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def LogicalOrOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # LogicalOrOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def LogicalOrOptionsStart(builder):
    builder.StartObject(0)

def Start(builder):
    LogicalOrOptionsStart(builder)

def LogicalOrOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return LogicalOrOptionsEnd(builder)


class LogicalOrOptionsT(object):

    # LogicalOrOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        logicalOrOptions = LogicalOrOptions()
        logicalOrOptions.Init(buf, pos)
        return cls.InitFromObj(logicalOrOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, logicalOrOptions):
        x = LogicalOrOptionsT()
        x._UnPack(logicalOrOptions)
        return x

    # LogicalOrOptionsT
    def _UnPack(self, logicalOrOptions):
        if logicalOrOptions is None:
            return

    # LogicalOrOptionsT
    def Pack(self, builder):
        LogicalOrOptionsStart(builder)
        logicalOrOptions = LogicalOrOptionsEnd(builder)
        return logicalOrOptions
