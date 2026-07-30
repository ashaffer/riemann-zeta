import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel23FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel23FlatComponentChunk25

end RHP2Bridge
