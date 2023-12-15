# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FullyConnectedOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FullyConnectedOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFullyConnectedOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def FullyConnectedOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # FullyConnectedOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FullyConnectedOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # FullyConnectedOptions
    def WeightsFormat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # FullyConnectedOptions
    def KeepNumDims(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # FullyConnectedOptions
    def AsymmetricQuantizeInputs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # FullyConnectedOptions
    def QuantizedBiasType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def FullyConnectedOptionsStart(builder):
    builder.StartObject(5)

def Start(builder):
    FullyConnectedOptionsStart(builder)

def FullyConnectedOptionsAddFusedActivationFunction(builder, fusedActivationFunction):
    builder.PrependInt8Slot(0, fusedActivationFunction, 0)

def AddFusedActivationFunction(builder, fusedActivationFunction):
    FullyConnectedOptionsAddFusedActivationFunction(builder, fusedActivationFunction)

def FullyConnectedOptionsAddWeightsFormat(builder, weightsFormat):
    builder.PrependInt8Slot(1, weightsFormat, 0)

def AddWeightsFormat(builder, weightsFormat):
    FullyConnectedOptionsAddWeightsFormat(builder, weightsFormat)

def FullyConnectedOptionsAddKeepNumDims(builder, keepNumDims):
    builder.PrependBoolSlot(2, keepNumDims, 0)

def AddKeepNumDims(builder, keepNumDims):
    FullyConnectedOptionsAddKeepNumDims(builder, keepNumDims)

def FullyConnectedOptionsAddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs):
    builder.PrependBoolSlot(3, asymmetricQuantizeInputs, 0)

def AddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs):
    FullyConnectedOptionsAddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs)

def FullyConnectedOptionsAddQuantizedBiasType(builder, quantizedBiasType):
    builder.PrependInt8Slot(4, quantizedBiasType, 0)

def AddQuantizedBiasType(builder, quantizedBiasType):
    FullyConnectedOptionsAddQuantizedBiasType(builder, quantizedBiasType)

def FullyConnectedOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return FullyConnectedOptionsEnd(builder)


class FullyConnectedOptionsT(object):

    # FullyConnectedOptionsT
    def __init__(self):
        self.fusedActivationFunction = 0  # type: int
        self.weightsFormat = 0  # type: int
        self.keepNumDims = False  # type: bool
        self.asymmetricQuantizeInputs = False  # type: bool
        self.quantizedBiasType = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        fullyConnectedOptions = FullyConnectedOptions()
        fullyConnectedOptions.Init(buf, pos)
        return cls.InitFromObj(fullyConnectedOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, fullyConnectedOptions):
        x = FullyConnectedOptionsT()
        x._UnPack(fullyConnectedOptions)
        return x

    # FullyConnectedOptionsT
    def _UnPack(self, fullyConnectedOptions):
        if fullyConnectedOptions is None:
            return
        self.fusedActivationFunction = fullyConnectedOptions.FusedActivationFunction()
        self.weightsFormat = fullyConnectedOptions.WeightsFormat()
        self.keepNumDims = fullyConnectedOptions.KeepNumDims()
        self.asymmetricQuantizeInputs = fullyConnectedOptions.AsymmetricQuantizeInputs()
        self.quantizedBiasType = fullyConnectedOptions.QuantizedBiasType()

    # FullyConnectedOptionsT
    def Pack(self, builder):
        FullyConnectedOptionsStart(builder)
        FullyConnectedOptionsAddFusedActivationFunction(builder, self.fusedActivationFunction)
        FullyConnectedOptionsAddWeightsFormat(builder, self.weightsFormat)
        FullyConnectedOptionsAddKeepNumDims(builder, self.keepNumDims)
        FullyConnectedOptionsAddAsymmetricQuantizeInputs(builder, self.asymmetricQuantizeInputs)
        FullyConnectedOptionsAddQuantizedBiasType(builder, self.quantizedBiasType)
        fullyConnectedOptions = FullyConnectedOptionsEnd(builder)
        return fullyConnectedOptions
