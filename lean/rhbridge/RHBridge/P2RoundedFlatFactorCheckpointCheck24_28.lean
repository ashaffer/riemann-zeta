import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel24FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel24FlatComponentChunk28

end RHP2Bridge
