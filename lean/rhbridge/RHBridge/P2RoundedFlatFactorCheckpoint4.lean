import RHBridge.P2RoundedFactorCheckpoint4
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck4_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel4FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel4FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel4FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel4FlatEven0_eq
  · exact panel4FlatEven1_eq
  · exact panel4FlatEven2_eq
  · exact panel4FlatEven3_eq
  · exact panel4FlatEven4_eq
  · exact panel4FlatEven5_eq
  · exact panel4FlatEven6_eq
  · exact panel4FlatEven7_eq
  · exact panel4FlatEven8_eq
  · exact panel4FlatEven9_eq
  · exact panel4FlatEven10_eq
  · exact panel4FlatEven11_eq
  · exact panel4FlatEven12_eq
  · exact panel4FlatEven13_eq
  · exact panel4FlatEven14_eq
  · exact panel4FlatEven15_eq
  · exact panel4FlatEven16_eq
  · exact panel4FlatEven17_eq
  · exact panel4FlatEven18_eq
  · exact panel4FlatEven19_eq
  · exact panel4FlatEven20_eq
  · exact panel4FlatEven21_eq
  · exact panel4FlatEven22_eq
  · exact panel4FlatEven23_eq

theorem panel4FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel4FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel4FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel4FlatOdd0_eq
  · exact panel4FlatOdd1_eq
  · exact panel4FlatOdd2_eq
  · exact panel4FlatOdd3_eq
  · exact panel4FlatOdd4_eq
  · exact panel4FlatOdd5_eq
  · exact panel4FlatOdd6_eq
  · exact panel4FlatOdd7_eq
  · exact panel4FlatOdd8_eq
  · exact panel4FlatOdd9_eq
  · exact panel4FlatOdd10_eq
  · exact panel4FlatOdd11_eq
  · exact panel4FlatOdd12_eq
  · exact panel4FlatOdd13_eq
  · exact panel4FlatOdd14_eq
  · exact panel4FlatOdd15_eq
  · exact panel4FlatOdd16_eq
  · exact panel4FlatOdd17_eq
  · exact panel4FlatOdd18_eq
  · exact panel4FlatOdd19_eq
  · exact panel4FlatOdd20_eq
  · exact panel4FlatOdd21_eq
  · exact panel4FlatOdd22_eq
  · exact panel4FlatOdd23_eq

theorem panel4FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel4FlatCache.EnclosesCanonical
      ⟨4, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel4FlatDefect
    rw [panel4FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel4DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel4FlatEvenComponents).get i)
    rw [panel4FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel4OuterLengthTable
      .even ⟨4, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel4FlatOddComponents).get i)
    rw [panel4FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel4OuterLengthTable
      .odd ⟨4, by decide⟩ i

end RHP2Bridge
