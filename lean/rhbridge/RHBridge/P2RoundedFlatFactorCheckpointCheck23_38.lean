import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel23FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel23FlatComponentChunk38

end RHP2Bridge
