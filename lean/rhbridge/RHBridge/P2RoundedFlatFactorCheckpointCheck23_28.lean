import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel23FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel23FlatComponentChunk28

end RHP2Bridge
