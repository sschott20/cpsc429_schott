# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MatrixDiagOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MatrixDiagOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMatrixDiagOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def MatrixDiagOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # MatrixDiagOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def MatrixDiagOptionsStart(builder):
    builder.StartObject(0)

def Start(builder):
    MatrixDiagOptionsStart(builder)

def MatrixDiagOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return MatrixDiagOptionsEnd(builder)


class MatrixDiagOptionsT(object):

    # MatrixDiagOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        matrixDiagOptions = MatrixDiagOptions()
        matrixDiagOptions.Init(buf, pos)
        return cls.InitFromObj(matrixDiagOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, matrixDiagOptions):
        x = MatrixDiagOptionsT()
        x._UnPack(matrixDiagOptions)
        return x

    # MatrixDiagOptionsT
    def _UnPack(self, matrixDiagOptions):
        if matrixDiagOptions is None:
            return

    # MatrixDiagOptionsT
    def Pack(self, builder):
        MatrixDiagOptionsStart(builder)
        matrixDiagOptions = MatrixDiagOptionsEnd(builder)
        return matrixDiagOptions