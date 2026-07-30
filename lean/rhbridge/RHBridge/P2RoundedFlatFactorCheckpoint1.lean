import RHBridge.P2RoundedFactorCheckpoint1
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck1_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel1FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel1FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel1FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel1FlatEven0_eq
  · exact panel1FlatEven1_eq
  · exact panel1FlatEven2_eq
  · exact panel1FlatEven3_eq
  · exact panel1FlatEven4_eq
  · exact panel1FlatEven5_eq
  · exact panel1FlatEven6_eq
  · exact panel1FlatEven7_eq
  · exact panel1FlatEven8_eq
  · exact panel1FlatEven9_eq
  · exact panel1FlatEven10_eq
  · exact panel1FlatEven11_eq
  · exact panel1FlatEven12_eq
  · exact panel1FlatEven13_eq
  · exact panel1FlatEven14_eq
  · exact panel1FlatEven15_eq
  · exact panel1FlatEven16_eq
  · exact panel1FlatEven17_eq
  · exact panel1FlatEven18_eq
  · exact panel1FlatEven19_eq
  · exact panel1FlatEven20_eq
  · exact panel1FlatEven21_eq
  · exact panel1FlatEven22_eq
  · exact panel1FlatEven23_eq

theorem panel1FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel1FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel1FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel1FlatOdd0_eq
  · exact panel1FlatOdd1_eq
  · exact panel1FlatOdd2_eq
  · exact panel1FlatOdd3_eq
  · exact panel1FlatOdd4_eq
  · exact panel1FlatOdd5_eq
  · exact panel1FlatOdd6_eq
  · exact panel1FlatOdd7_eq
  · exact panel1FlatOdd8_eq
  · exact panel1FlatOdd9_eq
  · exact panel1FlatOdd10_eq
  · exact panel1FlatOdd11_eq
  · exact panel1FlatOdd12_eq
  · exact panel1FlatOdd13_eq
  · exact panel1FlatOdd14_eq
  · exact panel1FlatOdd15_eq
  · exact panel1FlatOdd16_eq
  · exact panel1FlatOdd17_eq
  · exact panel1FlatOdd18_eq
  · exact panel1FlatOdd19_eq
  · exact panel1FlatOdd20_eq
  · exact panel1FlatOdd21_eq
  · exact panel1FlatOdd22_eq
  · exact panel1FlatOdd23_eq

theorem panel1FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel1FlatCache.EnclosesCanonical
      ⟨1, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel1FlatDefect
    rw [panel1FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel1DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel1FlatEvenComponents).get i)
    rw [panel1FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel1OuterLengthTable
      .even ⟨1, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel1FlatOddComponents).get i)
    rw [panel1FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel1OuterLengthTable
      .odd ⟨1, by decide⟩ i

end RHP2Bridge
