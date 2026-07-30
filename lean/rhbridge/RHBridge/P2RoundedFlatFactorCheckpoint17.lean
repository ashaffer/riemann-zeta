import RHBridge.P2RoundedFactorCheckpoint17
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck17_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel17FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel17FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel17FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel17FlatEven0_eq
  · exact panel17FlatEven1_eq
  · exact panel17FlatEven2_eq
  · exact panel17FlatEven3_eq
  · exact panel17FlatEven4_eq
  · exact panel17FlatEven5_eq
  · exact panel17FlatEven6_eq
  · exact panel17FlatEven7_eq
  · exact panel17FlatEven8_eq
  · exact panel17FlatEven9_eq
  · exact panel17FlatEven10_eq
  · exact panel17FlatEven11_eq
  · exact panel17FlatEven12_eq
  · exact panel17FlatEven13_eq
  · exact panel17FlatEven14_eq
  · exact panel17FlatEven15_eq
  · exact panel17FlatEven16_eq
  · exact panel17FlatEven17_eq
  · exact panel17FlatEven18_eq
  · exact panel17FlatEven19_eq
  · exact panel17FlatEven20_eq
  · exact panel17FlatEven21_eq
  · exact panel17FlatEven22_eq
  · exact panel17FlatEven23_eq

theorem panel17FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel17FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel17FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel17FlatOdd0_eq
  · exact panel17FlatOdd1_eq
  · exact panel17FlatOdd2_eq
  · exact panel17FlatOdd3_eq
  · exact panel17FlatOdd4_eq
  · exact panel17FlatOdd5_eq
  · exact panel17FlatOdd6_eq
  · exact panel17FlatOdd7_eq
  · exact panel17FlatOdd8_eq
  · exact panel17FlatOdd9_eq
  · exact panel17FlatOdd10_eq
  · exact panel17FlatOdd11_eq
  · exact panel17FlatOdd12_eq
  · exact panel17FlatOdd13_eq
  · exact panel17FlatOdd14_eq
  · exact panel17FlatOdd15_eq
  · exact panel17FlatOdd16_eq
  · exact panel17FlatOdd17_eq
  · exact panel17FlatOdd18_eq
  · exact panel17FlatOdd19_eq
  · exact panel17FlatOdd20_eq
  · exact panel17FlatOdd21_eq
  · exact panel17FlatOdd22_eq
  · exact panel17FlatOdd23_eq

theorem panel17FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel17FlatCache.EnclosesCanonical
      ⟨17, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel17FlatDefect
    rw [panel17FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel17DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel17FlatEvenComponents).get i)
    rw [panel17FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel17OuterLengthTable
      .even ⟨17, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel17FlatOddComponents).get i)
    rw [panel17FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel17OuterLengthTable
      .odd ⟨17, by decide⟩ i

end RHP2Bridge
