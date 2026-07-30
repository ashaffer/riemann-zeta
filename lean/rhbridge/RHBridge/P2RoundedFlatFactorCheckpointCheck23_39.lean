import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel23FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel23FlatComponentChunk39

end RHP2Bridge
