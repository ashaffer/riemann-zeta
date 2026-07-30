import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel23FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel23FlatComponentChunk47

end RHP2Bridge
