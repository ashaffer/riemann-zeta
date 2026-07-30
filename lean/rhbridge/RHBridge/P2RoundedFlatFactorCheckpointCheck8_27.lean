import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel8FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel8FlatComponentChunk27

end RHP2Bridge
