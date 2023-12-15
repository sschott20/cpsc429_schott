# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ZerosLikeOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ZerosLikeOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsZerosLikeOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def ZerosLikeOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # ZerosLikeOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def ZerosLikeOptionsStart(builder):
    builder.StartObject(0)

def Start(builder):
    ZerosLikeOptionsStart(builder)

def ZerosLikeOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return ZerosLikeOptionsEnd(builder)


class ZerosLikeOptionsT(object):

    # ZerosLikeOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        zerosLikeOptions = ZerosLikeOptions()
        zerosLikeOptions.Init(buf, pos)
        return cls.InitFromObj(zerosLikeOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, zerosLikeOptions):
        x = ZerosLikeOptionsT()
        x._UnPack(zerosLikeOptions)
        return x

    # ZerosLikeOptionsT
    def _UnPack(self, zerosLikeOptions):
        if zerosLikeOptions is None:
            return

    # ZerosLikeOptionsT
    def Pack(self, builder):
        ZerosLikeOptionsStart(builder)
        zerosLikeOptions = ZerosLikeOptionsEnd(builder)
        return zerosLikeOptions
