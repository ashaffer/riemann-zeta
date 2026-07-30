import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel8FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel8FlatComponentChunk43

end RHP2Bridge
