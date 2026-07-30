import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel8FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel8FlatComponentChunk33

end RHP2Bridge
