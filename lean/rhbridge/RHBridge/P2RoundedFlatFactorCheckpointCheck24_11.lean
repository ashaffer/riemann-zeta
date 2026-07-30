import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk11 :
    P2RoundedFactorCheckpointData.panel24FlatEven11 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel24FlatEven11_eq :
    P2RoundedFactorCheckpointData.panel24FlatEven11 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  exact panel24FlatComponentChunk11

end RHP2Bridge
