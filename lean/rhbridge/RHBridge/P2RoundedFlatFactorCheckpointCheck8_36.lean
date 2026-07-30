import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel8FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel8FlatComponentChunk36

end RHP2Bridge
