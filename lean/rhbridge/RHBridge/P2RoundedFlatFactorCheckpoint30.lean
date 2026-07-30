import RHBridge.P2RoundedFactorCheckpoint30
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck30_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel30FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel30FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel30TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel30FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel30FlatEven0_eq
  · exact panel30FlatEven1_eq
  · exact panel30FlatEven2_eq
  · exact panel30FlatEven3_eq
  · exact panel30FlatEven4_eq
  · exact panel30FlatEven5_eq
  · exact panel30FlatEven6_eq
  · exact panel30FlatEven7_eq
  · exact panel30FlatEven8_eq
  · exact panel30FlatEven9_eq
  · exact panel30FlatEven10_eq
  · exact panel30FlatEven11_eq
  · exact panel30FlatEven12_eq
  · exact panel30FlatEven13_eq
  · exact panel30FlatEven14_eq
  · exact panel30FlatEven15_eq
  · exact panel30FlatEven16_eq
  · exact panel30FlatEven17_eq
  · exact panel30FlatEven18_eq
  · exact panel30FlatEven19_eq
  · exact panel30FlatEven20_eq
  · exact panel30FlatEven21_eq
  · exact panel30FlatEven22_eq
  · exact panel30FlatEven23_eq

theorem panel30FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel30FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel30FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel30FlatOdd0_eq
  · exact panel30FlatOdd1_eq
  · exact panel30FlatOdd2_eq
  · exact panel30FlatOdd3_eq
  · exact panel30FlatOdd4_eq
  · exact panel30FlatOdd5_eq
  · exact panel30FlatOdd6_eq
  · exact panel30FlatOdd7_eq
  · exact panel30FlatOdd8_eq
  · exact panel30FlatOdd9_eq
  · exact panel30FlatOdd10_eq
  · exact panel30FlatOdd11_eq
  · exact panel30FlatOdd12_eq
  · exact panel30FlatOdd13_eq
  · exact panel30FlatOdd14_eq
  · exact panel30FlatOdd15_eq
  · exact panel30FlatOdd16_eq
  · exact panel30FlatOdd17_eq
  · exact panel30FlatOdd18_eq
  · exact panel30FlatOdd19_eq
  · exact panel30FlatOdd20_eq
  · exact panel30FlatOdd21_eq
  · exact panel30FlatOdd22_eq
  · exact panel30FlatOdd23_eq

theorem panel30FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel30FlatCache.EnclosesCanonical
      ⟨30, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel30FlatDefect
    rw [panel30FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel30DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel30FlatEvenComponents).get i)
    rw [panel30FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel30OuterLengthTable
      .even ⟨30, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel30FlatOddComponents).get i)
    rw [panel30FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel30OuterLengthTable
      .odd ⟨30, by decide⟩ i

end RHP2Bridge
