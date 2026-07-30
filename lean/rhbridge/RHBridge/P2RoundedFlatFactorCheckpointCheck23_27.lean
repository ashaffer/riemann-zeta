import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel23FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel23FlatComponentChunk27

end RHP2Bridge
