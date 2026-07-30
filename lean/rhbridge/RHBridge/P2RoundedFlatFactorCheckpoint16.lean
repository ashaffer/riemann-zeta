import RHBridge.P2RoundedFactorCheckpoint16
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck16_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel16FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel16FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel16FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel16FlatEven0_eq
  · exact panel16FlatEven1_eq
  · exact panel16FlatEven2_eq
  · exact panel16FlatEven3_eq
  · exact panel16FlatEven4_eq
  · exact panel16FlatEven5_eq
  · exact panel16FlatEven6_eq
  · exact panel16FlatEven7_eq
  · exact panel16FlatEven8_eq
  · exact panel16FlatEven9_eq
  · exact panel16FlatEven10_eq
  · exact panel16FlatEven11_eq
  · exact panel16FlatEven12_eq
  · exact panel16FlatEven13_eq
  · exact panel16FlatEven14_eq
  · exact panel16FlatEven15_eq
  · exact panel16FlatEven16_eq
  · exact panel16FlatEven17_eq
  · exact panel16FlatEven18_eq
  · exact panel16FlatEven19_eq
  · exact panel16FlatEven20_eq
  · exact panel16FlatEven21_eq
  · exact panel16FlatEven22_eq
  · exact panel16FlatEven23_eq

theorem panel16FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel16FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel16FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel16FlatOdd0_eq
  · exact panel16FlatOdd1_eq
  · exact panel16FlatOdd2_eq
  · exact panel16FlatOdd3_eq
  · exact panel16FlatOdd4_eq
  · exact panel16FlatOdd5_eq
  · exact panel16FlatOdd6_eq
  · exact panel16FlatOdd7_eq
  · exact panel16FlatOdd8_eq
  · exact panel16FlatOdd9_eq
  · exact panel16FlatOdd10_eq
  · exact panel16FlatOdd11_eq
  · exact panel16FlatOdd12_eq
  · exact panel16FlatOdd13_eq
  · exact panel16FlatOdd14_eq
  · exact panel16FlatOdd15_eq
  · exact panel16FlatOdd16_eq
  · exact panel16FlatOdd17_eq
  · exact panel16FlatOdd18_eq
  · exact panel16FlatOdd19_eq
  · exact panel16FlatOdd20_eq
  · exact panel16FlatOdd21_eq
  · exact panel16FlatOdd22_eq
  · exact panel16FlatOdd23_eq

theorem panel16FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel16FlatCache.EnclosesCanonical
      ⟨16, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel16FlatDefect
    rw [panel16FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel16DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel16FlatEvenComponents).get i)
    rw [panel16FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel16OuterLengthTable
      .even ⟨16, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel16FlatOddComponents).get i)
    rw [panel16FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel16OuterLengthTable
      .odd ⟨16, by decide⟩ i

end RHP2Bridge
