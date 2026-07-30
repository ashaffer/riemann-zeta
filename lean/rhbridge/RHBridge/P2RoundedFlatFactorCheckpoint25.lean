import RHBridge.P2RoundedFactorCheckpoint25
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck25_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel25FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel25FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel25FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel25FlatEven0_eq
  · exact panel25FlatEven1_eq
  · exact panel25FlatEven2_eq
  · exact panel25FlatEven3_eq
  · exact panel25FlatEven4_eq
  · exact panel25FlatEven5_eq
  · exact panel25FlatEven6_eq
  · exact panel25FlatEven7_eq
  · exact panel25FlatEven8_eq
  · exact panel25FlatEven9_eq
  · exact panel25FlatEven10_eq
  · exact panel25FlatEven11_eq
  · exact panel25FlatEven12_eq
  · exact panel25FlatEven13_eq
  · exact panel25FlatEven14_eq
  · exact panel25FlatEven15_eq
  · exact panel25FlatEven16_eq
  · exact panel25FlatEven17_eq
  · exact panel25FlatEven18_eq
  · exact panel25FlatEven19_eq
  · exact panel25FlatEven20_eq
  · exact panel25FlatEven21_eq
  · exact panel25FlatEven22_eq
  · exact panel25FlatEven23_eq

theorem panel25FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel25FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel25FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel25FlatOdd0_eq
  · exact panel25FlatOdd1_eq
  · exact panel25FlatOdd2_eq
  · exact panel25FlatOdd3_eq
  · exact panel25FlatOdd4_eq
  · exact panel25FlatOdd5_eq
  · exact panel25FlatOdd6_eq
  · exact panel25FlatOdd7_eq
  · exact panel25FlatOdd8_eq
  · exact panel25FlatOdd9_eq
  · exact panel25FlatOdd10_eq
  · exact panel25FlatOdd11_eq
  · exact panel25FlatOdd12_eq
  · exact panel25FlatOdd13_eq
  · exact panel25FlatOdd14_eq
  · exact panel25FlatOdd15_eq
  · exact panel25FlatOdd16_eq
  · exact panel25FlatOdd17_eq
  · exact panel25FlatOdd18_eq
  · exact panel25FlatOdd19_eq
  · exact panel25FlatOdd20_eq
  · exact panel25FlatOdd21_eq
  · exact panel25FlatOdd22_eq
  · exact panel25FlatOdd23_eq

theorem panel25FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel25FlatCache.EnclosesCanonical
      ⟨25, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel25FlatDefect
    rw [panel25FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel25DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel25FlatEvenComponents).get i)
    rw [panel25FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel25OuterLengthTable
      .even ⟨25, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel25FlatOddComponents).get i)
    rw [panel25FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel25OuterLengthTable
      .odd ⟨25, by decide⟩ i

end RHP2Bridge
