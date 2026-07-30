import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel23FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel23FlatComponentChunk34

end RHP2Bridge
