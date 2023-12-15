# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

class SparseIndexVector(object):
    NONE = 0
    Int32Vector = 1
    Uint16Vector = 2
    Uint8Vector = 3

def SparseIndexVectorCreator(unionType, table):
    from flatbuffers.table import Table
    if not isinstance(table, Table):
        return None
    if unionType == SparseIndexVector().Int32Vector:
        import tflite.Int32Vector
        return tflite.Int32Vector.Int32VectorT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == SparseIndexVector().Uint16Vector:
        import tflite.Uint16Vector
        return tflite.Uint16Vector.Uint16VectorT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == SparseIndexVector().Uint8Vector:
        import tflite.Uint8Vector
        return tflite.Uint8Vector.Uint8VectorT.InitFromBuf(table.Bytes, table.Pos)
    return None
