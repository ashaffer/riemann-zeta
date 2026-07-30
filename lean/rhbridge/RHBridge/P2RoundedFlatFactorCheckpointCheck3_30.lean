import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel3FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel3FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel3FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel3TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel3FlatComponentChunk30

end RHP2Bridge
