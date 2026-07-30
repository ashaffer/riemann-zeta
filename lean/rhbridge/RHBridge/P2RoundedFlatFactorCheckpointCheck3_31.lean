import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel3FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel3FlatComponentChunk31

end RHP2Bridge
