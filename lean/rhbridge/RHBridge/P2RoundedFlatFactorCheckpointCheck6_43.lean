import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel6FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel6FlatComponentChunk43

end RHP2Bridge
