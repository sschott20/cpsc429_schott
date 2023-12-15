# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SVDFOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SVDFOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSVDFOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def SVDFOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # SVDFOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SVDFOptions
    def Rank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SVDFOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # SVDFOptions
    def AsymmetricQuantizeInputs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def SVDFOptionsStart(builder):
    builder.StartObject(3)

def Start(builder):
    SVDFOptionsStart(builder)

def SVDFOptionsAddRank(builder, rank):
    builder.PrependInt32Slot(0, rank, 0)

def AddRank(builder, rank):
    SVDFOptionsAddRank(builder, rank)

def SVDFOptionsAddFusedActivationFunction(builder, fusedActivationFunction):
    builder.PrependInt8Slot(1, fusedActivationFunction, 0)

def AddFusedActivationFunction(builder, fusedActivationFunction):
    SVDFOptionsAddFusedActivationFunction(builder, fusedActivationFunction)

def SVDFOptionsAddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs):
    builder.PrependBoolSlot(2, asymmetricQuantizeInputs, 0)

def AddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs):
    SVDFOptionsAddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs)

def SVDFOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return SVDFOptionsEnd(builder)


class SVDFOptionsT(object):

    # SVDFOptionsT
    def __init__(self):
        self.rank = 0  # type: int
        self.fusedActivationFunction = 0  # type: int
        self.asymmetricQuantizeInputs = False  # type: bool

    @classmethod
    def InitFromBuf(cls, buf, pos):
        svdfoptions = SVDFOptions()
        svdfoptions.Init(buf, pos)
        return cls.InitFromObj(svdfoptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, svdfoptions):
        x = SVDFOptionsT()
        x._UnPack(svdfoptions)
        return x

    # SVDFOptionsT
    def _UnPack(self, svdfoptions):
        if svdfoptions is None:
            return
        self.rank = svdfoptions.Rank()
        self.fusedActivationFunction = svdfoptions.FusedActivationFunction()
        self.asymmetricQuantizeInputs = svdfoptions.AsymmetricQuantizeInputs()

    # SVDFOptionsT
    def Pack(self, builder):
        SVDFOptionsStart(builder)
        SVDFOptionsAddRank(builder, self.rank)
        SVDFOptionsAddFusedActivationFunction(builder, self.fusedActivationFunction)
        SVDFOptionsAddAsymmetricQuantizeInputs(builder, self.asymmetricQuantizeInputs)
        svdfoptions = SVDFOptionsEnd(builder)
        return svdfoptions
