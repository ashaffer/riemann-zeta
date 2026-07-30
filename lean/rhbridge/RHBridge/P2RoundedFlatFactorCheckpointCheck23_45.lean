import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel23FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel23FlatComponentChunk45

end RHP2Bridge
