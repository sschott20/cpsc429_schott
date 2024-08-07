# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class StablehloCustomCallOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = StablehloCustomCallOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsStablehloCustomCallOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def StablehloCustomCallOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # StablehloCustomCallOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # StablehloCustomCallOptions
    def CallTargetName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # StablehloCustomCallOptions
    def HasSideEffect(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # StablehloCustomCallOptions
    def BackendConfig(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # StablehloCustomCallOptions
    def ApiVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # StablehloCustomCallOptions
    def CalledComputations(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # StablehloCustomCallOptions
    def CalledComputationsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # StablehloCustomCallOptions
    def CalledComputationsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # StablehloCustomCallOptions
    def CalledComputationsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # StablehloCustomCallOptions
    def CustomAttributes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # StablehloCustomCallOptions
    def CustomAttributesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # StablehloCustomCallOptions
    def CustomAttributesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # StablehloCustomCallOptions
    def CustomAttributesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

def StablehloCustomCallOptionsStart(builder):
    builder.StartObject(6)

def Start(builder):
    StablehloCustomCallOptionsStart(builder)

def StablehloCustomCallOptionsAddCallTargetName(builder, callTargetName):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(callTargetName), 0)

def AddCallTargetName(builder, callTargetName):
    StablehloCustomCallOptionsAddCallTargetName(builder, callTargetName)

def StablehloCustomCallOptionsAddHasSideEffect(builder, hasSideEffect):
    builder.PrependBoolSlot(1, hasSideEffect, 0)

def AddHasSideEffect(builder, hasSideEffect):
    StablehloCustomCallOptionsAddHasSideEffect(builder, hasSideEffect)

def StablehloCustomCallOptionsAddBackendConfig(builder, backendConfig):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(backendConfig), 0)

def AddBackendConfig(builder, backendConfig):
    StablehloCustomCallOptionsAddBackendConfig(builder, backendConfig)

def StablehloCustomCallOptionsAddApiVersion(builder, apiVersion):
    builder.PrependInt32Slot(3, apiVersion, 0)

def AddApiVersion(builder, apiVersion):
    StablehloCustomCallOptionsAddApiVersion(builder, apiVersion)

def StablehloCustomCallOptionsAddCalledComputations(builder, calledComputations):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(calledComputations), 0)

def AddCalledComputations(builder, calledComputations):
    StablehloCustomCallOptionsAddCalledComputations(builder, calledComputations)

def StablehloCustomCallOptionsStartCalledComputationsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartCalledComputationsVector(builder, numElems: int) -> int:
    return StablehloCustomCallOptionsStartCalledComputationsVector(builder, numElems)

def StablehloCustomCallOptionsAddCustomAttributes(builder, customAttributes):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(customAttributes), 0)

def AddCustomAttributes(builder, customAttributes):
    StablehloCustomCallOptionsAddCustomAttributes(builder, customAttributes)

def StablehloCustomCallOptionsStartCustomAttributesVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartCustomAttributesVector(builder, numElems: int) -> int:
    return StablehloCustomCallOptionsStartCustomAttributesVector(builder, numElems)

def StablehloCustomCallOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return StablehloCustomCallOptionsEnd(builder)

try:
    from typing import List
except:
    pass

class StablehloCustomCallOptionsT(object):

    # StablehloCustomCallOptionsT
    def __init__(self):
        self.callTargetName = None  # type: str
        self.hasSideEffect = False  # type: bool
        self.backendConfig = None  # type: str
        self.apiVersion = 0  # type: int
        self.calledComputations = None  # type: List[int]
        self.customAttributes = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        stablehloCustomCallOptions = StablehloCustomCallOptions()
        stablehloCustomCallOptions.Init(buf, pos)
        return cls.InitFromObj(stablehloCustomCallOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, stablehloCustomCallOptions):
        x = StablehloCustomCallOptionsT()
        x._UnPack(stablehloCustomCallOptions)
        return x

    # StablehloCustomCallOptionsT
    def _UnPack(self, stablehloCustomCallOptions):
        if stablehloCustomCallOptions is None:
            return
        self.callTargetName = stablehloCustomCallOptions.CallTargetName()
        self.hasSideEffect = stablehloCustomCallOptions.HasSideEffect()
        self.backendConfig = stablehloCustomCallOptions.BackendConfig()
        self.apiVersion = stablehloCustomCallOptions.ApiVersion()
        if not stablehloCustomCallOptions.CalledComputationsIsNone():
            if np is None:
                self.calledComputations = []
                for i in range(stablehloCustomCallOptions.CalledComputationsLength()):
                    self.calledComputations.append(stablehloCustomCallOptions.CalledComputations(i))
            else:
                self.calledComputations = stablehloCustomCallOptions.CalledComputationsAsNumpy()
        if not stablehloCustomCallOptions.CustomAttributesIsNone():
            if np is None:
                self.customAttributes = []
                for i in range(stablehloCustomCallOptions.CustomAttributesLength()):
                    self.customAttributes.append(stablehloCustomCallOptions.CustomAttributes(i))
            else:
                self.customAttributes = stablehloCustomCallOptions.CustomAttributesAsNumpy()

    # StablehloCustomCallOptionsT
    def Pack(self, builder):
        if self.callTargetName is not None:
            callTargetName = builder.CreateString(self.callTargetName)
        if self.backendConfig is not None:
            backendConfig = builder.CreateString(self.backendConfig)
        if self.calledComputations is not None:
            if np is not None and type(self.calledComputations) is np.ndarray:
                calledComputations = builder.CreateNumpyVector(self.calledComputations)
            else:
                StablehloCustomCallOptionsStartCalledComputationsVector(builder, len(self.calledComputations))
                for i in reversed(range(len(self.calledComputations))):
                    builder.PrependInt32(self.calledComputations[i])
                calledComputations = builder.EndVector()
        if self.customAttributes is not None:
            if np is not None and type(self.customAttributes) is np.ndarray:
                customAttributes = builder.CreateNumpyVector(self.customAttributes)
            else:
                StablehloCustomCallOptionsStartCustomAttributesVector(builder, len(self.customAttributes))
                for i in reversed(range(len(self.customAttributes))):
                    builder.PrependUint8(self.customAttributes[i])
                customAttributes = builder.EndVector()
        StablehloCustomCallOptionsStart(builder)
        if self.callTargetName is not None:
            StablehloCustomCallOptionsAddCallTargetName(builder, callTargetName)
        StablehloCustomCallOptionsAddHasSideEffect(builder, self.hasSideEffect)
        if self.backendConfig is not None:
            StablehloCustomCallOptionsAddBackendConfig(builder, backendConfig)
        StablehloCustomCallOptionsAddApiVersion(builder, self.apiVersion)
        if self.calledComputations is not None:
            StablehloCustomCallOptionsAddCalledComputations(builder, calledComputations)
        if self.customAttributes is not None:
            StablehloCustomCallOptionsAddCustomAttributes(builder, customAttributes)
        stablehloCustomCallOptions = StablehloCustomCallOptionsEnd(builder)
        return stablehloCustomCallOptions
