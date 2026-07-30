import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel8FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel8FlatComponentChunk25

end RHP2Bridge
