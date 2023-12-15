# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BucketizeOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BucketizeOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBucketizeOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def BucketizeOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # BucketizeOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BucketizeOptions
    def Boundaries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # BucketizeOptions
    def BoundariesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # BucketizeOptions
    def BoundariesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # BucketizeOptions
    def BoundariesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def BucketizeOptionsStart(builder):
    builder.StartObject(1)

def Start(builder):
    BucketizeOptionsStart(builder)

def BucketizeOptionsAddBoundaries(builder, boundaries):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(boundaries), 0)

def AddBoundaries(builder, boundaries):
    BucketizeOptionsAddBoundaries(builder, boundaries)

def BucketizeOptionsStartBoundariesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartBoundariesVector(builder, numElems: int) -> int:
    return BucketizeOptionsStartBoundariesVector(builder, numElems)

def BucketizeOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return BucketizeOptionsEnd(builder)

try:
    from typing import List
except:
    pass

class BucketizeOptionsT(object):

    # BucketizeOptionsT
    def __init__(self):
        self.boundaries = None  # type: List[float]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        bucketizeOptions = BucketizeOptions()
        bucketizeOptions.Init(buf, pos)
        return cls.InitFromObj(bucketizeOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, bucketizeOptions):
        x = BucketizeOptionsT()
        x._UnPack(bucketizeOptions)
        return x

    # BucketizeOptionsT
    def _UnPack(self, bucketizeOptions):
        if bucketizeOptions is None:
            return
        if not bucketizeOptions.BoundariesIsNone():
            if np is None:
                self.boundaries = []
                for i in range(bucketizeOptions.BoundariesLength()):
                    self.boundaries.append(bucketizeOptions.Boundaries(i))
            else:
                self.boundaries = bucketizeOptions.BoundariesAsNumpy()

    # BucketizeOptionsT
    def Pack(self, builder):
        if self.boundaries is not None:
            if np is not None and type(self.boundaries) is np.ndarray:
                boundaries = builder.CreateNumpyVector(self.boundaries)
            else:
                BucketizeOptionsStartBoundariesVector(builder, len(self.boundaries))
                for i in reversed(range(len(self.boundaries))):
                    builder.PrependFloat32(self.boundaries[i])
                boundaries = builder.EndVector()
        BucketizeOptionsStart(builder)
        if self.boundaries is not None:
            BucketizeOptionsAddBoundaries(builder, boundaries)
        bucketizeOptions = BucketizeOptionsEnd(builder)
        return bucketizeOptions
