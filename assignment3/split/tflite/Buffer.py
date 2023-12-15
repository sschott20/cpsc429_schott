# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Buffer(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Buffer()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBuffer(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def BufferBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # Buffer
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Buffer
    def Data(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Buffer
    def DataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Buffer
    def DataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Buffer
    def DataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # Buffer
    def Offset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Buffer
    def Size(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

def BufferStart(builder):
    builder.StartObject(3)

def Start(builder):
    BufferStart(builder)

def BufferAddData(builder, data):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(data), 0)

def AddData(builder, data):
    BufferAddData(builder, data)

def BufferStartDataVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartDataVector(builder, numElems: int) -> int:
    return BufferStartDataVector(builder, numElems)

def BufferAddOffset(builder, offset):
    builder.PrependUint64Slot(1, offset, 0)

def AddOffset(builder, offset):
    BufferAddOffset(builder, offset)

def BufferAddSize(builder, size):
    builder.PrependUint64Slot(2, size, 0)

def AddSize(builder, size):
    BufferAddSize(builder, size)

def BufferEnd(builder):
    return builder.EndObject()

def End(builder):
    return BufferEnd(builder)

try:
    from typing import List
except:
    pass

class BufferT(object):

    # BufferT
    def __init__(self):
        self.data = None  # type: List[int]
        self.offset = 0  # type: int
        self.size = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        buffer = Buffer()
        buffer.Init(buf, pos)
        return cls.InitFromObj(buffer)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, buffer):
        x = BufferT()
        x._UnPack(buffer)
        return x

    # BufferT
    def _UnPack(self, buffer):
        if buffer is None:
            return
        if not buffer.DataIsNone():
            if np is None:
                self.data = []
                for i in range(buffer.DataLength()):
                    self.data.append(buffer.Data(i))
            else:
                self.data = buffer.DataAsNumpy()
        self.offset = buffer.Offset()
        self.size = buffer.Size()

    # BufferT
    def Pack(self, builder):
        if self.data is not None:
            if np is not None and type(self.data) is np.ndarray:
                data = builder.CreateNumpyVector(self.data)
            else:
                BufferStartDataVector(builder, len(self.data))
                for i in reversed(range(len(self.data))):
                    builder.PrependUint8(self.data[i])
                data = builder.EndVector()
        BufferStart(builder)
        if self.data is not None:
            BufferAddData(builder, data)
        BufferAddOffset(builder, self.offset)
        BufferAddSize(builder, self.size)
        buffer = BufferEnd(builder)
        return buffer
