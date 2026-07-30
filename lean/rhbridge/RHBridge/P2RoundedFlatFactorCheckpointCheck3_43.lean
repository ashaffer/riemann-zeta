import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel3FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel3FlatComponentChunk43

end RHP2Bridge
