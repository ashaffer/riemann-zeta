import RHBridge.P2RoundedFactorCheckpoint14
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_defect
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_0
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_1
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_2
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_3
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_4
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_5
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_6
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_7
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_8
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_9
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_10
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_11
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_12
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_13
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_14
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_15
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_16
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_17
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_18
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_19
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_20
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_21
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_22
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_23
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_24
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_25
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_26
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_27
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_28
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_29
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_30
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_31
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_32
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_33
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_34
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_35
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_36
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_37
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_38
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_39
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_40
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_41
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_42
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_43
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_44
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_45
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_46
import RHBridge.P2RoundedFlatFactorCheckpointCheck14_47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter
open P2RoundedDirectOuterComponent

theorem panel14FlatEvenComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel14FlatEvenComponents).get i =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel14FlatEvenComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel14FlatEven0_eq
  · exact panel14FlatEven1_eq
  · exact panel14FlatEven2_eq
  · exact panel14FlatEven3_eq
  · exact panel14FlatEven4_eq
  · exact panel14FlatEven5_eq
  · exact panel14FlatEven6_eq
  · exact panel14FlatEven7_eq
  · exact panel14FlatEven8_eq
  · exact panel14FlatEven9_eq
  · exact panel14FlatEven10_eq
  · exact panel14FlatEven11_eq
  · exact panel14FlatEven12_eq
  · exact panel14FlatEven13_eq
  · exact panel14FlatEven14_eq
  · exact panel14FlatEven15_eq
  · exact panel14FlatEven16_eq
  · exact panel14FlatEven17_eq
  · exact panel14FlatEven18_eq
  · exact panel14FlatEven19_eq
  · exact panel14FlatEven20_eq
  · exact panel14FlatEven21_eq
  · exact panel14FlatEven22_eq
  · exact panel14FlatEven23_eq

theorem panel14FlatOddComponents_get_eq
    (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel14FlatOddComponents).get i =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get i := by
  simp only [P2RoundedFactorCheckpointData.panel14FlatOddComponents,
    Vector.get_ofFn]
  fin_cases i
  · exact panel14FlatOdd0_eq
  · exact panel14FlatOdd1_eq
  · exact panel14FlatOdd2_eq
  · exact panel14FlatOdd3_eq
  · exact panel14FlatOdd4_eq
  · exact panel14FlatOdd5_eq
  · exact panel14FlatOdd6_eq
  · exact panel14FlatOdd7_eq
  · exact panel14FlatOdd8_eq
  · exact panel14FlatOdd9_eq
  · exact panel14FlatOdd10_eq
  · exact panel14FlatOdd11_eq
  · exact panel14FlatOdd12_eq
  · exact panel14FlatOdd13_eq
  · exact panel14FlatOdd14_eq
  · exact panel14FlatOdd15_eq
  · exact panel14FlatOdd16_eq
  · exact panel14FlatOdd17_eq
  · exact panel14FlatOdd18_eq
  · exact panel14FlatOdd19_eq
  · exact panel14FlatOdd20_eq
  · exact panel14FlatOdd21_eq
  · exact panel14FlatOdd22_eq
  · exact panel14FlatOdd23_eq

theorem panel14FlatCache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel14FlatCache.EnclosesCanonical
      ⟨14, by decide⟩ := by
  constructor
  · change RoundedRatPoly.Encloses 1 _
      P2RoundedFactorCheckpointData.panel14FlatDefect
    rw [panel14FlatDefect_eq]
    exact DefectPieces.assemble_encloses
      panel14DefectPieces_enclosesCanonical
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel14FlatEvenComponents).get i)
    rw [panel14FlatEvenComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel14OuterLengthTable
      .even ⟨14, by decide⟩ i
  · intro i
    change RoundedRatPoly.Encloses 1 _
      ((P2RoundedFactorCheckpointData.panel14FlatOddComponents).get i)
    rw [panel14FlatOddComponents_get_eq i]
    exact componentVectorFromTruncatedOuters_encloses
      P2RoundedCanonical.gridCells (by
        norm_num [P2RoundedCanonical.gridCells])
      generatedSphericalOuters_enclose
      P2RoundedFactorCheckpointData.panel14OuterLengthTable
      .odd ⟨14, by decide⟩ i

end RHP2Bridge
