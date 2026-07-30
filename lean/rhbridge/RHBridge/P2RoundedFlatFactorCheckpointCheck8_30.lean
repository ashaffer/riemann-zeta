import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel8FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel8FlatComponentChunk30

end RHP2Bridge
