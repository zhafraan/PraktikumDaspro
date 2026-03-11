from BinaryTree_NIM import *

def BSearchX(P, X):
    if isTreeEmpty(P):
        return False
    else:
        if X == Akar(P):
            return True
        else:
            return BSearchX(Kiri(P), X) or BSearchX(Kanan(P), X)

def AddX(P, X):
    if not BSearchX(P, X):
        if isTreeEmpty(P):
            return MakePB(X, [], [])
        else:
            if X >= Akar(P):
                return MakePB(Akar(P), Left(P), AddX(Right(P), X))
            else:
                return MakePB(Akar(P), AddX(Left(P), X), Right(P))
        

def MakeBST(L):
    if isTreeEmpty(L):
        return L
    else:
        return AddX(MakeBST(Head(L)), LastElmt(L))

def Delete(P, X):
    if isTreeEmpty(P):
        return []
    else:
        if Akar(P) == X:
            if isTreeEmpty(Left(P)) and isTreeEmpty(Right(P)):
                return []
            else:
                if isTreeEmpty(Left(P)):
                    return MakePB(Akar(Right(P)), Left(P), Right(Right(P)))
                else:
                    return MakePB(Akar(Left(P)), Left(Left(P)), Right(P))

        elif X > Akar(P):
            return MakePB(Akar(P), Left(P), Delete(Right(P), X))
        else:
            return MakePB(Akar(P), Delete(Left(P), X), Right(P)) 



