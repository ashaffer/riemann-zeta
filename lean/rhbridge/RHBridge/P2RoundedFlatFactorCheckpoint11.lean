import RHBridge.P2RoundedFactorCheckpoint11
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck11_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel11FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel11FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel11FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel11FlatEven0_eq
  · exact panel11FlatEven1_eq
  · exact panel11FlatEven2_eq
  · exact panel11FlatEven3_eq
  · exact panel11FlatEven4_eq
  · exact panel11FlatEven5_eq
  · exact panel11FlatEven6_eq
  · exact panel11FlatEven7_eq
  · exact panel11FlatEven8_eq
  · exact panel11FlatEven9_eq
  · exact panel11FlatEven10_eq
  · exact panel11FlatEven11_eq
  · exact panel11FlatEven12_eq
  · exact panel11FlatEven13_eq
  · exact panel11FlatEven14_eq
  · exact panel11FlatEven15_eq
  · exact panel11FlatEven16_eq
  · exact panel11FlatEven17_eq
  · exact panel11FlatEven18_eq
  · exact panel11FlatEven19_eq
  · exact panel11FlatEven20_eq
  · exact panel11FlatEven21_eq
  · exact panel11FlatEven22_eq
  · exact panel11FlatEven23_eq

theorem panel11FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel11FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel11FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel11FlatOdd0_eq
  · exact panel11FlatOdd1_eq
  · exact panel11FlatOdd2_eq
  · exact panel11FlatOdd3_eq
  · exact panel11FlatOdd4_eq
  · exact panel11FlatOdd5_eq
  · exact panel11FlatOdd6_eq
  · exact panel11FlatOdd7_eq
  · exact panel11FlatOdd8_eq
  · exact panel11FlatOdd9_eq
  · exact panel11FlatOdd10_eq
  · exact panel11FlatOdd11_eq
  · exact panel11FlatOdd12_eq
  · exact panel11FlatOdd13_eq
  · exact panel11FlatOdd14_eq
  · exact panel11FlatOdd15_eq
  · exact panel11FlatOdd16_eq
  · exact panel11FlatOdd17_eq
  · exact panel11FlatOdd18_eq
  · exact panel11FlatOdd19_eq
  · exact panel11FlatOdd20_eq
  · exact panel11FlatOdd21_eq
  · exact panel11FlatOdd22_eq
  · exact panel11FlatOdd23_eq

theorem panel11FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel11FlatCache.EnclosesCanonical
      ⟨11, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel11FlatDefect
    rw [panel11FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel11DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel11FlatEvenComponents).get i)
    rw [panel11FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel11OuterLengthTable
      .even ⟨11, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel11FlatOddComponents).get i)
    rw [panel11FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel11OuterLengthTable
      .odd ⟨11, by decide⟩ i

end RHP2Bridge
